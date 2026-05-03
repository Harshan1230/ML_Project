from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    with open(file_path) as f:
        requirements = f.readlines()
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    return requirements

setup(
    name='mlProject',
    version='0.0.1',
    author="Harshan R K ",
    author_email="harshanrk3210@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
)