# PREDICTO
### Juction-Hackathon-Columbia-Road
------------
Predicto is a AI able to predict the utilities you need when you need them. It will be able to fill the shopping cart of your customer as soon as they log in. It works with many different e-commerce platform with an effortless integration code. It work with just your transaction data and exploit bayesian regression to provide a concrete.

## REQUIREMENTS
 - Python Flusk
 - Basically everything was made with python <3
 
## DOCS
Our code is hosted on https://predicto.pythonanywhere.com/
We offer two API:
 - */update/transaction* | This endpoint is expecting data coming in the form of:
 ` {
      'id': BASKET_ID,
      'timestamp': unixEpoch,
      'customer': CUST_CODE,
      'customer_info': CUST_LIFESTAGE,
      'items': [{
                    'prod_id': PROD_CODE,
                    'cat_id': PROD_CODE_10
               }]
       }
 `
 - */get/suggestion* | When provided with a JSON object:
 `{'customer': CUST_CODE, 'timestamp': unixEpoch}`
 
## RUN
To run the validator is very easy to download the python notebook Simulator.ipny and run in the environment of your choice. The code can simulate a real situation and check the validity of the prediction using the dataset provided in this same repository.

## FUTURE WORK
A pluging for E-commerce platform would be our next step in order to bring this fast, efforless experience to each business. Tailored solution can be expanded and brought also into offline shopping enhancing the whole user experience and increasing the satisfaction and retetion rate. 

