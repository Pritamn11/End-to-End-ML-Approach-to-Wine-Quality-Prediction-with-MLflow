from MLproject.constants import *
from MLproject.utils.common import read_yaml, create_directories
from MLproject.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                config_filepath = CONFIG_FILE_PATH):
        
        self.config = read_yaml(config_filepath)

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