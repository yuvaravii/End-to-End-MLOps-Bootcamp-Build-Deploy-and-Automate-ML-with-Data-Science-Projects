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
    

@ensure_annotations
def create_directories(path_to_directories:list, verbose=True)->None:
    """
    Objective:
    - To create list of directories

    Args:
    - path_to_directories (list): List of path like input
    - ignore_log (bool, optional): whether to log or not

    Returns:
    - None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory Successfuly at: {path} 🥳")


@ensure_annotations
def save_json(path:Path, data:dict)->None:
    """
    Objective:
    - To save json data to a file

    Args:
    - path (Path): path like input where json file to be saved
    - data (dict): data to be saved in json file

    Returns:
    - None
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"Json file saved at: {path} 🥳")


@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """
    Objective:
    - To load json file and return the data

    Args:
    - path (Path): path like input where json file is saved

    Returns:
    - dict: data loaded from json file
    """
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    logger.info(f"Json file loaded from: {path} 🥳")
    return ConfigBox(data)

@ensure_annotations
def save_bin(data:Any, path:Path)->None:
    """
    Objective:
    - To save binary file using joblib

    Args:
    - data (Any): data to be saved in binary file
    - path (Path): path like input where binary file to be saved

    Returns:
    - None
    """
    with open(path, 'wb') as bin_file:
        joblib.dump(data, bin_file)
    logger.info(f"Binary file saved at: {path} 🥳")

@ensure_annotations
def load_bin(path:Path)->Any:
    """
    Objective:
    - To load binary file using joblib

    Args:
    - path (Path): path like input where binary file is saved

    Returns:
    - Any: data loaded from binary file
    """
    with open(path, 'rb') as bin_file:
        data = joblib.load(bin_file)
    logger.info(f"Binary file loaded from: {path} 🥳")
    return data