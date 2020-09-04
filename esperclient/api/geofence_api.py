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


class GeofenceApi(object):
    """NOTE: This class is auto generated.

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_geofence(self, data, enterprise_id, **kwargs):
        """Create a geofence

        Returns Geofence instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_geofence(data, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Geofence data: (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_geofence_with_http_info(data, enterprise_id, **kwargs)
        else:
            (data) = self.create_geofence_with_http_info(data, enterprise_id, **kwargs)
            return data

    def create_geofence_with_http_info(self, data, enterprise_id, **kwargs):
        """Create a geofence

        Returns Geofence instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_geofence_with_http_info(data, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Geofence data: (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_geofence" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `create_geofence`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `create_geofence`")

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
            '/v0/enterprise/{enterprise_id}/geofence/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Geofence',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_geofence(self, geofence_id, enterprise_id, **kwargs):
        """Delete a geofence

        Empty response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_geofence(geofence_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str geofence_id: A UUID string identifying the geofence. (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_geofence_with_http_info(geofence_id, enterprise_id, **kwargs)
        else:
            (data) = self.delete_geofence_with_http_info(geofence_id, enterprise_id, **kwargs)
            return data

    def delete_geofence_with_http_info(self, geofence_id, enterprise_id, **kwargs):
        """Delete a geofence

        Empty response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_geofence_with_http_info(geofence_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str geofence_id: A UUID string identifying the geofence. (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['geofence_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_geofence" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'geofence_id' is set
        if ('geofence_id' not in params or
                params['geofence_id'] is None):
            raise ValueError("Missing the required parameter `geofence_id` when calling `delete_geofence`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `delete_geofence`")

        collection_formats = {}

        path_params = {}
        if 'geofence_id' in params:
            path_params['geofence_id'] = params['geofence_id']
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
            '/v0/enterprise/{enterprise_id}/geofence/{geofence_id}/', 'DELETE',
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

    def get_all_geofences(self, enterprise_id, **kwargs):
        """List Geofences in Enterprise

        API to view all the geofences in an enterprise
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_geofences(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :param str search: A search term.
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_geofences_with_http_info(enterprise_id, **kwargs)
        else:
            (data) = self.get_all_geofences_with_http_info(enterprise_id, **kwargs)
            return data

    def get_all_geofences_with_http_info(self, enterprise_id, **kwargs):
        """List Geofences in Enterprise

        API to view all the geofences in an enterprise
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_geofences_with_http_info(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :param str search: A search term.
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse20010
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
                    " to method get_all_geofences" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_all_geofences`")

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
            '/v0/enterprise/{enterprise_id}/geofence/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20010',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_geofence(self, geofence_id, enterprise_id, **kwargs):
        """Get geofence information

        Returns geofence instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_geofence(geofence_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str geofence_id: A UUID string identifying the geofence. (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_geofence_with_http_info(geofence_id, enterprise_id, **kwargs)
        else:
            (data) = self.get_geofence_with_http_info(geofence_id, enterprise_id, **kwargs)
            return data

    def get_geofence_with_http_info(self, geofence_id, enterprise_id, **kwargs):
        """Get geofence information

        Returns geofence instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_geofence_with_http_info(geofence_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str geofence_id: A UUID string identifying the geofence. (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['geofence_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_geofence" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'geofence_id' is set
        if ('geofence_id' not in params or
                params['geofence_id'] is None):
            raise ValueError("Missing the required parameter `geofence_id` when calling `get_geofence`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_geofence`")

        collection_formats = {}

        path_params = {}
        if 'geofence_id' in params:
            path_params['geofence_id'] = params['geofence_id']
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
            '/v0/enterprise/{enterprise_id}/geofence/{geofence_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Geofence',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def partial_update_geofence(self, geofence_id, enterprise_id, data, **kwargs):
        """Partially updates geofence information

        Returns geofence instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_geofence(geofence_id, enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str geofence_id: A UUID string identifying the geofence. (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :param GeofenceUpdate data: (required)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.partial_update_geofence_with_http_info(geofence_id, enterprise_id, data, **kwargs)
        else:
            (data) = self.partial_update_geofence_with_http_info(geofence_id, enterprise_id, data, **kwargs)
            return data

    def partial_update_geofence_with_http_info(self, geofence_id, enterprise_id, data, **kwargs):
        """Partially updates geofence information

        Returns geofence instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.partial_update_geofence_with_http_info(geofence_id, enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str geofence_id: A UUID string identifying the geofence. (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :param GeofenceUpdate data: (required)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['geofence_id', 'enterprise_id', 'data']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method partial_update_geofence" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'geofence_id' is set
        if ('geofence_id' not in params or
                params['geofence_id'] is None):
            raise ValueError("Missing the required parameter `geofence_id` when calling `partial_update_geofence`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `partial_update_geofence`")
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `partial_update_geofence`")

        collection_formats = {}

        path_params = {}
        if 'geofence_id' in params:
            path_params['geofence_id'] = params['geofence_id']
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
            '/v0/enterprise/{enterprise_id}/geofence/{geofence_id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Geofence',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_geofence(self, geofence_id, enterprise_id, data, **kwargs):
        """Update geofence information

        Returns geofence instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_geofence(geofence_id, enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str geofence_id: A UUID string identifying the geofence. (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :param Geofence data: (required)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_geofence_with_http_info(geofence_id, enterprise_id, data, **kwargs)
        else:
            (data) = self.update_geofence_with_http_info(geofence_id, enterprise_id, data, **kwargs)
            return data

    def update_geofence_with_http_info(self, geofence_id, enterprise_id, data, **kwargs):
        """Update geofence information

        Returns geofence instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_geofence_with_http_info(geofence_id, enterprise_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str geofence_id: A UUID string identifying the geofence. (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :param Geofence data: (required)
        :return: Geofence
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['geofence_id', 'enterprise_id', 'data']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_geofence" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'geofence_id' is set
        if ('geofence_id' not in params or
                params['geofence_id'] is None):
            raise ValueError("Missing the required parameter `geofence_id` when calling `update_geofence`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `update_geofence`")
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `update_geofence`")

        collection_formats = {}

        path_params = {}
        if 'geofence_id' in params:
            path_params['geofence_id'] = params['geofence_id']
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
            '/v0/enterprise/{enterprise_id}/geofence/{geofence_id}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Geofence',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
