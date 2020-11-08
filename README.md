# PREDICTO
### Juction-Hackathon-Columbia-Road
------------
Predicto is a AI-based predicting system able to predict your next shopping cart, what you need, when you need. It will be able to fill the shopping cart with your repetitive purchases as soon as your customer log in on the platform. It would work with many different e-commerce platform with small integration code needed.
Leveraging old transaction history Predicto will create, maintain, and iterate its bayesian model from which the prediction is drawn.
The model can be updated online and improve itself as the transaction history grows.

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

## USER EXPERIENCE
We envisioned a new and better user experience for the customers of the platform as can be see by the [following workflow](https://www.figma.com/file/nH156e9v4jv6iNkGMTFUJG/Untitled?node-id=6%3A526) 

## FUTURE WORK
A pluging for E-commerce platform would be our next step in order to bring this fast, efforless experience to each business. Tailored solution can be expanded and brought also into offline shopping enhancing the whole user experience and increasing the satisfaction and retetion rate.

# TEAM


