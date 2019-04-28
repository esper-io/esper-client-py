# coding: utf-8

"""
Esper Manage API

OpenAPI spec version: 1.0.0
Contact: developer@esper.io
---------------------------------------------------------

Copyright 2019 Esper, Inc.

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


class PolicyApi(object):
    """NOTE: This class is auto generated.

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_policy(self, enterprise_id, data, **kwargs):
        """Create a policy

        Return EnterprisePolicy instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_policy(enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param EnterprisePolicy data: (required)
        :return: EnterprisePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_policy_with_http_info(enterprise_id, data, **kwargs)
        else:
            (data) = self.create_policy_with_http_info(enterprise_id, data, **kwargs)
            return data

    def create_policy_with_http_info(self, enterprise_id, data, **kwargs):
        """Create a policy

        Return EnterprisePolicy instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_policy_with_http_info(enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param EnterprisePolicy data: (required)
        :return: EnterprisePolicy
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
                    " to method create_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `create_policy`")
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `create_policy`")

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
            '/enterprise/{enterprise_id}/policy/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EnterprisePolicy',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_policy(self, policy_id, enterprise_id, **kwargs):
        """Delete a policy

        Empty response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_policy(policy_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: A unique integer value identifying this enterprise policy. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_policy_with_http_info(policy_id, enterprise_id, **kwargs)
        else:
            (data) = self.delete_policy_with_http_info(policy_id, enterprise_id, **kwargs)
            return data

    def delete_policy_with_http_info(self, policy_id, enterprise_id, **kwargs):
        """Delete a policy

        Empty response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_policy_with_http_info(policy_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: A unique integer value identifying this enterprise policy. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `delete_policy`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `delete_policy`")

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policy_id'] = params['policy_id']
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
            '/enterprise/{enterprise_id}/policy/{policy_id}/', 'DELETE',
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

    def get_all_policies(self, enterprise_id, **kwargs):
        """List enterprise policies

        Returns EnterprisePolicy list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_policies(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param str name: filter by name (starts with)
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_policies_with_http_info(enterprise_id, **kwargs)
        else:
            (data) = self.get_all_policies_with_http_info(enterprise_id, **kwargs)
            return data

    def get_all_policies_with_http_info(self, enterprise_id, **kwargs):
        """List enterprise policies

        Returns EnterprisePolicy list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_policies_with_http_info(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param str name: filter by name (starts with)
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2008
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
                    " to method get_all_policies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_all_policies`")

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
            '/enterprise/{enterprise_id}/policy/', 'GET',
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

    def get_policy_by_id(self, policy_id, enterprise_id, **kwargs):
        """Get policy details

        Returns EnterprisePolicy instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy_by_id(policy_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: A unique integer value identifying this enterprise policy. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: EnterprisePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_policy_by_id_with_http_info(policy_id, enterprise_id, **kwargs)
        else:
            (data) = self.get_policy_by_id_with_http_info(policy_id, enterprise_id, **kwargs)
            return data

    def get_policy_by_id_with_http_info(self, policy_id, enterprise_id, **kwargs):
        """Get policy details

        Returns EnterprisePolicy instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_policy_by_id_with_http_info(policy_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: A unique integer value identifying this enterprise policy. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: EnterprisePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_policy_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `get_policy_by_id`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_policy_by_id`")

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policy_id'] = params['policy_id']
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
            '/enterprise/{enterprise_id}/policy/{policy_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EnterprisePolicy',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def partial_update_policy(self, policy_id, enterprise_id, data, **kwargs):
        """Partial update policy

        Returns updated policy
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_policy(policy_id, enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: A unique integer value identifying this enterprise policy. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param EnterprisePolicy data: (required)
        :return: EnterprisePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.partial_update_policy_with_http_info(policy_id, enterprise_id, data, **kwargs)
        else:
            (data) = self.partial_update_policy_with_http_info(policy_id, enterprise_id, data, **kwargs)
            return data

    def partial_update_policy_with_http_info(self, policy_id, enterprise_id, data, **kwargs):
        """Partial update policy

        Returns updated policy
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_policy_with_http_info(policy_id, enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: A unique integer value identifying this enterprise policy. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param EnterprisePolicy data: (required)
        :return: EnterprisePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'enterprise_id', 'data']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method partial_update_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `partial_update_policy`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `partial_update_policy`")
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `partial_update_policy`")

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policy_id'] = params['policy_id']
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
            '/enterprise/{enterprise_id}/policy/{policy_id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EnterprisePolicy',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_policy(self, policy_id, enterprise_id, data, **kwargs):
        """Update/Replace information

        Returns updated policy
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_policy(policy_id, enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: A unique integer value identifying this enterprise policy. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param EnterprisePolicy data: (required)
        :return: EnterprisePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_policy_with_http_info(policy_id, enterprise_id, data, **kwargs)
        else:
            (data) = self.update_policy_with_http_info(policy_id, enterprise_id, data, **kwargs)
            return data

    def update_policy_with_http_info(self, policy_id, enterprise_id, data, **kwargs):
        """Update/Replace information

        Returns updated policy
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_policy_with_http_info(policy_id, enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: A unique integer value identifying this enterprise policy. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param EnterprisePolicy data: (required)
        :return: EnterprisePolicy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'enterprise_id', 'data']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `update_policy`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `update_policy`")
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `update_policy`")

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policy_id'] = params['policy_id']
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
            '/enterprise/{enterprise_id}/policy/{policy_id}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EnterprisePolicy',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
