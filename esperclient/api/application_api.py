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


class ApplicationApi(object):
    """NOTE: This class is auto generated.

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_app_version(self, version_id, application_id, enterprise_id, **kwargs):
        """Delete app version

        Empty response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_app_version(version_id, application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version_id: A UUID string identifying this app version. (required)
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_app_version_with_http_info(version_id, application_id, enterprise_id, **kwargs)
        else:
            (data) = self.delete_app_version_with_http_info(version_id, application_id, enterprise_id, **kwargs)
            return data

    def delete_app_version_with_http_info(self, version_id, application_id, enterprise_id, **kwargs):
        """Delete app version

        Empty response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_app_version_with_http_info(version_id, application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version_id: A UUID string identifying this app version. (required)
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version_id', 'application_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_app_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `delete_app_version`")
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `delete_app_version`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `delete_app_version`")

        collection_formats = {}

        path_params = {}
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']
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
            '/enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/', 'DELETE',
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

    def delete_application(self, application_id, enterprise_id, **kwargs):
        """Delete an application

        Empty response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_application(application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_application_with_http_info(application_id, enterprise_id, **kwargs)
        else:
            (data) = self.delete_application_with_http_info(application_id, enterprise_id, **kwargs)
            return data

    def delete_application_with_http_info(self, application_id, enterprise_id, **kwargs):
        """Delete an application

        Empty response
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_application_with_http_info(application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_application" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `delete_application`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `delete_application`")

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']
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
            '/enterprise/{enterprise_id}/application/{application_id}/', 'DELETE',
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

    def get_all_applications(self, enterprise_id, **kwargs):
        """List apps in enterprise

        Returns Application list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_applications(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param str application_name: filter by application name
        :param str package_name: filter by package name
        :param bool is_hidden: filter default esper apps
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_applications_with_http_info(enterprise_id, **kwargs)
        else:
            (data) = self.get_all_applications_with_http_info(enterprise_id, **kwargs)
            return data

    def get_all_applications_with_http_info(self, enterprise_id, **kwargs):
        """List apps in enterprise

        Returns Application list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_applications_with_http_info(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param str application_name: filter by application name
        :param str package_name: filter by package name
        :param bool is_hidden: filter default esper apps
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'application_name', 'package_name', 'is_hidden', 'limit', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_applications" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_all_applications`")

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = []
        if 'application_name' in params:
            query_params.append(('application_name', params['application_name']))
        if 'package_name' in params:
            query_params.append(('package_name', params['package_name']))
        if 'is_hidden' in params:
            query_params.append(('is_hidden', params['is_hidden']))
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
            '/enterprise/{enterprise_id}/application/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_app_version(self, version_id, application_id, enterprise_id, **kwargs):
        """Get app version information

        Returns AppVersion instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_app_version(version_id, application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version_id: A UUID string identifying this app version. (required)
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param bool legacy_format: If False, returns standardized format with version_name and version_code (build_number removed). If True or not specified, returns legacy format. (optional)
        :return: AppVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_app_version_with_http_info(version_id, application_id, enterprise_id, **kwargs)
        else:
            (data) = self.get_app_version_with_http_info(version_id, application_id, enterprise_id, **kwargs)
            return data

    def get_app_version_with_http_info(self, version_id, application_id, enterprise_id, **kwargs):
        """Get app version information

        Returns AppVersion instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_app_version_with_http_info(version_id, application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version_id: A UUID string identifying this app version. (required)
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param bool legacy_format: If False, returns standardized format with version_name and version_code (build_number removed). If True or not specified, returns legacy format. (optional)
        :return: AppVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version_id', 'application_id', 'enterprise_id', 'legacy_format']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_app_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `get_app_version`")
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `get_app_version`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_app_version`")

        collection_formats = {}

        path_params = {}
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = []
        if 'legacy_format' in params:
            # Convert boolean to lowercase string for API compatibility
            legacy_format_val = params['legacy_format']
            if isinstance(legacy_format_val, bool):
                legacy_format_val = str(legacy_format_val).lower()
            query_params.append(('legacy_format', legacy_format_val))

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
            '/enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AppVersion',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_app_versions(self, application_id, enterprise_id, **kwargs):
        """List App versions

        Returns AppVersion list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_app_versions(application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param str version_code: filter by version code
        :param str build_number: filter by build number
        :param bool legacy_format: If False, returns standardized format with version_name and version_code (build_number removed). If True or not specified, returns legacy format. (optional)
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_app_versions_with_http_info(application_id, enterprise_id, **kwargs)
        else:
            (data) = self.get_app_versions_with_http_info(application_id, enterprise_id, **kwargs)
            return data

    def get_app_versions_with_http_info(self, application_id, enterprise_id, **kwargs):
        """List App versions

        Returns AppVersion list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_app_versions_with_http_info(application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param str version_code: filter by version code
        :param str build_number: filter by build number
        :param bool legacy_format: If False, returns standardized format with version_name and version_code (build_number removed). If True or not specified, returns legacy format. (optional)
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'enterprise_id', 'version_code', 'build_number', 'legacy_format', 'limit', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_app_versions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `get_app_versions`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_app_versions`")

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = []
        if 'version_code' in params:
            query_params.append(('version_code', params['version_code']))
        if 'build_number' in params:
            query_params.append(('build_number', params['build_number']))
        if 'legacy_format' in params:
            # Convert boolean to lowercase string for API compatibility
            legacy_format_val = params['legacy_format']
            if isinstance(legacy_format_val, bool):
                legacy_format_val = str(legacy_format_val).lower()
            query_params.append(('legacy_format', legacy_format_val))
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
            '/enterprise/{enterprise_id}/application/{application_id}/version/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_application(self, application_id, enterprise_id, **kwargs):
        """Get application information

        Returns Application instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application(application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_application_with_http_info(application_id, enterprise_id, **kwargs)
        else:
            (data) = self.get_application_with_http_info(application_id, enterprise_id, **kwargs)
            return data

    def get_application_with_http_info(self, application_id, enterprise_id, **kwargs):
        """Get application information

        Returns Application instance
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application_with_http_info(application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'enterprise_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_application" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `get_application`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_application`")

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']
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
            '/enterprise/{enterprise_id}/application/{application_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Application',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_install_devices(self, version_id, application_id, enterprise_id, **kwargs):
        """List install devices

        Returns list of devices with the specified app version installed
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_install_devices(version_id, application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version_id: A UUID string identifying this app version. (required)
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param str search: A search term
        :param int limit: Number of results to return per page
        :param int offset: The initial index from which to return the results
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_install_devices_with_http_info(version_id, application_id, enterprise_id, **kwargs)
        else:
            (data) = self.get_install_devices_with_http_info(version_id, application_id, enterprise_id, **kwargs)
            return data

    def get_install_devices_with_http_info(self, version_id, application_id, enterprise_id, **kwargs):
        """List install devices

        Returns list of devices with the specified app version installed
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_install_devices_with_http_info(version_id, application_id, enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str version_id: A UUID string identifying this app version. (required)
        :param str application_id: A UUID string identifying this application. (required)
        :param str enterprise_id: A UUID string identifying enterprise. (required)
        :param str search: A search term
        :param int limit: Number of results to return per page
        :param int offset: The initial index from which to return the results
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version_id', 'application_id', 'enterprise_id', 'search', 'limit', 'offset']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_install_devices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `get_install_devices`")
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `get_install_devices`")
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_install_devices`")

        collection_formats = {}

        path_params = {}
        if 'version_id' in params:
            path_params['version_id'] = params['version_id']
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']
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
            '/enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/installdevices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload(self, enterprise_id, app_file, **kwargs):
        """Upload an application to enterprise

        Returns application
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload(enterprise_id, app_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param file app_file: Valid APK file (required)
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_with_http_info(enterprise_id, app_file, **kwargs)
        else:
            (data) = self.upload_with_http_info(enterprise_id, app_file, **kwargs)
            return data

    def upload_with_http_info(self, enterprise_id, app_file, **kwargs):
        """Upload an application to enterprise

        Returns application
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_with_http_info(enterprise_id, app_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: A UUID string identifying this enterprise. (required)
        :param file app_file: Valid APK file (required)
        :return: InlineResponse201
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
                    " to method upload" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `upload`")
        # verify the required parameter 'app_file' is set
        if ('app_file' not in params or
                params['app_file'] is None):
            raise ValueError("Missing the required parameter `app_file` when calling `upload`")

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
            ['multipart/form-data', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api(
            '/enterprise/{enterprise_id}/application/upload/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse201',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
