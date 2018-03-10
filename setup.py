#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = 'Jason Koh'
__version__ = '0.0.1'

setup(
    name = 'jasonhelper',
    version = __version__,
    packages = ['jasonhelper'],
    package_dir = {'jasonhelper': 'jasonhelper'},
    author = __author__,
    description = 'This helps Jason. Maybe you too.',
    zip_safe = False,
    install_requires = ['setuptools'],
    include_package_data = True,
    classifiers = (
        'Development Status:: 1 - Planning',
        'Intended Audience :: Developers'
    )
)
