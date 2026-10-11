from setuptools import find_packages, setup

def get_requirements(file_path:str)->list[str]:
    '''
    This function will return the list of requiremnts
    '''
    HYPHEN_E_D_VERSION = '-e .'
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    
    requirements=[req.replace("\n", "") for req in requirements]
    
    if HYPHEN_E_D_VERSION in requirements:
        requirements.remove(HYPHEN_E_D_VERSION)
    
    return requirements


setup(
    name = "Student-Performance-Predictor",
    version = "0.0.1",
    author = "Izhan Shaikh",
    author_email = "izhanshk26@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')
)