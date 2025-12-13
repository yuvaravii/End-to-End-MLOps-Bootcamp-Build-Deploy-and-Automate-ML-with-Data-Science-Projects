import os
from pathlib import Path
import logging

project_name = "my_first_end_to_end_project"
logging.basicConfig(level=logging.INFO)

list_of_files_to_create = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",                # 
    f"src/{project_name}/components/__init__.py",     # for creating pipelines and can be imported anywhere within the project
    f"src/{project_name}/config/__init__.py",         # for configuration
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py", 
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",       # creting different pipelines for training and testing
    f"src/{project_name}/utils/__init__.py",          # any general functions are stored in utils
    f"src/{project_name}/utils/common_utils.py",      # common functions storage
    "tests",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",                                        # entire project as a package --> can be deployed in pypi environment
    "pyproject.toml",
    "README.md",
    "research/research.ipynb",
    "templates/index.html",
]

for filepath in list_of_files_to_create:
    file_path = Path(filepath)
    file_path.parent.mkdir(exist_ok=True, parents=True)
    if file_path.exists():
        logging.info(f"{filepath} already exists")
    else:
        with open(filepath, "w") as f:
            pass
        logging.info(f"created file: {filepath}")