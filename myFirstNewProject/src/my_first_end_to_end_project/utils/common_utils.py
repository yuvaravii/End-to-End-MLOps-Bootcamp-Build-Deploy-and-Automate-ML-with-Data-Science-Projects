import os
import yaml
import json
import joblib
import pickle
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from src.my_first_end_to_end_project.logger import logger
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """
    Objective:
    - To read YAML file and return
    
    Args:
    - Takes in path_to_yaml : path like input

    Raises:
    - ValueError: if Yaml file is not found/empty

    Returns:
    - ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} is loaded successfully 🥳")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("No values found within the yaml file")
    except Exception as e:
        raise e