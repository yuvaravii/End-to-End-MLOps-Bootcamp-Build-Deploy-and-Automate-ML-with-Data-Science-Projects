
# My First New Project

Welcome to your first end-to-end MLOps project! This guide is designed for students to learn how to build, deploy, and automate machine learning workflows using industry best practices.

## Why Use Separate Environments?

Each project may require different libraries or package versions. Installing everything in a single environment can cause conflicts and waste storage. Always create a dedicated environment for each project.

## Setting Up Your Environment with uv

1. **Initialize your GitHub repository** (if you haven't already).
2. Run `uv init --python 3.11` to initialize the uv package manager in your project directory.
    > **Note:** `pip install uv` installs a Python wrapper, not the full Rust binary. For best performance and all features, install the Rust binary from the [official repository](https://github.com/astral-sh/uv#installation).
3. Run `uv venv` to create a new virtual environment for your project.
4. **Activate your environment**:
   - On Windows: `./.venv/Scripts/activate`
   - On macOS/Linux: `source ./.venv/bin/activate`
5. Use `uv add <package-name>` to add dependencies as needed.
6. Use `uv rm <package-name>` to remove packages you no longer need.
7. Run `uv sync` to synchronize dependencies listed in your configuration files.

> **Tip:** `uv` is preferred because it is written in Rust, making it faster than conda or Python's built-in venv.

## Prerequisites

- Python 3.11 or higher
- `uv` package manager ([installation guide](https://github.com/astral-sh/uv)).
    - If you use `pip install uv`, you get a Python wrapper, not the full Rust binary. For full features and speed, follow the official installation guide.

## Special Note for GitHub Codespaces

If you are using GitHub Codespaces and want to run Jupyter notebooks (`.ipynb` files), you may need to set up the kernel:

1. `uv add ipykernel`  
2. If that fails: `uv pip install ipykernel`
3. `python -m ipykernel install --user --name=.venv --display-name "Python (.venv)"`
4. Restart the application once done.

## Project Structure

- `main.py`: Entry point for the project
- `params.yaml`: Configuration file for hyperparameters and other settings
- `config/`: Contains configuration files
- `src/`: Source code for the project
- `tests/`: Test cases for the project
- `Dockerfile`: Docker configuration for containerizing the project
- `requirements.txt`: List of Python dependencies
- `setup.py`: Script for installing the project as a package
- `readme.md`: Project documentation

## Getting Started

1. Clone the repository from GitHub.
2. Install the required dependencies with `pip install -r requirements.txt` (or use `uv sync` if you are using uv).
3. Run the project using `python main.py`.

## Features

- Complete end-to-end machine learning workflow
- Modular and organized code structure
- Easy configuration management
- Built-in logging and exception handling
- Docker support for reproducibility

## Step 1: Create Project Template

You can use a package like Cookiecutter to create templates, but for this project, a custom script `template.py` is provided. Run:

```bash
uv run python template.py
```

This will set up the project structure by creating necessary directories and files.

## Step 2: Logging System Setup

Logging is essential for debugging and understanding the flow of execution. All logging is handled in `src/my_first_end_to_end_project/logger`. Logs are stored in the `my_execution_logs` directory as `logged_summary.log`.

## Step 3: Common Functionality

Common functions used across modules are stored in `src/my_first_end_to_end_project/utils/common_utils.py`.

### Handling YAML Files

- Use `ConfigBox` for configuration (immutable, safer than dict for configs).
- Use the `ensure_annotations` decorator to enforce type safety in functions.
    - The `ensure` package is third-party and must be installed: `pip install ensure`

Example:

```python
from ensure import ensure_annotations

@ensure_annotations
def get_product(x: int, y: int) -> int:
        return x * y
```

## Common Utility Functions

1. `read_yaml`
2. `create_directories`
3. `save_json`
4. `load_json`
5. `save_bin` (save model)
6. `load_bin` (load model)

## Step 4: ML Pipeline Creation

### Workflow Steps

1. Update `config.yaml` (data source management --> data input, loading etc.) ; The yaml file should not be empty
2. Update `schema.yaml` (data validation and schema --> Schema management of input data); The yaml file should not be empty
3. Update `params.yaml` (parameter management, managing all the parameters) ; The yaml file should not be empty
4. Update the entity module (for modular coding)
    - Here we are defining the dataclass which is general, that can be imported in the configuration manager.
5. Update the configuration manager in `src/config` (define configuration classes and constants)
    - To update the configuration manager, we need to read all the Yaml file 
    - YAML file cannot be directly called into the function and read
        - We navigate to `src/my_first_end_to_end_project/constants` and write where the yaml directories are located.
        - These constants are folder, which contains where the .yaml directories are stored.
            ```
            # within constants/__init__.py
            from pathlib import Path


            CONFIG_FILE_PATH = Path("config/config.yaml")
            PARAMS_FILE_PATH = Path("params.yaml")
            SCHEMA_FILE_PATH = Path("schema.yaml")
            ```   
        - After updating entity with general dataclass of data_ingestion, update the configuration manager 
6. Update components (modular pipeline steps)
    - On completion of the data ingestion component, we need to create a python file for performing the data ingestion.
    - create a python file in `src/my_first_end_to_end_project/component`
    - now write the code for loading the configuration manager, function for downloading data and unzipping it.
7. Update the pipeline (training --> batch prediction etc.)
    - within `src/my_first_end_to_end_project/pipeline` --> create a folder `01_data_ingestion.py`
8. Update `main.py` (entry point)

### Typical ML Pipeline Stages

1. Data Ingestion
    - Create a sample file in `research\01_data_ingestion.ipynb`
    - Check the current working directory `%pwd` then ensure, they are in the root folder of the project else use cmd `os.chdir("../")`
    - update the `config.yaml` file
        - input for data ingestion file, now navigate to `config.yaml` file, write this down
            ```
            artifacts_root: artifacts

            data_ingestion:
                root_dir: artifacts/data_ingestion
                source_URL: https://github.com/krishnaik06/datasets/raw/refs/heads/main/winequality-data.zip  # Connect to database or API or any other data source
                local_data_file: artifacts/data_ingestion/data.zip
                unzip_dir: artifacts/data_ingestion
            ``` 
        - now to test all, move to `research/01_data_ingestion.ipynb`
            - usage of dataclass and pathlib for more functionality
            - Just like how we use the `ensure_annotations` to set the datatype for the arguments in **functions**, we use dataclass for ensuring the datatype of input arguments to the **class**
                - We used to write the `def __init__(self, name:str, .....): then self.ky1 = name etc.` inorder to overcome this clutter the dataclass is used.
                - Traditional method:
                    ```
                    class dataIngestionConfig:
                        def __init__(self, root_dir: Path, source_URL: str, local_data_file: Path):
                            self.root_dir = root_dir
                            self.source_URL = source_URL
                            self.local_data_file = local_data_file
                    ```
                - The same code can be written as 
                    ```
                    @dataclass
                    class dataIngestionConfig:
                        root_dir: Path
                        source_URL: str
                        local_data_file: Path
                    ```
                - *Note* : It is wise to use self and init method, if you are using the default path.
2. Data Validation
3. Data Preprocessing
4. Model Training
5. Model Evaluation

#### Why modular coding ?
- This pipeline can be built using the .ipynb notebook as well, however we would prefer modular coding as they are the production ready coes.
- The pipelines can be tested in .ipynb notebooks, but cannot be used in the production as they make it complex to connect with front end and dataflow management too.







## License

This project is licensed under the MIT License.







