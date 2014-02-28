#!/usr/bin/env python
import os
from distutils.core import setup
from setuptools import find_packages

setup(name='pytableparse',
      version='0.1',
      description='Search table values by keys',
      author='Potapov Konstantin',
      author_email='phpconf@gmail.com',
      packages=find_packages(),
      install_requires=['pyquery', 'six'],
      test_suite="nose.collector"


      )

