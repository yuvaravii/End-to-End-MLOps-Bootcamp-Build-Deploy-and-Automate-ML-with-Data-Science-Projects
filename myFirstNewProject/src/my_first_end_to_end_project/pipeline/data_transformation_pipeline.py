from src.my_first_end_to_end_project.config.configuration import ConfigurationManager
from src.my_first_end_to_end_project.components.data_transformation import DataTransformation
from src.my_first_end_to_end_project.logger import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.split_train_test() 

if __name__ == "__main__":
    try:
        logger.info(f">>>>> Stage : {STAGE_NAME} started execution <<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>> Stage: {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e