from src.my_first_end_to_end_project.logger import logger
from src.my_first_end_to_end_project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.my_first_end_to_end_project.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.my_first_end_to_end_project.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.my_first_end_to_end_project.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.my_first_end_to_end_project.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started execution <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>> Stage: {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started execution <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>> Stage: {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started execution <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>> Stage: {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started execution <<<<<")
    model_training = ModelTrainingPipeline()
    model_training.initiate_model_trainer()
    logger.info(f">>>> Stage: {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>> Stage : {STAGE_NAME} started execution <<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.initiate_model_evaluation()
    logger.info(f">>>> Stage: {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e