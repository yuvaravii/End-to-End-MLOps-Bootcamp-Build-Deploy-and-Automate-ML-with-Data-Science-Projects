# Copilot Instructions for End-to-End MLOps Bootcamp

## Project Overview
This repository demonstrates a modular, production-ready MLOps pipeline for machine learning projects. The workflow covers data ingestion, validation, transformation, model training, and evaluation, with strong emphasis on configuration management, reproducibility, and experiment tracking.

## Key Architectural Patterns
- **Modular Design:** Each pipeline stage (ingestion, validation, transformation, training, evaluation) is implemented as a separate component in `src/my_first_end_to_end_project/components/` and orchestrated via pipeline scripts in `src/my_first_end_to_end_project/pipeline/`.
- **Configuration Management:** All settings are managed via YAML files (`config/config.yaml`, `params.yaml`, `schema.yaml`). Constants for file paths are defined in `src/my_first_end_to_end_project/constants/`.
- **Entities & Dataclasses:** Use dataclasses in `src/my_first_end_to_end_project/entity/` for configuration objects, ensuring type safety and clarity.
- **Common Utilities:** Shared functions (YAML handling, directory creation, JSON/bin serialization) are in `src/my_first_end_to_end_project/utils/common_utils.py`.
- **Logging:** Centralized logging is implemented in `src/my_first_end_to_end_project/logger/`, with logs written to `my_execution_logs/logged_summary.log`.
- **Experiment Tracking:** Model evaluation uses MLflow and Dagshub for experiment tracking and model registry. Credentials and URIs are set via environment variables or in code.

## Developer Workflows
- **Environment Setup:** Use the [uv](https://github.com/astral-sh/uv) package manager for Python environments. See `readme.md` for setup commands (`uv init --python 3.11`, `uv venv`, `uv add <package>`).
- **Build & Run:**
  - Install dependencies: `uv sync` or `pip install -r requirements.txt`
  - Run main pipeline: `python main.py`
  - Generate project template: `uv run python template.py`
- **Testing:** Place tests in `tests/`. (No test runner specified; add if needed.)
- **Jupyter Notebooks:** Use notebooks in `research/` for prototyping and debugging. Ensure correct working directory with `%pwd` and `os.chdir()`.
- **Docker:** Use `Dockerfile` for containerization. Build with `docker build -t <tag> .` and run as needed.

## Project-Specific Conventions
- **YAML Files Must Not Be Empty:** Always populate `config.yaml`, `params.yaml`, and `schema.yaml` before running pipelines.
- **Dataclasses for Entities:** Prefer dataclasses over manual `__init__` for configuration objects.
- **Component Importing:** Import configuration objects from `entity/`, not from configuration manager logic.
- **MLflow/Dagshub Integration:** Set tracking URIs and credentials explicitly. See model evaluation code for examples.
- **Logging:** All modules should use the centralized logger.

## Integration Points
- **MLflow/Dagshub:** Used for experiment tracking and model registry. Credentials are set in code or via environment variables.
- **Cookiecutter Alternative:** Use `template.py` for project scaffolding instead of external template tools.

## Example File References
- `src/my_first_end_to_end_project/components/data_ingestion.py`: Data ingestion logic
- `src/my_first_end_to_end_project/pipeline/data_ingestion_pipeline.py`: Pipeline orchestration
- `src/my_first_end_to_end_project/entity/config_entity.py`: Dataclass definitions
- `src/my_first_end_to_end_project/utils/common_utils.py`: Utility functions
- `src/my_first_end_to_end_project/logger/`: Logging setup
- `config/config.yaml`, `params.yaml`, `schema.yaml`: Configuration files

---
If any section is unclear or missing details, please provide feedback or specify which workflow/component needs more documentation.