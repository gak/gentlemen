#!/usr/bin/env python

from setuptools import setup

setup(
    name='Gentlemen',
    version='1.0',
    description='This is gentlemen',
    author='Gerald Kaszuba',
    author_email='gak@gak0.com',
    packages=['gentlemen'],
    entry_points={
        'console_scripts': [
            'gentlemen = gentlemen:main',
        ]
    }
)
