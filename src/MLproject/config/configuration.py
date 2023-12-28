from MLproject.constants import *
from MLproject.utils.common import read_yaml, create_directories
from MLproject.entity.config_entity import (DataIngestionConfig, 
                                            DataValidationConfig, 
                                            DataTransformationConfig,
                                            ModelTrainerConfig)



class ConfigurationManager:
    def __init__(self,
                config_filepath = CONFIG_FILE_PATH,
                schema_filepath = SCHEMA_FILE_PATH,
                params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(schema_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        initialize = self.config.data_ingestion 

        create_directories([initialize.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=initialize.root_dir,
            source_URL=initialize.source_URL,
            local_data_file=initialize.local_data_file,
            unzip_dir= initialize.unzip_dir
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation 
        schema = self.schema.COLUMNS 

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            unzip_data_dir= config.unzip_data_dir,
            all_schema= schema,
        )    

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        transformation_config = self.config.data_transformation 

        create_directories([transformation_config.root_dir]) 

        data_transformation_config = DataTransformationConfig(
            root_dir= transformation_config.root_dir,
            data_path= transformation_config.data_path,
            train= transformation_config.train,
            test= transformation_config.test 
        )    
        
        return data_transformation_config
    


    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer 
        params = self.params.ElasticNet 
        schema = self.schema.TARGET_COLUMN 

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path= config.test_data_path,
            model_name= config.model_name,
            alpha= params.alpha,
            l1_ratio= params.l1_ratio,
            target_column= schema.name 
        )

        return model_trainer_config