from MLproject.entity.config_entity import DataTransformationConfig
from MLproject.components.data_transformation import DataTransformation
from MLproject.config.configuration import ConfigurationManager
from MLproject import logger 
from pathlib import Path


STAGE_NAME = 'Data Transformation stage'


class DataTransformationTrainingPipeline:

    def __init__(self):
        pass 

    
    def main(self):
        try :
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == 'True':
                config = ConfigurationManager()
                data_tranformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_tranformation_config)
                train_data, test_data = data_transformation.train_test_split()
                train_arr, test_arr = data_transformation.inititate_data_transformation(train_data, test_data)
            else:
                raise Exception("You data schema is not valid")
    
        except Exception as e:
            print(e) 




if __name__=="__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME} stage: {e}") 