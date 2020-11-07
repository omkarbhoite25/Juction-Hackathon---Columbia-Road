import os, shutil
import datetime
import logging
import json
import random
import pandas as pd
from math import sqrt


from flask import (
    abort,
    Blueprint,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
    Response,
    session,
    jsonify,
    send_file)

from uuid import uuid4
import sys
from werkzeug.utils import secure_filename

from flask import current_app as app
landing = Blueprint('landing', __name__)


prediction_table={}


INDEX_TIME=0
INDEX_MEAN=1
INDEX_VAR=2
INDEX_TOTAL=3
INDEX_RATIO=4
INDEX_PREDICTED=5

df=pd.read_csv("https://raw.githubusercontent.com/omkarbhoite25/Juction-Hackathon-Columbia-Road/main/datasets/transaction_best_costumers.csv")
costumers = (df.drop_duplicates(subset = ["CUST_CODE"])['CUST_CODE']).to_list()
db_costumer = (df.drop_duplicates(subset = ["CUST_CODE"])[['CUST_CODE','CUST_LIFESTAGE']])
allproducts = pd.read_csv("https://raw.githubusercontent.com/omkarbhoite25/Juction-Hackathon-Columbia-Road/main/datasets/sustDataset.csv")


@landing.route('/', methods=['GET'])
def index():
    return jsonify({"Message" : "Hello from PREDICTO :)"})

@landing.route('/update/test', methods = ['POST'])
def test():
    return jsonify({"TEST" : "Hi"})

@landing.route('/update/transaction', methods = ['POST'])
def new_transaction():
    content = request.get_json()

    data=request.get_json()
    #Simulate the online learnig
    for row in data:
        costumer=row['customer']
        timestamp=row["timestamp"]

        for p in row['items']:
            category=p["cat_id"]
            #cat=p["cat_id"]

            if costumer not in prediction_table:
              prediction_table[costumer]={}
            if (category not in prediction_table[costumer]):
              prediction_table[costumer][category]=[timestamp, 0, 0, 0,0,1]
            else:
                period=sub_timestamp(timestamp, prediction_table[costumer][category][INDEX_TIME])
                if (prediction_table[costumer][category][INDEX_MEAN]==0):
                  prediction_table[costumer][category][INDEX_TIME]=timestamp
                  prediction_table[costumer][category][INDEX_MEAN]=period
                  prediction_table[costumer][category][INDEX_VAR]=0.2
                  prediction_table[costumer][category][INDEX_TOTAL]=1
                else:
                  old_mean=prediction_table[costumer][category][INDEX_MEAN]
                  old_variance=prediction_table[costumer][category][INDEX_VAR]
                  total_products=prediction_table[costumer][category][INDEX_TOTAL]+1

                  prediction_table[costumer][category][INDEX_TIME]=timestamp
                  new_mean=old_mean+(period-old_mean)/total_products
                  prediction_table[costumer][category][INDEX_MEAN]=new_mean
                  prediction_table[costumer][category][INDEX_VAR]=sqrt((old_variance+(period-old_mean)*(period-new_mean))/total_products)
                  prediction_table[costumer][category][INDEX_TOTAL]=total_products
                  prediction_table[costumer][category][INDEX_PREDICTED]=0

                  if(prediction_table[costumer][category][INDEX_MEAN]!=0):
                    prediction_table[costumer][category][INDEX_RATIO]=prediction_table[costumer][category][INDEX_VAR]/prediction_table[costumer][category][INDEX_MEAN]
    #print(row['c1'], row['c2'])
    return jsonify(prediction_table)

@landing.route('/get/suggestion')
def suggestion():
    c=request.args.get("customer")
    timestamp=int(request.args.get("timestamp"))

    age=db_costumer[db_costumer['CUST_CODE']=='CUST0000880709']['CUST_LIFESTAGE'].to_list()[0]

    grocery_recommended = []
    if(c in prediction_table):
        grocery_list=[]
        new_item = []
        for p, stats in prediction_table[c].items():
            #print(p)
            #print(str(stats[INDEX_RATIO]) +"   " +str(stats[INDEX_TOTAL])+ "   "+str(stats[INDEX_PREDICTED]))
            if (stats[INDEX_RATIO]<0.2 and stats[INDEX_TOTAL]>2 and stats[INDEX_PREDICTED]==0):
                from_last_purchase=sub_timestamp(timestamp,stats[INDEX_TIME])
                if(from_last_purchase>(stats[INDEX_MEAN]-stats[INDEX_VAR]) and from_last_purchase<(stats[INDEX_MEAN]+stats[INDEX_VAR])):
                    print("dentro")
                    #print("from_last_purchase: "+str(from_last_purchase)+" mean "+str(stats[INDEX_MEAN])+" var "+str(stats[INDEX_VAR]))
                    #       print("BUY "+ str(p))
                    prediction_table[c][p][INDEX_PREDICTED]=1
                    grocery_list.append(p)

                ##Check if element bought inside the range
                #from_ = timestamp- stats[INDEX_VAR]*24*60*60
                #to_ = timestamp+ stats[INDEX_VAR]*24*60*60

                #d_tmp=df.loc[(df['PROD_CODE_10'] ==p) & (df['CUST_CODE'] == c) & (df["TIMESTAMP"]>=from_) & (df["TIMESTAMP"]<=to_) ]
                #if d_tmp.empty:
                #  failure=failure+1
                #else:
                #  success=success+1
                print(grocery_list)
        if len(grocery_list)>0:
            print(str((datetime.datetime.fromtimestamp(timestamp)).date()) +"***"+str(timestamp)+" "+str(c) +" maybe wants to buy: "+str(grocery_list))
            #print(index)
            #print(str((datetime.datetime.fromtimestamp(timestamp)).date()) +" "+str(c) +" maybe wants to buy: "+str(grocery_list))
            for product_class in grocery_list:
                df_sub = allproducts.loc[allproducts["PROD_CODE_10"] == product_class ]
                new_item = df_sub.loc[(df_sub["SUST_IDX"].min()) == df_sub["SUST_IDX"]]
                if (new_item.loc[new_item["CUST_LIFESTAGE"] == age].empty == False):
                    new_item = new_item.loc[new_item["CUST_LIFESTAGE"] == age]
                else:
                    new_item = new_item.sample()
                grocery_recommended.extend(new_item["PROD_CODE"].to_list())
    #print(str((datetime.datetime.fromtimestamp(timestamp)).date()) +" "+str(c) +" maybe wants to buy: "+str(grocery_recommended))

    return jsonify({"Message" : "Amazing", "Products":grocery_recommended})

def sub_timestamp(timestamp_1, timestamp_2):
  t1 = datetime.datetime.fromtimestamp(int(timestamp_1))
  t2 = datetime.datetime.fromtimestamp(int(timestamp_2))

  return (t1-t2).days
