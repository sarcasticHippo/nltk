#!/usr/bin/env python
#
# Distribute setup script for the Natural Language Toolkit
#
# Copyright (C) 2001-2013 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gradient.cis.upenn.edu>
#         Ewan Klein <ewan@inf.ed.ac.uk>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# python2.5 compatibility
from __future__ import with_statement

# Work around mbcs bug in distutils. 
# http://bugs.python.org/issue10945
import codecs 
try: 
    codecs.lookup('mbcs') 
except LookupError: 
    ascii = codecs.lookup('ascii') 
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs') 
    codecs.register(func) 

import os

# Use the VERSION file to get NLTK version
version_file = os.path.join(os.path.dirname(__file__), 'nltk', 'VERSION')
with open(version_file) as fh:
    nltk_version = fh.read().strip()

import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

#
# Prevent setuptools from trying to add extra files to the source code
# manifest by scanning the version control system for its contents.
#
from setuptools.command import sdist
del sdist.finders[:]

setup(
    name = "nltk",
    description = "Natural Language Toolkit",
    version = nltk_version,
    url = "http://nltk.org/",
    long_description = """\
The Natural Language Toolkit (NLTK) is a Python package for
natural language processing.  NLTK requires Python 2.5 or higher.""",
    license = "Apache License, Version 2.0",
    keywords = ['NLP', 'CL', 'natural language processing',
                'computational linguistics', 'parsing', 'tagging',
                'tokenizing', 'syntax', 'linguistics', 'language',
                'natural language', 'text analytics'],
    maintainer = "Steven Bird",
    maintainer_email = "stevenbird1@gmail.com",
    author = "Steven Bird",
    author_email = "stevenbird1@gmail.com",
    classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Text Processing',
    'Topic :: Text Processing :: Filters',
    'Topic :: Text Processing :: General',
    'Topic :: Text Processing :: Indexing',
    'Topic :: Text Processing :: Linguistic',
    ],
    package_data = {'nltk': ['nltk.jar', 'test/*.doctest', 'VERSION']},
    packages = find_packages(),
    zip_safe=False, # since normal files will be present too?
    install_requires=['PyYAML>=3.09'],
    )
