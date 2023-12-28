from MLproject.entity.config_entity import ModelTrainerConfig
from MLproject.config.configuration import ConfigurationManager
from MLproject.components.model_trainer import ModelTrainer
from MLproject import logger 


STAGE_NAME = "Model Trainer stage"


class ModelTrianingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__=="__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrianingPipeline()
        obj.main()
        logger.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME} stage: {e}") 