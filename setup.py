#!/usr/bin/env python
from setuptools import setup

setup(
    name='PetitPotam',
    version='1.0.0',
    description='PoC to elicit machine account authentication via MS-EFSRPC functions',
    author='GILLES Lionel aka topotam',
    py_modules=['PetitPotam'],
    install_requires=[
        'impacket',
    ],
    entry_points={
        'console_scripts': [
            'PetitPotam.py=PetitPotam:main',
        ],
    },
    python_requires='>=3.6',
)
