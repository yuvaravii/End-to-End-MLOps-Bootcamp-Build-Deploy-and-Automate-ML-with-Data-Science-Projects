import os
import pandas
from src.my_first_end_to_end_project.logger import logger
from src.my_first_end_to_end_project.entity import (DataValidationConfig)

class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config

    # def validate_all_columns(self)-> bool:
    #     try:
    #         validation_status = None

    #         data = pd.read_csv(self.config.unzip_data_dir)
    #         all_columns = list(data.columns)

            
    #         all_schema = self.config.all_schema.keys()

    #         for col in all_columns:
    #             if col not in all_schema:
    #                 validation_status = False
    #                 with open(self.config.STATUS_FILE, 'a') as f:
    #                     f.write(f"for {col} --> Validation status: {validation_status} \n")

    #             else:
    #                 validation_status= True
    #                 with open(self.config.STATUS_FILE,'a') as f:
    #                     f.write(f"for {col} --> Validation status: {validation_status} \n")

    #         return validation_status

    #     except Exception as e:
    #         raise e

    def validate_all_columns(self)-> bool:
        try:
            validation_status = True
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            schema = self.config.all_schema

            with open(self.config.STATUS_FILE, 'w') as f:
                # check all cols present in csv are in schema
                for col in all_cols:
                    if col not in schema:
                        validation_status = False
                        f.write(f"Column: {col} \n Validation status: {validation_status} \n Column not found in schema")
                    else:
                        expected_col_type = schema[col]
                        actual_col_type = str(data[col].dtype)

                        if expected_col_type != actual_col_type:
                            validation_status = False
                            f.write(f"Column: {col} \n Validation status: {validation_status} \n Data type match status : {validation_status} \n mismatch (expected type {expected_col_type} != actual data type {actual_col_type})\n ---\n")
                        else:
                            validation_status = True
                            f.write(f"Column: {col} \n Validation status: {validation_status} \n Data type MATCH (expected type {expected_col_type} == actual data type {actual_col_type}) \n ---\n")

                # check all cols present in schema present in csv or not
                for col in schema.keys():
                    if col not in all_cols:
                        validation_status = False
                        f.write(f"Column: {col} | Column missing in .csv file | Validation status : {validation_status} \n") 
            return validation_status
        except Exception as e:
            raise e