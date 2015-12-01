#!/usr/bin/env python
#
# Copyright 2014 (c) clairvoyant
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''The setup and build script for a python project.'''

import os

from setuptools import setup, find_packages

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='python-MODIFY-PROJECT-NAME',
    version='2.1',
    author='MODIFY-DEVELOPER-NAME',
    author_email='MODIFY@ORGANIZATION.COM',
    license='Apache License 2.0',
    url='https://MODIFY-PROJECT-GIT-URL',
    keywords='PROYECT-KEY-WORDS',
    description='An example project to be use as a starting point.',
    long_description=(read('README.rst') + '\n\n' +
                      read('AUTHORS.rst') + '\n\n' +
                      read('CHANGES')),
    packages=find_packages(exclude=['tests*']),
    install_requires = ['requests', 'requests-oauthlib'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
