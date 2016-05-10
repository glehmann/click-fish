#!/usr/bin/env python

import ast
import re

from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('click_fish.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='click-fish',
    version=version,
    description='Fish completion for Click',
    author='Gaëtan Lehmann',
    author_email='gaetan.lehmann@gmail.com',
    url='https://github.com/glehmann/click-fish',
    license='MIT',
    long_description=open('README.md').read(),
    py_modules=['click_fish'],
    install_requires=[
        'click',
    ],
)
