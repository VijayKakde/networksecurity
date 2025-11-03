''' this is the setup.py file it iwll incluide an essential part of 
packginbg and distributing python
project . it is used by the setuptools module to define metadata and configuration 
for the project.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    ''' Returns the list of requirements from requirements.txt '''
    requirements_lst: List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            # Process each line 
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':  # Corrected condition
                    requirements_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found. Proceeding with empty requirements.")

    return requirements_lst
print(get_requirements())     
setup(
    name = "networksecurity",
    version = "0.0.1",
    author="vijay kakde",
    author_email="vijaykumarkakde77@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
