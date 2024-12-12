from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requuirements
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
    return requirements




setup(
name="Ml_project",
version="0.0.1",
author="vishal",
author_email="vishalraj857808@gamil.com",
packages=find_packages(),

## below we write all the requirement modules
# install_requires=['numpy', 'pandas']

##now, we want to get all modules from requirements.txt file
install_requires=get_requirements("requirements.txt")
)