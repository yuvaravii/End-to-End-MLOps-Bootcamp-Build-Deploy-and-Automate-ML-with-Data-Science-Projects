# My First End-to-End Project

This is a template for building an end-to-end machine learning project with MLOps practices. It includes logging, configuration, and a modular structure for scalability.
- Since the developer are working in different projects, each project would require its own dependencies (like libraries, packages,frameworks etc..). If I compile all together in one environment the storage efficiency becomes low and each project dependencies might contradict with each other. So, we need distinct environment for each project.

## How to create environment using uv
- Ensure that you initalized your gitHub repo.
- ```uv init``` : This initalizes the uv package manager
- ```uv venv``` : for creating virtual environment.
- Ensure to activate your environment.
- ```uv add <your package name>```: for adding dependencies
- ```uv rm <your package name>``` : for removing package 
- ```uv sync``` : for syncing the dependencies

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
- This can be easily done using *"cookieCutter"*
- But instead to practise them we create something called __"template.py"__

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
  - This ensure_annotations helps to pass the arguments as mentioned in argument only.
    ```
    def get_product(x:int, y:int)-> int:
      return x*y   
    output = get_product(5,"3")
    print(output)  # output : "33333"

    # To overcome the above situation, we use ensure_annotations
    from ensure import ensure_annotations
    def get_product(x:int, y:int)-> int:
      return x*y

      # Now this will throw error
    ```

  ## Now building common functions that could be used all over the project
  1. read_yaml
  2. create_directories
  3. save_json
  4. load_json
  5. save_bin (save model)
  6. load_bin (load model)
- as from the above functions we can note that these functions are used across different files and common.

# Step-5: Creation of ML pipelines
## Workflow creation steps
1. update config.yaml
  - This file details about the data source management
  - Data source could be API, Datawarehouse , data lake etc.
  - Here we define, the data entry points, which are artifacts. Basically we are handling where the data is residing and how to fetch them into local repository, within local repository, where can we store them and fetch them.
  - Since the data after the above process resides in local folder, now we need to define the schema for better quality extraction, so that we can use them in modeling, that's why we have **schema.yaml**
2. update **schema.yaml**
  - Once the data is loaded, this yaml file ensures the data types and its validation --> input data schema
    - We shall be using dataclass decorator wiith normal class, but why ?
      - In normal class we will use ```self``` keyword, however when the decorator can use datatype itself.
    - We have created the data_ingestion in config.yaml
      - Now the same has be defined in the dataclass

3. update params.yaml 
  - Specifically used when the parameters are updated.
4. update the entity
  - This is used while modular coding.
5. update the configuration manager in src config
  - Here are we are creating the configuration class
  - To create that we need paths, Since these paths does not change we are going add them in constants ```myFirstNewProject/src/my_first_end_to_end_project/constants/__init__.py```
6. update the components
7. update the pipeline
  - Batch 
  - Training
8. update the main.py

## 1. Data Ingestion
## 2. Data Validation 
## 3. Data Preprocessing
## 4. Model training 
## 5. Model evaluations







