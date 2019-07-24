"""
Create by yy on 2019-07-24
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = "0.1.0"

setup(
    name="flask-ueditor",
    version=__version__,
    author="guaidashu",
    author_email="song42960@gmail.com",
    description="Flask ueditor Backstage, designed by yy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/guaidashu/ueditor-flask",
    packages=find_packages(),
    install_requires=[
        "qiniu >= 7.2.6",
        "requests >= 2.21.0",
        "Flask >= 1.0.2"
    ],
    classifiers=[
        "Topic :: components which used to coordinate ueditor to upload file.",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
