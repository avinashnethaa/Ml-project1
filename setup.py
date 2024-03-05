from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements (file_path:str)->List[str]:
    ''' This function will returns the list of requiremetns. 
    '''
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace('\n','') for req in requirments]
    
    if HYPEN_E_DOT in requirments:
        requirments.remove(HYPEN_E_DOT)
    
    return requirments

setup(
name='mlproject',
version='0.0.1',
author='Avinash',
author_email='aarchanapalli@gmail.com',
packages=find_packages(),
install_requirements = get_requirements('requirements.txt')
)