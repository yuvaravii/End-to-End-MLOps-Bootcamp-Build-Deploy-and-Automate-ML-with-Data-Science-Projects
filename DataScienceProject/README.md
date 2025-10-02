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

# Step 2 : 