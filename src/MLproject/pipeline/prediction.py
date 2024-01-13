import joblib 
import pandas as pd 
import numpy as np 
from pathlib import Path 


 
class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts\model_trainer\model.joblib"))


    def predict(self, data):
        prediction = self.model.predict(data)
        
        return prediction


# if __name__=="__main__":
#     obj = PredictionPipeline()
#     data= np.array([8.1,0.38,0.28,2.1,0.066,13.0,30.0,0.9968,3.23,0.73,9.7])
#     data = data.reshape(1, -1)
#     print(obj.predict(data=data)) 
