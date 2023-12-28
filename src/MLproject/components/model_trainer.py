import pandas as pd 
import numpy as np 
import os 
from MLproject import logger 
from sklearn.linear_model import ElasticNet
import joblib
from MLproject.config.configuration import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config : ModelTrainerConfig ):
        self.config = config 

    def train(self):
        train_data = np.load(self.config.train_data_path)
        test_data = np.load(self.config.test_data_path)

        logger.info("Train and Test data loaded successfully")

        logger.info("Separate features (X) and target variable (y)")
        X_train = train_data[:, :-1]
        y_train = train_data[:, -1]

        X_test = test_data[:, :-1]
        y_test = test_data[:, -1]

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(X_train, y_train)
        logger.info("Train the model on the training data")

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name)) 
        logger.info("Save the trained model to a file using joblib")      
