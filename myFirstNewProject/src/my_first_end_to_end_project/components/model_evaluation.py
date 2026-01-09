import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.my_first_end_to_end_project.entity.config_entity import (ModelEvaluationConfig)
from src.my_first_end_to_end_project.utils.common_utils import save_json
from pathlib import Path
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib

# import os
# os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/rj.workhub/End-to-End-MLOps-Bootcamp-Build-Deploy-and-Automate-ML-with-Data-Science-Projects.mlflow"
# os.environ["MLFLOW_TRACKING_USERNAME"] = "rj.workhub"
# os.environ["MLFLOW_TRACKING_PASSWORD"] = "88fff356ea218f9049140f5c41fb57fa3e757224"


class ModelEvaluation:
    def __init__(
            self,
            config:ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae= mean_absolute_error(actual,pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis =1)
        test_y = test_data[[self.config.target_column]]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            pred_value = model.predict(test_x)
            (rmse, mae, r2)= self.eval_metrics(test_y,pred_value)

            # saving metrics as local
            scores = {"rmse":rmse, "mae":mae, "r2":r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2",r2)
            mlflow.log_metric("mae", mae)

            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                # register the model
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model,"model") 