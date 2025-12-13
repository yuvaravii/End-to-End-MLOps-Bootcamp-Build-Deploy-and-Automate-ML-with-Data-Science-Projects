# Step 1: Creating environment and activating it
- environment is created using the uv package manager
- python version used is 3.11
- cmd  used 
```cmd
uv init --python 3.11
uv venv
.\.venv\Scripts\activate
```
- The environment can be created in multiple ways
1. using conda
2. using uv
3. using python 

- I preferred uv because they are written in rust, thus the executions are faster than the conda and python


# Step 2: Create templates.py
- we can use package called cookiecutter to create templates for our project
- Since it is first, we can create a template for our project

```cmd
uv run setup.py
```
The above code will run and setting the project up.

# Step 3: logging of the setup ran




