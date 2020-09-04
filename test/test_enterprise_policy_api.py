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



from __future__ import absolute_import

import unittest

import esperclient
from esperclient.api.enterprise_policy_api import EnterprisePolicyApi
from esperclient.rest import ApiException


class TestEnterprisePolicyApi(unittest.TestCase):
    """EnterprisePolicyApi unit test stubs"""

    def setUp(self):
        self.api = esperclient.api.enterprise_policy_api.EnterprisePolicyApi()

    def tearDown(self):
        pass

    def test_create_policy(self):
        """Test case for create_policy

        Create a new Enterprise Policy
        """
        pass

    def test_delete_enterprise_policy(self):
        """Test case for delete_enterprise_policy

        Delete a Enterprise Policy
        """
        pass

    def test_get_policy_by_id(self):
        """Test case for get_policy_by_id

        Get Enterprise Policy
        """
        pass

    def test_list_policies(self):
        """Test case for list_policies

        List all policies in enterprise
        """
        pass

    def test_partialupdate_policy(self):
        """Test case for partialupdate_policy

        Partial update EnterprisePolicy
        """
        pass

    def test_update_policy(self):
        """Test case for update_policy

        Update Enterprise Policy
        """
        pass


if __name__ == '__main__':
    unittest.main()
