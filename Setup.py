from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'

#this function will return a list of requirements
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    packages = find_packages(),
    author = 'Faisal',
    author_email = 'faisalmajeedpak2@gmail.com',
    install_requires=get_requirements('Requirement_txt')
                      
    )