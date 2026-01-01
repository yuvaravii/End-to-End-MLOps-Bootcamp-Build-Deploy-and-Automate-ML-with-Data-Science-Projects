from src.my_first_end_to_end_project.logger import logger
from src.my_first_end_to_end_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started execution <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>> Stage: {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e
