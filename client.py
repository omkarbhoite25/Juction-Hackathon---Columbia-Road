import pandas as pd
import regex as re
import requests
import time
import json

finalDB = pd.read_csv('https://raw.githubusercontent.com/omkarbhoite25/Juction-Hackathon-Columbia-Road/main/datasets/transaction_best_costumers.csv')
API_ENDPOINT = "http://localhost:5000/update/transaction"
finalDB = finalDB[finalDB['CUST_CODE']=='CUST0000561725']
timestamp = sorted(set(finalDB['TIMESTAMP']))
timestamp = filter(lambda x: x < 1163452400, timestamp)

for t in timestamp:
  batch = finalDB[finalDB['TIMESTAMP']==t]
  batch = batch[['PROD_CODE','PROD_CODE_10','CUST_CODE','CUST_LIFESTAGE','BASKET_ID']]
  batch_json = []
  batch = batch.groupby(['CUST_CODE','CUST_LIFESTAGE','BASKET_ID']).sum()
  order_obj = {}
  for index, row in batch.iterrows():
    order_obj['id'] = index[2]
    order_obj['timestamp'] = t
    order_obj['customer'] = index[0]
    order_obj['customer_info'] = index[1]
    order_obj['items'] = []
    prods = re.findall("PRD\d{6}", row['PROD_CODE'])
    categs = re.findall("C\w\d{5}", row['PROD_CODE_10'])
    for i in range(len(prods)):
      basket_obj = {
          'prod_id': prods[i],
          'cat_id': categs[i]
      }
      order_obj['items'].append(basket_obj)
    batch_json.append(order_obj)
  r = requests.post(url = API_ENDPOINT, json=batch_json)
  print(time.strftime('%Y-%m-%d', time.localtime(t)))
  for tim in range(t,t+140000,20000):
    PARAMS = {'customer': 'CUST0000561725', 'timestamp': tim }
    r = requests.get(url = "http://localhost:5000/get/suggestion", params = PARAMS)
    print(r.text)
  time.sleep(0.5)
