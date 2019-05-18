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

import re

# python 2 and python 3 compatibility library
import six

from esperclient.api_client import ApiClient


class GroupCommandsApi(object):
    """NOTE: This class is auto generated.

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_group_command(self, command_id, group_id, enterprise_id, **kwargs):
        """Get group command status

        Returns GroupCommand instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_command(command_id, group_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: A UUID string identifying this device command. (required)
        :param str group_id: A UUID string identifying this group. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: GroupCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_command_with_http_info(command_id, group_id, enterprise_id, **kwargs)
        else:
            (data) = self.get_group_command_with_http_info(command_id, group_id, enterprise_id, **kwargs)
            return data

    def get_group_command_with_http_info(self, command_id, group_id, enterprise_id, **kwargs):
        """Get group command status

        Returns GroupCommand instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_command_with_http_info(command_id, group_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: A UUID string identifying this device command. (required)
        :param str group_id: A UUID string identifying this group. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: GroupCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id', 'group_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params or
                params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `get_group_command`")
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_group_command`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_group_command`")

        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['command_id'] = params['command_id']
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']
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
            '/enterprise/{enterprise_id}/devicegroup/{group_id}/command/{command_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupCommand',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def run_group_command(self, enterprise_id, group_id, data, **kwargs):
        """Run commands on group devices

        Fire commands on all the group devices
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.run_group_command(enterprise_id, group_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :param str group_id: ID of the group (required)
        :param GroupCommandRequest data: Group command request (required)
        :return: GroupCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.run_group_command_with_http_info(enterprise_id, group_id, data, **kwargs)
        else:
            (data) = self.run_group_command_with_http_info(enterprise_id, group_id, data, **kwargs)
            return data

    def run_group_command_with_http_info(self, enterprise_id, group_id, data, **kwargs):
        """Run commands on group devices

        Fire commands on all the group devices
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.run_group_command_with_http_info(enterprise_id, group_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :param str group_id: ID of the group (required)
        :param GroupCommandRequest data: Group command request (required)
        :return: GroupCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'group_id', 'data']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method run_group_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `run_group_command`")
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `run_group_command`")
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `run_group_command`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']

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
            '/enterprise/{enterprise_id}/devicegroup/{group_id}/command/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupCommand',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
