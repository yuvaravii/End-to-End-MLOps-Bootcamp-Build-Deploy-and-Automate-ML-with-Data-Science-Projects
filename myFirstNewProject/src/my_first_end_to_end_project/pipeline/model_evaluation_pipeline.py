from src.my_first_end_to_end_project.config.configuration import ConfigurationManager
from src.my_first_end_to_end_project.components.model_evaluation import ModelEvaluation
from src.my_first_end_to_end_project.logger import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        # model_evaluation.eval_metrics()
        model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> Stage : {STAGE_NAME} started execution <<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>> Stage: {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e