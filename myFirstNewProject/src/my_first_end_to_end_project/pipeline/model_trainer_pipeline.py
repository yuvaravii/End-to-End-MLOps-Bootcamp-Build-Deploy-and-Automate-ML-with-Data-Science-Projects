from src.my_first_end_to_end_project.config.configuration import ConfigurationManager
from src.my_first_end_to_end_project.components.model_trainer import ModelTrainer
from src.my_first_end_to_end_project.logger import logger


STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> Stage : {STAGE_NAME} started execution <<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_model_trainer()
        logger.info(f">>>> Stage: {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e