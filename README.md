# PREDICTO
### Juction-Hackathon-Columbia-Road
------------
Predicto is a AI able to predict the utilities you need when you need them. It will be able to fill the shopping cart of your customer as soon as they log in. It works with many different e-commerce platform with an effortless integration code. It work with just your transaction data and exploit bayesian regression to provide a concrete.

## REQUIREMENTS
 - Python Flusk
 - Basically everything was made with <3 and python
 
## DOCS
Our code is hosted on https://predicto.pythonanywhere.com/ free of charge and free of data. This means that you should feed the AI in order to get insights.
Remember, garbage in garbage out!  
We offer two API:
 - *POST /update/transaction* | This endpoint is expecting data coming in the form of:
 ```
     {
      'id': BASKET_ID,
      'timestamp': unixEpoch,
      'customer': CUST_CODE,
      'customer_info': CUST_LIFESTAGE,
      'items': [{
                    'prod_id': PROD_CODE,
                    'cat_id': PROD_CODE_10
               }]
     }
 ```
 - *GET /get/suggestion* | When provided with a JSON object as specified below the API will grant a prediction to the customer if relevant:
 ```
 REQUEST
 {
   'customer': CUST_CODE,
   'timestamp': unixEpoch
 }
 
 RESPONSE
 {
   "Message" : "Amazing/No Prediction Available",
   "Products": [PROD_CODE],
   "Categories": [PROD_CODE_10]
 }
 ```
 
## RUN
To run the validator is very easy to download the python notebook Simulator.ipny and run in the environment of your choice. The code can simulate a real situation and check the validity of the prediction using the dataset provided in this same repository.

## FUTURE WORK
A pluging for E-commerce platform would be our next step in order to bring this fast, efforless experience to each business. Tailored solution can be expanded and brought also into offline shopping enhancing the whole user experience and increasing the satisfaction and retetion rate. 

