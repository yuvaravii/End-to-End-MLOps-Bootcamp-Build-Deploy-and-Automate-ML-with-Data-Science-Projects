# Step 1 : Environment Creation

## Objective:
- Since the developer are working in different projects, each project would require its own dependencies (like libraries, packages,frameworks etc..). If I compile all together in one environment the storage efficiency becomes low and each project dependencies might contradict with each other. So, we need distinct environment for each project.

## How to create environment using uv
- Ensure that you initalized your gitHub repo.
- ```uv init``` : This initalizes the uv package manager
- ```uv venv``` : for creating virtual environment.
- Ensure to activate your environment.
- ```uv add <your package name>```: for adding dependencies
- ```uv rm <your package name>``` : for removing package 
- ```uv sync``` : for syncing the dependencies

# Step 2 : Creating structure for the project.
- This can be easily done using *"cookieCutter"*
- But instead to practise them we create something called __"template.py"__

## Objective :
- To create a project structure template that standard and used across industries. Re-use them when required.

## How to create template.py
```python

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
    "template/index.html"
]

for filePath in list_of_files:
    filePath = Path(filePath)
    fileDir, fileName= os.path.split(filePath)

    if fileDir != "":
        os.makedirs(fileDir,exist_ok=True)
        logging.info(f"Creating directories : {fileDir} for the file : {fileName}")
    
    if (not.os.path.exists(filePath)) or (os.path.getsize(filepath)==0):
        with open(filePath, "w") as f:
            pass 
            logging.info(f"Creating empty files : {filePath}")
    
    else:
        logging.info(f"{fileName} is already existing.")
```


# Step 3 : Set up logging within the SRC folder's __init__.py file

```python
import os 
import sys
import logging


# structure of the configuratoin
logging_str =  "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"

logging.basicConfig

```