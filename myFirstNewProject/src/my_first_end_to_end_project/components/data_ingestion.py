## New component class
import os
import urllib.request as request
from src.my_first_end_to_end_project.logger import logger
from src.my_first_end_to_end_project.entity.config_entity import (DataIngestionConfig)
import zipfile


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config= config

    # downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info : {headers}")
        else:
            logger.info(f"The file already exists in the local repository")

    # extract the zip file
    def extract_zip_file(self):
        """
        Objective: To extract the zip file from the local repository
        arguments: NIL
        returns: returns None but loads the unzipped file into local repository
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
    
