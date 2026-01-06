import os
from src.my_first_end_to_end_project.logger import logger
from sklearn.model_selection import train_test_split
from src.my_first_end_to_end_project.entity.config_entity import DataTransformationConfig
import pandas as pd  

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
        
    ## We can utilize all the data transformation techniques here like PCA, Scaling, encoding and other here
    def split_train_test(self):
        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data)

        # save the train and test data
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info(f"Train test split completed. ")
        logger.info(f"Train data shape : {train.shape}")
        logger.info(f"Test data shape : {test.shape}")

        print(train.shape)
        print(test.shape)  
