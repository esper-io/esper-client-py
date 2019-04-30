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
from esperclient.api.policy_api import PolicyApi
from esperclient.rest import ApiException


class TestPolicyApi(unittest.TestCase):
    """PolicyApi unit test stubs"""

    def setUp(self):
        self.api = esperclient.api.policy_api.PolicyApi()

    def tearDown(self):
        pass

    def test_create_policy(self):
        """Test case for create_policy

        Create a policy
        """
        pass

    def test_delete_policy(self):
        """Test case for delete_policy

        Delete a policy
        """
        pass

    def test_get_all_policies(self):
        """Test case for get_all_policies

        List enterprise policies
        """
        pass

    def test_get_policy_by_id(self):
        """Test case for get_policy_by_id

        Get policy details
        """
        pass

    def test_partial_update_policy(self):
        """Test case for partial_update_policy

        Partial update policy
        """
        pass

    def test_update_policy(self):
        """Test case for update_policy

        Update/Replace information
        """
        pass


if __name__ == '__main__':
    unittest.main()
