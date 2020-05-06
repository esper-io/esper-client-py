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
from esperclient.api.device_group_api import DeviceGroupApi
from esperclient.rest import ApiException


class TestDeviceGroupApi(unittest.TestCase):
    """DeviceGroupApi unit test stubs"""

    def setUp(self):
        self.api = esperclient.api.device_group_api.DeviceGroupApi()

    def tearDown(self):
        pass

    def test_create_group(self):
        """Test case for create_group

        Create a device group
        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        Delete a device group
        """
        pass

    def test_get_all_groups(self):
        """Test case for get_all_groups

        List device groups
        """
        pass

    def test_get_group_by_id(self):
        """Test case for get_group_by_id

        Get device group information
        """
        pass

    def test_partial_update_group(self):
        """Test case for partial_update_group

        Partial update group
        """
        pass

    def test_update_group(self):
        """Test case for update_group

        Update device group
        """
        pass


if __name__ == '__main__':
    unittest.main()
