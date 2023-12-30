from MLproject.entity.config_entity import ModelEvaluationConfig
from MLproject.config.configuration import ConfigurationManager
from MLproject.components.model_evaluation import ModelEvaluation 
from MLproject import logger 


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:

    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        model_evalutaion_config = config.get_model_evaluation_config()
        model_config = ModelEvaluation(config=model_evalutaion_config)
        model_config.log_into_mlflow()


if __name__=="__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME} stage: {e}") 