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
from esperclient.api.device_api import DeviceApi
from esperclient.rest import ApiException


class TestDeviceApi(unittest.TestCase):
    """DeviceApi unit test stubs"""

    def setUp(self):
        self.api = esperclient.api.device_api.DeviceApi()

    def tearDown(self):
        pass

    def test_get_all_devices(self):
        """Test case for get_all_devices

        Fetch all devices in an enterprise
        """
        pass

    def test_get_app_installs(self):
        """Test case for get_app_installs

        List installed apps
        """
        pass

    def test_get_device_app_by_id(self):
        """Test case for get_device_app_by_id

        Get device app details
        """
        pass

    def test_get_device_apps(self):
        """Test case for get_device_apps

        List all device apps
        """
        pass

    def test_get_device_by_id(self):
        """Test case for get_device_by_id

        Fetch device details by ID
        """
        pass

    def test_get_device_event(self):
        """Test case for get_device_event

        Get latest device event
        """
        pass


if __name__ == '__main__':
    unittest.main()
