#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Copyright Bernardo Heynemann <heynemann@gmail.com>

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(
    name = 'Peon',
    version = "0.2.1",
    description = "Peon is an auto-testing-like tool",
    long_description = """Peon works for you while you are developing.""",
    keywords = 'Testing Notify',
    author = 'Bernardo Heynemann',
    author_email = 'heynemann@gmail.com',
    url = 'http://www.nonesofar.org',
    license = 'OSI',
    classifiers = ['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Natural Language :: English',
                   'Operating System :: MacOS',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Topic :: Software Development :: Quality Assurance',
                   'Topic :: Software Development :: Testing',],
    packages=["peon",],
    include_package_data=True,
    package_data = {
        '': ['*.png'],
    },
    install_requires=[
    ],

    entry_points = {
        'console_scripts': [
            'peon = peon.peon:main',
        ],
    },

)


