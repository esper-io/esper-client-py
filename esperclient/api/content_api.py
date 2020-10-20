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

import re

# python 2 and python 3 compatibility library
import six

from esperclient.api_client import ApiClient


class ContentApi(object):
    """NOTE: This class is auto generated.

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_content(self, content_id, enterprise_id, **kwargs):
        """Delete Content

        Empty response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_content(content_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_id: A UUID string identifying a content instance. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_content_with_http_info(content_id, enterprise_id, **kwargs)
        else:
            (data) = self.delete_content_with_http_info(content_id, enterprise_id, **kwargs)
            return data

    def delete_content_with_http_info(self, content_id, enterprise_id, **kwargs):
        """Delete Content

        Empty response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_content_with_http_info(content_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_id: A UUID string identifying a content instance. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_id' is set
        if ('content_id' not in params or
                params['content_id'] is None):
            raise ValueError("Missing the required parameter `content_id` when calling `delete_content`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `delete_content`")

        collection_formats = {}

        path_params = {}
        if 'content_id' in params:
            path_params['content_id'] = params['content_id']
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api(
            '/v0/enterprise/{enterprise_id}/content/{content_id}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_content(self, enterprise_id, **kwargs):
        """List content in the enterprise

        Returns Content list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_content(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param str search: Seach by tags, description
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_content_with_http_info(enterprise_id, **kwargs)
        else:
            (data) = self.get_all_content_with_http_info(enterprise_id, **kwargs)
            return data

    def get_all_content_with_http_info(self, enterprise_id, **kwargs):
        """List content in the enterprise

        Returns Content list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_content_with_http_info(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param str search: Seach by tags, description
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'search', 'limit', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_all_content`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api(
            '/v0/enterprise/{enterprise_id}/content/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20011',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_content(self, content_id, enterprise_id, **kwargs):
        """Get content information

        Returns Content instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content(content_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_id: A UUID string identifying a content instance. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: Content
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_content_with_http_info(content_id, enterprise_id, **kwargs)
        else:
            (data) = self.get_content_with_http_info(content_id, enterprise_id, **kwargs)
            return data

    def get_content_with_http_info(self, content_id, enterprise_id, **kwargs):
        """Get content information

        Returns Content instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_with_http_info(content_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_id: A UUID string identifying a content instance. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: Content
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_id' is set
        if ('content_id' not in params or
                params['content_id'] is None):
            raise ValueError("Missing the required parameter `content_id` when calling `get_content`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_content`")

        collection_formats = {}

        path_params = {}
        if 'content_id' in params:
            path_params['content_id'] = params['content_id']
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api(
            '/v0/enterprise/{enterprise_id}/content/{content_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Content',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_content(self, content_id, enterprise_id, **kwargs):
        """Patch a content instance

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_content(content_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_id: A UUID string identifying a content instance. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param Data data:
        :return: Content
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_content_with_http_info(content_id, enterprise_id, **kwargs)
        else:
            (data) = self.patch_content_with_http_info(content_id, enterprise_id, **kwargs)
            return data

    def patch_content_with_http_info(self, content_id, enterprise_id, **kwargs):
        """Patch a content instance

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_content_with_http_info(content_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_id: A UUID string identifying a content instance. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param Data data:
        :return: Content
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_id', 'enterprise_id', 'data']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_id' is set
        if ('content_id' not in params or
                params['content_id'] is None):
            raise ValueError("Missing the required parameter `content_id` when calling `patch_content`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `patch_content`")

        collection_formats = {}

        path_params = {}
        if 'content_id' in params:
            path_params['content_id'] = params['content_id']
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api(
            '/v0/enterprise/{enterprise_id}/content/{content_id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Content',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_content(self, enterprise_id, app_file, **kwargs):
        """Upload new content

        Returns Content instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_content(enterprise_id, app_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param file app_file: Valid file to upload (required)
        :return: Content
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_content_with_http_info(enterprise_id, app_file, **kwargs)
        else:
            (data) = self.post_content_with_http_info(enterprise_id, app_file, **kwargs)
            return data

    def post_content_with_http_info(self, enterprise_id, app_file, **kwargs):
        """Upload new content

        Returns Content instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_content_with_http_info(enterprise_id, app_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param file app_file: Valid file to upload (required)
        :return: Content
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'app_file']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `post_content`")
        # verify the required parameter 'app_file' is set
        if ('app_file' not in params or
                params['app_file'] is None):
            raise ValueError("Missing the required parameter `app_file` when calling `post_content`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'app_file' in params:
            local_var_files['app_file'] = params['app_file']

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['multipart/form-data'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api(
            '/v0/enterprise/{enterprise_id}/content/upload/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Content',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
