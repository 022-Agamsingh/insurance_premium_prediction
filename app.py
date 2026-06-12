from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import JSONResponse
import pandas as pd
from Model.predict import predict_output
from schema.prediction_response import prediction_response
from schema.user_input import UserInput
from Model.predict import predict_output





app =FastAPI()


@app.get('/')
def home():
    return {'message':'WELCOME TO INSURANCE PREMIUM Prediction api'} 

@app.get('/health')
def health_check():
    return {
        'status':'ok',
        'message':'API is healthy and running',  
        'model_version':'1.0'
    }



@app.post('/predict',response_model=prediction_response)
def predict(data : UserInput):

    user_input= {
            'bmi':data.bmi,
            'age_group':data.age_group,
            'lifestyle_risk':data.lifestyle_risk,
            'city_tier':data.city_tier,
            'income_lpa':data.income_lpa,
            'occupation':data.occupation
             }
    try:
    


     prediction=predict_output(user_input)
    
     return JSONResponse(status_code=200, content={"prediction": prediction})
    except Exception as e:
       return JSONResponse(status_code=500, content={"error": str(e)})