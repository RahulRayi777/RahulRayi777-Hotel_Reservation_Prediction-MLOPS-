from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements=f.read().splitlines()

setup(
    name="Hotel_Reservations_Project",
    version="0.1",
    author="RahulRayi",
    packages=find_packages(),
    install_requires=requirements
)