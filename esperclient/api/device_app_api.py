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

import re

# python 2 and python 3 compatibility library
import six

from esperclient.api_client import ApiClient


class DeviceAppApi(object):
    """NOTE: This class is auto generated.

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_device_app_by_id(self, app_id, enterprise_id, device_id, **kwargs):
        """Get app information

        Returns DeviceApp instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_app_by_id(app_id, enterprise_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_id: A UUID string identifying this device app. (required)
        :param str enterprise_id: A UUID string identifying this device. (required)
        :param str device_id: A UUID string identifying this enteprise. (required)
        :return: DeviceApp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_device_app_by_id_with_http_info(app_id, enterprise_id, device_id, **kwargs)
        else:
            (data) = self.get_device_app_by_id_with_http_info(app_id, enterprise_id, device_id, **kwargs)
            return data

    def get_device_app_by_id_with_http_info(self, app_id, enterprise_id, device_id, **kwargs):
        """Get app information

        Returns DeviceApp instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_app_by_id_with_http_info(app_id, enterprise_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_id: A UUID string identifying this device app. (required)
        :param str enterprise_id: A UUID string identifying this device. (required)
        :param str device_id: A UUID string identifying this enteprise. (required)
        :return: DeviceApp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'enterprise_id', 'device_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_app_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params or
                params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `get_device_app_by_id`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_device_app_by_id`")
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `get_device_app_by_id`")

        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['app_id'] = params['app_id']
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']

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
            '/enterprise/{enterprise_id}/device/{device_id}/app/{app_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceApp',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_device_apps(self, enterprise_id, device_id, **kwargs):
        """List all device apps

        Returns DeviceApp list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_apps(enterprise_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param str device_id: A UUID string identifying device. (required)
        :param str package_name: package name contains filter
        :param str whitelisted: Whitelist filter
        :param str search: A search term. Search by app_name.
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_device_apps_with_http_info(enterprise_id, device_id, **kwargs)
        else:
            (data) = self.get_device_apps_with_http_info(enterprise_id, device_id, **kwargs)
            return data

    def get_device_apps_with_http_info(self, enterprise_id, device_id, **kwargs):
        """List all device apps

        Returns DeviceApp list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_apps_with_http_info(enterprise_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param str device_id: A UUID string identifying device. (required)
        :param str package_name: package name contains filter
        :param str whitelisted: Whitelist filter
        :param str search: A search term. Search by app_name.
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'device_id', 'package_name', 'whitelisted', 'search', 'limit', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_apps" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_device_apps`")
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `get_device_apps`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']

        query_params = []
        if 'package_name' in params:
            query_params.append(('package_name', params['package_name']))
        if 'whitelisted' in params:
            query_params.append(('whitelisted', params['whitelisted']))
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
            '/enterprise/{enterprise_id}/device/{device_id}/app/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
