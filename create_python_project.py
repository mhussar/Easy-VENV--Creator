"""
Filename: create_python_project.py
Author: MGH
Company: Hitlab Studios
Created Date: 06/02/24
Last Modified: 09/24/24
Version: 1.0.0
Description: This module provides functionality for setting up a Python project
Usage: create_python_project.py 
License: MIT
Disclaimer: THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import subprocess
from datetime import datetime
import argparse

 
def create_python_project(date: str, project_path: str, python_version_path: str):
    # Create the project folder
    os.makedirs(project_path, exist_ok=True)

    # Path to the virtual environment
    venv_path = os.path.join(project_path, '.venv')
    
    # Create a virtual environment using the specified Python version
    subprocess.run([python_version_path, '-m', 'venv', venv_path])

    # Path to the Python executable in the virtual environment
    venv_python_path = os.path.join(venv_path, 'Scripts', 'python.exe')
    
    # Upgrade pip in the virtual environment
    subprocess.run([venv_python_path, '-m', 'pip', 'install', '--upgrade', 'pip'])

    # Create the readme_installs.txt file with the given instructions
    readme_content = f"""
{date}
 

## version of python used for the project
"{python_version_path}"

## project folder
{project_path}

## select interpreter
F1 F1 choose the recommended version of python for the project


## List of pip installs done for project so far:  
{venv_python_path} -m pip install --upgrade pip 

## example for installing other python packages - use at commandline
{venv_python_path} -m pip install pandas

"""

    readme_path = os.path.join(project_path, 'readme_installs.txt')
    with open(readme_path, 'w') as readme_file:
        readme_file.write(readme_content.strip())
 

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Set up a Python project with a virtual environment.')
    parser.add_argument('project_path', type=str, help='The path to the project directory')
    parser.add_argument('python_version_path', type=str, help='The path to the preferred Python executable')
    
    # Parse the arguments
    args = parser.parse_args()

    # Get the current date
    current_date = datetime.now()

    # Format the date as mm/dd/yyyy
    formatted_date = current_date.strftime("%m/%d/%Y")

    # Call the create_python_project function with the provided arguments
    create_python_project(str(formatted_date), args.project_path, args.python_version_path)


if __name__ == "__main__":
    main()
