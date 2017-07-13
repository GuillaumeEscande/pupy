#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import versioneer
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pupy",

    version = versioneer.get_version(),
    cmdclass = versioneer.get_cmdclass(),

    description = ("The pupy CLI tool"),
    long_description=read('README.md'),


    url = "https://gitlab.escande.ovh:2443/WorkTools/pupy.git",

    author = "Escande Guillaume",
    author_email = "escande.guillaume@gmail.com",
    
    license = "MIT",
    keywords = "",
    
    packages=['pupy'],
    
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    entry_points={
        'console_scripts': [
            'pupy=pupy.pupy:main',
        ]
    },
    setup_requires=['pytest-runner', 'pytest-pylint'],
    tests_require=['pytest', 'pylint'],
)
