import os
from MLproject import logger
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from MLproject.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config=DataTransformationConfig):
        self.config = config

    def get_data_transformation_object(self):
        try:
            numerical_features = [
                "fixed acidity",
                "volatile acidity",
                "citric acid",
                "residual sugar",
                "chlorides",
                "free sulfur dioxide",
                "total sulfur dioxide",
                "density",
                "pH",
                "sulphates",
                "alcohol",
            ]

            data_transformer = ColumnTransformer(
                transformers=[
                    ("standard_scaler", StandardScaler(), numerical_features),
                ]
            )

            preprocessor = Pipeline(steps=[("data_transformer", data_transformer)])

            return preprocessor

        except Exception as e:
            logger.info(f"Error in creating data transformation object: {e}")
            raise e

    def train_test_split(self):
        try:
            data = pd.read_csv(self.config.data_path)
            logger.info("Read the dataset as DataFrame")

            logger.info("train test split initiated")
            train_set, test_set = train_test_split(data)

            train_set.to_csv(
                os.path.join(self.config.root_dir, "train.csv"), index=False
            )
            test_set.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

            logger.info("Splited data into training and test sets")
            logger.info(train_set.shape)
            logger.info(test_set.shape)

            return (
                self.config.train,
                self.config.test,
            )

        except Exception as e:
            logger.info(f"Error in splitting train test sets: {e}")
            raise e

    def inititate_data_transformation(self, train_set, test_set):
        try:
            train_set = pd.read_csv(self.config.train)
            test_set = pd.read_csv(self.config.test)

            logger.info("Reading train and test dataset completed")
            logger.info("Obtaining preprocessor object")

            preprocessor_obj = self.get_data_transformation_object()

            target_feature = "quality"

            independent_feature = [
                "fixed acidity",
                "volatile acidity",
                "citric acid",
                "residual sugar",
                "chlorides",
                "free sulfur dioxide",
                "total sulfur dioxide",
                "density",
                "pH",
                "sulphates",
                "alcohol",
            ]

            # Separate features and target
            input_train_df = train_set.drop(columns=[target_feature], axis=1)
            target_train_df = train_set[target_feature]

            input_test_df = test_set.drop(columns=[target_feature], axis=1)
            target_test_df = test_set[target_feature]

            logger.info(
                f"Applying preprocessing object on training dataframe and test dataframe."
            )

            # Apply preprocessor
            train_df = preprocessor_obj.fit_transform(input_train_df)
            test_df = preprocessor_obj.transform(input_test_df)

            logger.info(
                "successfully applied preprocessor object on train and test data"
            )

            # Combine features and target
            train_arr = np.c_[train_df, np.array(target_train_df)]

            test_arr = np.c_[test_df, np.array(target_test_df)]
            logger.info("returning train_array and test_array")

            logger.info("Saving transformed train and test set in numpy file")
            np.save(os.path.join(self.config.root_dir,"train_arr.npy"), train_arr)
            np.save(os.path.join(self.config.root_dir,"test_arr.npy"), test_arr)


            return (
            train_arr,
            test_arr
        )

        except Exception as e:
            logger.info(f"Error in initiating data transformation: {e}")
            raise e