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
from esperclient.api.geofence_api import GeofenceApi
from esperclient.rest import ApiException


class TestGeofenceApi(unittest.TestCase):
    """GeofenceApi unit test stubs"""

    def setUp(self):
        self.api = esperclient.api.geofence_api.GeofenceApi()

    def tearDown(self):
        pass

    def test_create_geofence(self):
        """Test case for create_geofence

        Create a geofence
        """
        pass

    def test_delete_geofence(self):
        """Test case for delete_geofence

        Delete a geofence
        """
        pass

    def test_get_all_geofences(self):
        """Test case for get_all_geofences

        List Geofences in Enterprise
        """
        pass

    def test_get_geofence(self):
        """Test case for get_geofence

        Get geofence information
        """
        pass

    def test_partial_update_geofence(self):
        """Test case for partial_update_geofence

        Partially updates geofence information
        """
        pass

    def test_update_geofence(self):
        """Test case for update_geofence

        Update geofence information
        """
        pass


if __name__ == '__main__':
    unittest.main()
