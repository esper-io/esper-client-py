# coding: utf-8

"""
ESPER API REFERENCE

OpenAPI spec version: 1.0.0
Contact: developer@esper.io
---------------------------------------------------------

Copyright 2019 Shoonya Enterprises Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""



from setuptools import setup, find_packages

NAME = "esperclient"
VERSION = "0.1.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="ESPER API REFERENCE",
    author_email="developer@esper.io",
    url="",
    keywords=["Python SDK", "ESPER API REFERENCE"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Esper SDK for Python

    Python client library for Esper Manage APIs. You can find out more about Esper at https://esper.io.

    - API version: 1.0.0
    - Package version: 0.1.1

    For usage instructions and API documentation please visit: https://github.com/esper-io/esper-client-py

    """,
    long_description_content_type='text/markdown'
)
