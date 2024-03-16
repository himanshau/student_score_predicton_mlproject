from setuptools import find_packages,setup 
from typing import List

HYPN_NOT='-e .'


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirments]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements 


setup(
name = 'mlprojects',
email = 'hs9011016@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)