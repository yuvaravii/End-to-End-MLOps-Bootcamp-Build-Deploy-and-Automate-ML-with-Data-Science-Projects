
# My First New Project

Welcome to your first end-to-end MLOps project! This guide is designed for students to learn how to build, deploy, and automate machine learning workflows using industry best practices.

## Why Use Separate Environments?

Each project may require different libraries or package versions. Installing everything in a single environment can cause conflicts and waste storage. Always create a dedicated environment for each project.

## Setting Up Your Environment with uv

1. **Initialize your GitHub repository** (if you haven't already).
2. Run `uv init --python 3.11` to initialize the uv package manager in your project directory.
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
- `uv` package manager ([installation guide](https://github.com/astral-sh/uv) or run `pip install uv`)

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

1. Update `config.yaml` (data source management)
2. Update `schema.yaml` (data validation and schema)
3. Update `params.yaml` (parameter management)
4. Update the entity module (for modular coding)
5. Update the configuration manager in `src/config` (define configuration classes and constants)
6. Update components (modular pipeline steps)
7. Update the pipeline (batch, training, etc.)
8. Update `main.py` (entry point)

### Typical ML Pipeline Stages

1. Data Ingestion
2. Data Validation
3. Data Preprocessing
4. Model Training
5. Model Evaluation

## License

This project is licensed under the MIT License.







