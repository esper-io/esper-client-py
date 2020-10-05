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


class SubscriptionApi(object):
    """NOTE: This class is auto generated.

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_subscription(self, data, enterprise_id, **kwargs):
        """Create a Subscription

        Returns Subscription instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_subscription(data, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EventSubscriptionArgs data: (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :return: EventSubscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_subscription_with_http_info(data, enterprise_id, **kwargs)
        else:
            (data) = self.create_subscription_with_http_info(data, enterprise_id, **kwargs)
            return data

    def create_subscription_with_http_info(self, data, enterprise_id, **kwargs):
        """Create a Subscription

        Returns Subscription instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_subscription_with_http_info(data, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EventSubscriptionArgs data: (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :return: EventSubscription
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
                    " to method create_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `create_subscription`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `create_subscription`")

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
            '/v0/enterprise/{enterprise_id}/subscription/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventSubscription',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_subscription(self, subscription_id, enterprise_id, **kwargs):
        """Delete a subscription

        Empty response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_subscription(subscription_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subscription_id: A UUID string identifying the subscription. (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_subscription_with_http_info(subscription_id, enterprise_id, **kwargs)
        else:
            (data) = self.delete_subscription_with_http_info(subscription_id, enterprise_id, **kwargs)
            return data

    def delete_subscription_with_http_info(self, subscription_id, enterprise_id, **kwargs):
        """Delete a subscription

        Empty response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_subscription_with_http_info(subscription_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subscription_id: A UUID string identifying the subscription. (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `delete_subscription`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `delete_subscription`")

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in params:
            path_params['subscription_id'] = params['subscription_id']
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
            '/v0/enterprise/{enterprise_id}/subscription/{subscription_id}/', 'DELETE',
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

    def get_all_subscriptions(self, enterprise_id, **kwargs):
        """List Subscriptions in Enterprise

        API to view all the subscriptions in an enterprise
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_subscriptions(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_subscriptions_with_http_info(enterprise_id, **kwargs)
        else:
            (data) = self.get_all_subscriptions_with_http_info(enterprise_id, **kwargs)
            return data

    def get_all_subscriptions_with_http_info(self, enterprise_id, **kwargs):
        """List Subscriptions in Enterprise

        API to view all the subscriptions in an enterprise
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_subscriptions_with_http_info(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'limit', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_all_subscriptions`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = []
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
            '/v0/enterprise/{enterprise_id}/subscription/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_subscription(self, subscription_id, enterprise_id, **kwargs):
        """Get subscription information

        Returns subscription instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_subscription(subscription_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subscription_id: A UUID string identifying the subscription. (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :return: EventSubscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_subscription_with_http_info(subscription_id, enterprise_id, **kwargs)
        else:
            (data) = self.get_subscription_with_http_info(subscription_id, enterprise_id, **kwargs)
            return data

    def get_subscription_with_http_info(self, subscription_id, enterprise_id, **kwargs):
        """Get subscription information

        Returns subscription instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_subscription_with_http_info(subscription_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subscription_id: A UUID string identifying the subscription. (required)
        :param str enterprise_id: A UUID string identifying the enterprise. (required)
        :return: EventSubscription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_subscription`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_subscription`")

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in params:
            path_params['subscription_id'] = params['subscription_id']
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
            '/v0/enterprise/{enterprise_id}/subscription/{subscription_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventSubscription',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
