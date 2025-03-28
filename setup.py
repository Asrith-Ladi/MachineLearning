#find_packages will automatically find out all the packages 
# that are available in the entire machine learning application 
# in the directory we created.
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[requirement.replace('\n','') for requirement in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
    
#metadata information about the project
setup(
    name='MachineLearning',
    version='0.0.1',
    author='Asrith',
    author_email='asrith.ladi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)