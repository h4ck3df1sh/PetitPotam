#!/usr/bin/env python
from setuptools import setup

setup(
    name='PetitPotam',
    version='1.0.0',
    description='PoC to elicit machine account authentication via MS-EFSRPC functions',
    author='GILLES Lionel aka topotam',
    scripts=['PetitPotam.py'],
    install_requires=[
        'impacket',
    ],
    python_requires='>=3.6',
)
