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
from esperclient.api.content_api import ContentApi
from esperclient.rest import ApiException


class TestContentApi(unittest.TestCase):
    """ContentApi unit test stubs"""

    def setUp(self):
        self.api = esperclient.api.content_api.ContentApi()

    def tearDown(self):
        pass

    def test_delete_content(self):
        """Test case for delete_content

        Delete Content
        """
        pass

    def test_get_all_content(self):
        """Test case for get_all_content

        List content in the enterprise
        """
        pass

    def test_get_content(self):
        """Test case for get_content

        Get content information
        """
        pass

    def test_patch_content(self):
        """Test case for patch_content

        Patch a content instance
        """
        pass

    def test_post_content(self):
        """Test case for post_content

        Upload new content
        """
        pass


if __name__ == '__main__':
    unittest.main()
