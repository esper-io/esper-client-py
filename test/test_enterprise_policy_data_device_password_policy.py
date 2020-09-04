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
from esperclient.models.enterprise_policy_data_device_password_policy import EnterprisePolicyDataDevicePasswordPolicy
from esperclient.rest import ApiException


class TestEnterprisePolicyDataDevicePasswordPolicy(unittest.TestCase):
    """EnterprisePolicyDataDevicePasswordPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnterprisePolicyDataDevicePasswordPolicy(self):
        """Test EnterprisePolicyDataDevicePasswordPolicy"""
        model = esperclient.models.enterprise_policy_data_device_password_policy.EnterprisePolicyDataDevicePasswordPolicy()
        pass


if __name__ == '__main__':
    unittest.main()
