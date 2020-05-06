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
from esperclient.api.commands_v2_api import CommandsV2Api
from esperclient.rest import ApiException


class TestCommandsV2Api(unittest.TestCase):
    """CommandsV2Api unit test stubs"""

    def setUp(self):
        self.api = esperclient.api.commands_v2_api.CommandsV2Api()

    def tearDown(self):
        pass

    def test_create_command(self):
        """Test case for create_command

        Create a command request
        """
        pass

    def test_get_command_request_status(self):
        """Test case for get_command_request_status

        get status list for command request
        """
        pass

    def test_get_device_command_history(self):
        """Test case for get_device_command_history

        get command history for device
        """
        pass

    def test_list_command_request(self):
        """Test case for list_command_request

        List command requests
        """
        pass

    def test_partial_update_command_status(self):
        """Test case for partial_update_command_status

        Update command status
        """
        pass


if __name__ == '__main__':
    unittest.main()
