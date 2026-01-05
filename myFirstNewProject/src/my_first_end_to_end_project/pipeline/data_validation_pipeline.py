from src.my_first_end_to_end_project.config.configuration import ConfigurationManager
from src.my_first_end_to_end_project.components.data_validation import DataValidation
from src.my_first_end_to_end_project.logger import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_columns()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> Stage : {STAGE_NAME} started execution <<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>> Stage: {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e