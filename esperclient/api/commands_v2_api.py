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


class CommandsV2Api(object):
    """NOTE: This class is auto generated.

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_command(self, enterprise_id, request, **kwargs):
        """Create a command request

        API to create a command request for the device.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_command(enterprise_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :param V0CommandRequest request: The request body to create a command for set of devices or groups (required)
        :return: V0CommandRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_command_with_http_info(enterprise_id, request, **kwargs)
        else:
            (data) = self.create_command_with_http_info(enterprise_id, request, **kwargs)
            return data

    def create_command_with_http_info(self, enterprise_id, request, **kwargs):
        """Create a command request

        API to create a command request for the device.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_command_with_http_info(enterprise_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :param V0CommandRequest request: The request body to create a command for set of devices or groups (required)
        :return: V0CommandRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `create_command`")
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `create_command`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api(
            '/v0/enterprise/{enterprise_id}/command/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V0CommandRequest',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_command_request_status(self, enterprise_id, request_id, **kwargs):
        """get status list for command request

        API to get and filter command request status
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_command_request_status(enterprise_id, request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :param str request_id: ID for the command request (required)
        :param str device: Filter status result by device id.
        :param str state: Filter by command state
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_command_request_status_with_http_info(enterprise_id, request_id, **kwargs)
        else:
            (data) = self.get_command_request_status_with_http_info(enterprise_id, request_id, **kwargs)
            return data

    def get_command_request_status_with_http_info(self, enterprise_id, request_id, **kwargs):
        """get status list for command request

        API to get and filter command request status
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_command_request_status_with_http_info(enterprise_id, request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :param str request_id: ID for the command request (required)
        :param str device: Filter status result by device id.
        :param str state: Filter by command state
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'request_id', 'device', 'state']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_command_request_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_command_request_status`")
        # verify the required parameter 'request_id' is set
        if ('request_id' not in params or
                params['request_id'] is None):
            raise ValueError("Missing the required parameter `request_id` when calling `get_command_request_status`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']
        if 'request_id' in params:
            path_params['request_id'] = params['request_id']

        query_params = []
        if 'device' in params:
            query_params.append(('device', params['device']))
        if 'state' in params:
            query_params.append(('state', params['state']))

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
            '/v0/enterprise/{enterprise_id}/command/{request_id}/status/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2008',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_device_command_history(self, enterprise_id, device_id, **kwargs):
        """get command history for device

        API to get and filter deivce command history
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_command_history(enterprise_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: Id of the enterprise (required)
        :param str device_id: Id for the command request (required)
        :param str state: Filter by command state
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_device_command_history_with_http_info(enterprise_id, device_id, **kwargs)
        else:
            (data) = self.get_device_command_history_with_http_info(enterprise_id, device_id, **kwargs)
            return data

    def get_device_command_history_with_http_info(self, enterprise_id, device_id, **kwargs):
        """get command history for device

        API to get and filter deivce command history
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_command_history_with_http_info(enterprise_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: Id of the enterprise (required)
        :param str device_id: Id for the command request (required)
        :param str state: Filter by command state
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'device_id', 'state']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_command_history" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_device_command_history`")
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `get_device_command_history`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']

        query_params = []
        if 'state' in params:
            query_params.append(('state', params['state']))

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
            '/v0/enterprise/{enterprise_id}/device/{device_id}/command-history/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2008',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_command_request(self, enterprise_id, **kwargs):
        """List command requests

        API to get and filter command requests
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_command_request(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :param str command_type: Filter by type of command request i.e device, group etc
        :param str devices: Filter by device IDs. Accepts comma separated values.
        :param str device_type: Filter by device type i.e active, inactive etc
        :param str command: Filter by command name
        :param str issued_by: Filter by user. Accepts user id.
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_command_request_with_http_info(enterprise_id, **kwargs)
        else:
            (data) = self.list_command_request_with_http_info(enterprise_id, **kwargs)
            return data

    def list_command_request_with_http_info(self, enterprise_id, **kwargs):
        """List command requests

        API to get and filter command requests
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_command_request_with_http_info(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :param str command_type: Filter by type of command request i.e device, group etc
        :param str devices: Filter by device IDs. Accepts comma separated values.
        :param str device_type: Filter by device type i.e active, inactive etc
        :param str command: Filter by command name
        :param str issued_by: Filter by user. Accepts user id.
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'command_type', 'devices', 'device_type', 'command', 'issued_by']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_command_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `list_command_request`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = []
        if 'command_type' in params:
            query_params.append(('command_type', params['command_type']))
        if 'devices' in params:
            query_params.append(('devices', params['devices']))
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))
        if 'command' in params:
            query_params.append(('command', params['command']))
        if 'issued_by' in params:
            query_params.append(('issued_by', params['issued_by']))

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
            '/v0/enterprise/{enterprise_id}/command/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2007',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def partial_update_command_status(self, enterprise_id, request_id, command_id, action, **kwargs):
        """Update command status

        API to patch the state of command
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_command_status(enterprise_id, request_id, command_id, action, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :param str request_id: ID for the command request (required)
        :param str command_id: ID for the command (required)
        :param str action: Action to be performed on device (required)
        :param V0CommandStatusUpdate data:
        :return: V0CommandStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.partial_update_command_status_with_http_info(enterprise_id, request_id, command_id, action, **kwargs)
        else:
            (data) = self.partial_update_command_status_with_http_info(enterprise_id, request_id, command_id, action, **kwargs)
            return data

    def partial_update_command_status_with_http_info(self, enterprise_id, request_id, command_id, action, **kwargs):
        """Update command status

        API to patch the state of command
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_command_status_with_http_info(enterprise_id, request_id, command_id, action, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :param str request_id: ID for the command request (required)
        :param str command_id: ID for the command (required)
        :param str action: Action to be performed on device (required)
        :param V0CommandStatusUpdate data:
        :return: V0CommandStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'request_id', 'command_id', 'action', 'data']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method partial_update_command_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `partial_update_command_status`")
        # verify the required parameter 'request_id' is set
        if ('request_id' not in params or
                params['request_id'] is None):
            raise ValueError("Missing the required parameter `request_id` when calling `partial_update_command_status`")
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params or
                params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `partial_update_command_status`")
        # verify the required parameter 'action' is set
        if ('action' not in params or
                params['action'] is None):
            raise ValueError("Missing the required parameter `action` when calling `partial_update_command_status`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']
        if 'request_id' in params:
            path_params['request_id'] = params['request_id']
        if 'command_id' in params:
            path_params['command_id'] = params['command_id']

        query_params = []
        if 'action' in params:
            query_params.append(('action', params['action']))

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
            '/v0/enterprise/{enterprise_id}/command/{request_id}/status/{command_id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V0CommandStatus',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
