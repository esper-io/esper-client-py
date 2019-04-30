# coding: utf-8

"""
Esper Manage API

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
from esperclient.api.enterprise_api import EnterpriseApi
from esperclient.rest import ApiException


class TestEnterpriseApi(unittest.TestCase):
    """EnterpriseApi unit test stubs"""

    def setUp(self):
        self.api = esperclient.api.enterprise_api.EnterpriseApi()

    def tearDown(self):
        pass

    def test_get_all_enterprises(self):
        """Test case for get_all_enterprises

        List all enterprises
        """
        pass

    def test_get_enterprise(self):
        """Test case for get_enterprise

        Get your enteprise information
        """
        pass

    def test_partial_update_enterprise(self):
        """Test case for partial_update_enterprise

        Partial update enterprise information
        """
        pass


if __name__ == '__main__':
    unittest.main()
