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


class DeviceGroupApi(object):
    """NOTE: This class is auto generated.

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_group(self, enterprise_id, data, **kwargs):
        """Create a device group

        Returns EnterpriseDeviceGroup instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_group(enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param DeviceGroupUpdate data: (required)
        :return: DeviceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_group_with_http_info(enterprise_id, data, **kwargs)
        else:
            (data) = self.create_group_with_http_info(enterprise_id, data, **kwargs)
            return data

    def create_group_with_http_info(self, enterprise_id, data, **kwargs):
        """Create a device group

        Returns EnterpriseDeviceGroup instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_group_with_http_info(enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param DeviceGroupUpdate data: (required)
        :return: DeviceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'data']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `create_group`")
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `create_group`")

        collection_formats = {}

        path_params = {}
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
            '/enterprise/{enterprise_id}/devicegroup/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceGroup',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_group(self, group_id, enterprise_id, **kwargs):
        """Delete a device group

        Emtpy response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_group(group_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: A UUID string identifying this enterprise device group. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_group_with_http_info(group_id, enterprise_id, **kwargs)
        else:
            (data) = self.delete_group_with_http_info(group_id, enterprise_id, **kwargs)
            return data

    def delete_group_with_http_info(self, group_id, enterprise_id, **kwargs):
        """Delete a device group

        Emtpy response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_group_with_http_info(group_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: A UUID string identifying this enterprise device group. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `delete_group`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `delete_group`")

        collection_formats = {}

        path_params = {}
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
            '/enterprise/{enterprise_id}/devicegroup/{group_id}/', 'DELETE',
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

    def get_all_groups(self, enterprise_id, **kwargs):
        """List device groups

        Returns EnterpriseDeviceGroup list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_groups(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param str name: Filter by group name
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_groups_with_http_info(enterprise_id, **kwargs)
        else:
            (data) = self.get_all_groups_with_http_info(enterprise_id, **kwargs)
            return data

    def get_all_groups_with_http_info(self, enterprise_id, **kwargs):
        """List device groups

        Returns EnterpriseDeviceGroup list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_groups_with_http_info(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param str name: Filter by group name
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'name', 'limit', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_all_groups`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))
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
            '/enterprise/{enterprise_id}/devicegroup/', 'GET',
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

    def get_group_by_id(self, group_id, enterprise_id, **kwargs):
        """Get device group information

        Returns EnterpriseDeviceGroup instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_by_id(group_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: A UUID string identifying this enterprise device group. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: DeviceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_by_id_with_http_info(group_id, enterprise_id, **kwargs)
        else:
            (data) = self.get_group_by_id_with_http_info(group_id, enterprise_id, **kwargs)
            return data

    def get_group_by_id_with_http_info(self, group_id, enterprise_id, **kwargs):
        """Get device group information

        Returns EnterpriseDeviceGroup instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_by_id_with_http_info(group_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: A UUID string identifying this enterprise device group. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: DeviceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_group_by_id`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_group_by_id`")

        collection_formats = {}

        path_params = {}
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
            '/enterprise/{enterprise_id}/devicegroup/{group_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceGroup',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def partial_update_group(self, group_id, enterprise_id, data, **kwargs):
        """Partial update group

        Returns EnterpriseDeviceGroup instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_group(group_id, enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: A UUID string identifying this enterprise device group. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param DeviceGroupPartialUpdate data: (required)
        :param str action: add / remove / rename / move
        :return: DeviceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.partial_update_group_with_http_info(group_id, enterprise_id, data, **kwargs)
        else:
            (data) = self.partial_update_group_with_http_info(group_id, enterprise_id, data, **kwargs)
            return data

    def partial_update_group_with_http_info(self, group_id, enterprise_id, data, **kwargs):
        """Partial update group

        Returns EnterpriseDeviceGroup instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_group_with_http_info(group_id, enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: A UUID string identifying this enterprise device group. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param DeviceGroupPartialUpdate data: (required)
        :param str action: add / remove / rename / move
        :return: DeviceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'enterprise_id', 'data', 'action']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method partial_update_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `partial_update_group`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `partial_update_group`")
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `partial_update_group`")

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

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
            '/enterprise/{enterprise_id}/devicegroup/{group_id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceGroup',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_group(self, group_id, enterprise_id, data, **kwargs):
        """Update device group

        Returns EnterpriseDeviceGroup instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group(group_id, enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: A UUID string identifying this enterprise device group. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param DeviceGroupUpdate data: (required)
        :param str action: add / remove / rename / move
        :return: DeviceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_group_with_http_info(group_id, enterprise_id, data, **kwargs)
        else:
            (data) = self.update_group_with_http_info(group_id, enterprise_id, data, **kwargs)
            return data

    def update_group_with_http_info(self, group_id, enterprise_id, data, **kwargs):
        """Update device group

        Returns EnterpriseDeviceGroup instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_group_with_http_info(group_id, enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: A UUID string identifying this enterprise device group. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param DeviceGroupUpdate data: (required)
        :param str action: add / remove / rename / move
        :return: DeviceGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'enterprise_id', 'data', 'action']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `update_group`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `update_group`")
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `update_group`")

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

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
            '/enterprise/{enterprise_id}/devicegroup/{group_id}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceGroup',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
