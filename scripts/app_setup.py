import subprocess

# Define the Conda environment name and requirements file
conda_env_name = "image_app_env"
conda_requirements_file = "conda_requirements.txt"

# Create the Conda environment
create_env_command = f"conda create --name {conda_env_name} --file {conda_requirements_file}"
subprocess.call(create_env_command, shell=True)

# Activate the Conda environment
activate_env_command = f"conda activate {conda_env_name}"
subprocess.call(activate_env_command, shell=True)

# Run the main Python file (replace 'app.py' with your file's name)
app_launcher_file = "app_launcher.py"
subprocess.call(f"python scripts/{app_launcher_file}", shell=True)
