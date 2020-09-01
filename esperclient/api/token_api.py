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


class TokenApi(object):
    """NOTE: This class is auto generated.

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_token_info(self, **kwargs):
        """Token Information

        API to get resource information associated with your token like your enterprise, user etc
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TokenInfoV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_token_info_with_http_info(**kwargs)
        else:
            (data) = self.get_token_info_with_http_info(**kwargs)
            return data

    def get_token_info_with_http_info(self, **kwargs):
        """Token Information

        API to get resource information associated with your token like your enterprise, user etc
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TokenInfoV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v1/token-info/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenInfoV1',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def renew_token(self, enterprise_id, developerapp_id, access_token, **kwargs):
        """Renew Token

        API to renew your token
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.renew_token(enterprise_id, developerapp_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param str developerapp_id: A UUID string identifying the developerapp (required)
        :param str access_token: Token to be renewed (required)
        :return: TokenRenewV0
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.renew_token_with_http_info(enterprise_id, developerapp_id, access_token, **kwargs)
        else:
            (data) = self.renew_token_with_http_info(enterprise_id, developerapp_id, access_token, **kwargs)
            return data

    def renew_token_with_http_info(self, enterprise_id, developerapp_id, access_token, **kwargs):
        """Renew Token

        API to renew your token
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.renew_token_with_http_info(enterprise_id, developerapp_id, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param str developerapp_id: A UUID string identifying the developerapp (required)
        :param str access_token: Token to be renewed (required)
        :return: TokenRenewV0
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'developerapp_id', 'access_token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method renew_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `renew_token`")
        # verify the required parameter 'developerapp_id' is set
        if ('developerapp_id' not in params or
                params['developerapp_id'] is None):
            raise ValueError("Missing the required parameter `developerapp_id` when calling `renew_token`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `renew_token`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']
        if 'developerapp_id' in params:
            path_params['developerapp_id'] = params['developerapp_id']

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))

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
            '/v0/enterprise/{enterprise_id}/developerapp/{developerapp_id}/renew-token/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenRenewV0',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
