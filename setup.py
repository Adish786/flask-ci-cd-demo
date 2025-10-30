
from setuptools import setup, find_packages

setup(
    name="flask-app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.3.3",
        "pytest>=7.4.2",
        "gunicorn>=21.2.0",
    ],
)
