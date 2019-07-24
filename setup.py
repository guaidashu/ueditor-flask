"""
Create by yy on 2019-07-24
"""
import os
import sys

from setuptools import setup, find_packages

about = {}

with open('flask_ueditor/__about__.py') as f:
    exec(f.read(), about)

if sys.argv[-1] == 'test':
    status = os.system('make check')
    status >>= 8
    sys.exit(status)

setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    long_description=__doc__,
    long_description_content_type="text/markdown",
    license=about['__license__'],
    url=about['__url__'],
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
