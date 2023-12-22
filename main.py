from MLproject import logger
from MLproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline



STAGE_NAME = "Data Ingestion stage"

if __name__=="__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME} stage: {e}")
        raise e
