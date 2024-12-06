# ---INFO-----------------------------------------------------------------------
"""
Praeceptus
"""
# ---DEPENDENCIES---------------------------------------------------------------
from setuptools import setup, find_packages


# ------------------------------------------------------------------------------
VERSION = "0.0.1"
with open("README.md", "r") as fh:
    LONG_DESCRIP = fh.read()
with open("requirements.txt", "r") as fh:
    REQUIREMENTS = fh.read().splitlines()


# ------------------------------------------------------------------------------
setup(
    name="praeceptus",
    version=VERSION,
    author="Triune AI",
    author_email="triune.ai@gmail.com",
    url="https://github.com/triune-ai/praeceptus.git",
    description="A python package for LLM assisted legal use-cases",
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIP,
    license="MIT license",
    packages=find_packages(exclude=["test"]),
    install_requires=REQUIREMENTS,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
