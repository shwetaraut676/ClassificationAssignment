# -- coding: utf-8 --
"""
Created on Sat Jan 13 12:22:55 2024

@author: Shweta
"""

from fastapi import FastAPI



# 1. Library imports
import uvicorn
#from fastapi import FastAPI
from Title import Title
#import numpy as np

import pickle
#import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)
print("Classifier loaded successfully.")
# 3. Index route, opens automatically on http://127.0.0.1:8000


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return with the confidence
@app.post('/predict')
def predict_title(data:Title):
    data = data.dict()
    print(data['title'])
    
    
    prediction = classifier.predict(data['title'])
    print("Prediction:", prediction)
    
    
    
    return {
        'prediction': prediction
    }
#uvicorn app:app --reload