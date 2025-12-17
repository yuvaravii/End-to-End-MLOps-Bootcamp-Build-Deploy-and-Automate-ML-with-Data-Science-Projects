# Step 1: Creating environment and activating it
- environment is created using the uv package manager
- python version used is 3.11
- cmd  used 
```cmd
uv init --python 3.11
uv venv
.\.venv\Scripts\activate
```

```bash
uv init --python 3.11
uv sync
source ./.venv/bin/activate    # if bash
clear                           # to clear all the above information in bash
```

- The environment can be created in multiple ways
1. using conda
2. using uv
3. using python 

- I preferred uv because they are written in rust, thus the executions are faster than the conda and python- 


# Step 2: Create templates.py
- we can use package called cookiecutter to create templates for our project
- Since it is first, we can create a template for our project

```cmd
uv run setup.py
```
The above code will run and setting the project up.

# Step 3: logging of the setup
- We are logging each movement happening in the project, thus logger is necessary.
- Why logging is essential?
    - Logging is esesential, as they are easy to debug and understand the flow of execution. Also, we can include the fallback mechanism where the system fails frequently.
- How to log them?
    - They can be logged using logger.info(), however they are multiple exceptions and errors that can be handled efficiently and catched easily.
- In this project the entire logging is preferred to be in logger file present in 
```/workspaces/End-to-End-MLOps-Bootcamp-Build-Deploy-and-Automate-ML-with-Data-Science-Projects/myFirstNewProject/src/my_first_end_to_end_project/logger```
    - The logger function is written within the logger folder only, thus can be imported as __init__ file is available within it.
    - Created a basic logging function in ```logger/__init__.py```






