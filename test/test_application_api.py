# coding: utf-8

"""
Esper APIs

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



from __future__ import absolute_import

import unittest

import esperclient
from esperclient.api.application_api import ApplicationApi
from esperclient.rest import ApiException


class TestApplicationApi(unittest.TestCase):
    """ApplicationApi unit test stubs"""

    def setUp(self):
        self.api = esperclient.api.application_api.ApplicationApi()

    def tearDown(self):
        pass

    def test_delete_app_version(self):
        """Test case for delete_app_version

        Delete app version
        """
        pass

    def test_delete_application(self):
        """Test case for delete_application

        Delete an application
        """
        pass

    def test_get_all_applications(self):
        """Test case for get_all_applications

        List apps in enterprise
        """
        pass

    def test_get_app_version(self):
        """Test case for get_app_version

        Get app version information
        """
        pass

    def test_get_app_versions(self):
        """Test case for get_app_versions

        List App versions
        """
        pass

    def test_get_application(self):
        """Test case for get_application

        Get application information
        """
        pass

    def test_upload(self):
        """Test case for upload

        upload an application to enterprise
        """
        pass


if __name__ == '__main__':
    unittest.main()
