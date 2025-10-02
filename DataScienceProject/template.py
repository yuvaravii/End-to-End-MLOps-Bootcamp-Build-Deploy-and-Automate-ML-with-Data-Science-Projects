
import os 
from pathlib import Path
import logging

# need to log all the actions taken
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "datascience"

list_of_files = [
    ".github/workflows/.gitkeep",    # for github actions and CI/CD pipeline
    f"src/{project_name}/__init__.py",   # the constructor __init__.py is needed to identify this as package, and I can import from anywhere.
    f"src/{project_name}/components/__init__.py",   # the components(class, package etc.) to be orchestrated in a pipeline are stored here.
    f"src/{project_name}/utils/__init__.py",     # project's generic requirements are stored here
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",   # contains collections of all the pipeline
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",          # storing the machine learning params while training models
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",   # for storing all the plugs and plays here
    "template/index.html",
    "app.py"
]

for filePath in list_of_files:
    filePath = Path(filePath)
    fileDir, fileName= os.path.split(filePath)

    if fileDir != "":
        os.makedirs(fileDir,exist_ok=True)
        logging.info(f"Creating directories : {fileDir} for the file : {fileName}")
    
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath, "w") as f:
            pass 
            logging.info(f"Creating empty files : {filePath}")
    
    else:
        logging.info(f"{fileName} is already existing.")
