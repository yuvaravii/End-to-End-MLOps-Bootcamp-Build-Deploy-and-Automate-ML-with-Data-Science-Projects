# My First End-to-End Project

This is a template for building an end-to-end machine learning project with MLOps practices. It includes logging, configuration, and a modular structure for scalability.

## Prerequisites
- Python 3.11
- `uv` package manager (install via `pip install uv` or from [uv's website](https://github.com/astral-sh/uv))

# Step 1: Creating environment and activating it
- Environment is created using the `uv` package manager.
- Python version used is 3.11.
- Commands used:

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

- The environment can be created in multiple ways:
  1. Using conda
  2. Using uv
  3. Using Python's built-in venv

- I preferred `uv` because it is written in Rust, making executions faster than conda and Python's venv.

## In any case if you are github codespace then selection of kernel while executing ```.ipynb``` file becomes complex.
Use the following commands in bash in github codespace
1. ```uv add ipykernel```
2. Else : ```uv pip install ipykernel```
3. ```python -m ipykernel install --user --name=.venv --display-name "Python (.venv)"```
4. restart the application once done.

# Step 2: Create project template
- We can use a package called Cookiecutter to create templates for our project.
- Since this is our first project, we can create a custom template script.

```bash
uv run python template.py
```

The above command will run the template script and set up the project structure by creating necessary directories and files.

# Step 3: Logging system setup
- We log every action happening in the project, so a logger is necessary.
- Why is logging essential?
  - Logging is essential as it makes debugging and understanding the flow of execution easier. It also allows for fallback mechanisms when the system fails frequently.
- How to log them?
  - Logs can be created using `logger.info()`, and there are multiple exceptions and errors that can be handled efficiently and caught easily.
- In this project, the entire logging is handled in the logger file located at:
  ```
  src/my_first_end_to_end_project/logger
  ```
  - The logger function is written within the logger folder, and can be imported since an `__init__.py` file is available.
  - A basic logging function is created in `logger/__init__.py`.
  - Logs are stored in the "my_execution_logs" directory as "logged_summary.log".

# Step 4: Common functionality setup
- Common functions are used across different modules within the src folder, similar to the log function.
- These are stored in `src/my_first_end_to_end_project/utils/common_utils.py`.

## Handling yaml file
- it is essential to use **BoxConfigError** while handling Yaml file, as they are handled more efficiently.
    - ```Use dicts for data. Use ConfigBox for configuration.```
    - ConfigBox is unidirection, you can load it but does not get manipulated thus ConfigBox output are immutable.
    - can find the code and example in ```research.ipynb```

- Use **ensure_annotation** decorator while using YAML file.







