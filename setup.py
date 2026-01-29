from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    Return list of requirements, excluding editable installs (-e .)
    """
    requirements = []

    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()

            # skip empty lines and editable installs
            if not line or line.startswith("-e"):
                continue

            requirements.append(line)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Manan",
    author_email="mananofc24@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
