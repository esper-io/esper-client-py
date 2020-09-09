# esperclient.ApplicationApi

All URIs are relative to *https://foo-api.esper.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_app_version**](ApplicationApi.md#delete_app_version) | **DELETE** /enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/ | Delete app version
[**delete_application**](ApplicationApi.md#delete_application) | **DELETE** /enterprise/{enterprise_id}/application/{application_id}/ | Delete an application
[**get_all_applications**](ApplicationApi.md#get_all_applications) | **GET** /enterprise/{enterprise_id}/application/ | List apps in enterprise
[**get_app_version**](ApplicationApi.md#get_app_version) | **GET** /enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/ | Get app version information
[**get_app_versions**](ApplicationApi.md#get_app_versions) | **GET** /enterprise/{enterprise_id}/application/{application_id}/version/ | List App versions
[**get_application**](ApplicationApi.md#get_application) | **GET** /enterprise/{enterprise_id}/application/{application_id}/ | Get application information
[**get_install_devices**](ApplicationApi.md#get_install_devices) | **GET** /enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/installdevices | List install devices
[**upload**](ApplicationApi.md#upload) | **POST** /enterprise/{enterprise_id}/application/upload/ | Upload an application to enterprise


# **delete_app_version**
> delete_app_version(version_id, application_id, enterprise_id)

Delete app version

Empty response

### Example
```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.host = 'SERVER_URL'
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
version_id = 'version_id_example' # str | A UUID string identifying this app version.
application_id = 'application_id_example' # str | A UUID string identifying this application.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Delete app version
    api_instance.delete_app_version(version_id, application_id, enterprise_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_app_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**str**](.md)| A UUID string identifying this app version. | 
 **application_id** | [**str**](.md)| A UUID string identifying this application. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(application_id, enterprise_id)

Delete an application

Empty response

### Example
```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.host = 'SERVER_URL'
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
application_id = 'application_id_example' # str | A UUID string identifying this application.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Delete an application
    api_instance.delete_application(application_id, enterprise_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | [**str**](.md)| A UUID string identifying this application. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_applications**
> InlineResponse200 get_all_applications(enterprise_id, application_name=application_name, package_name=package_name, is_hidden=is_hidden, limit=limit, offset=offset)

List apps in enterprise

Returns Application list

### Example
```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.host = 'SERVER_URL'
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
application_name = 'application_name_example' # str | filter by application name (optional)
package_name = 'package_name_example' # str | filter by package name (optional)
is_hidden = true # bool | filter default esper apps (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 0 # int | The initial index from which to return the results. (optional) (default to 0)

try:
    # List apps in enterprise
    api_response = api_instance.get_all_applications(enterprise_id, application_name=application_name, package_name=package_name, is_hidden=is_hidden, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_all_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying this enterprise. | 
 **application_name** | **str**| filter by application name | [optional] 
 **package_name** | **str**| filter by package name | [optional] 
 **is_hidden** | **bool**| filter default esper apps | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] [default to 0]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_version**
> AppVersion get_app_version(version_id, application_id, enterprise_id)

Get app version information

Returns AppVersion instance

### Example
```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.host = 'SERVER_URL'
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
version_id = 'version_id_example' # str | A UUID string identifying this app version.
application_id = 'application_id_example' # str | A UUID string identifying this application.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Get app version information
    api_response = api_instance.get_app_version(version_id, application_id, enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_app_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**str**](.md)| A UUID string identifying this app version. | 
 **application_id** | [**str**](.md)| A UUID string identifying this application. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

[**AppVersion**](AppVersion.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_versions**
> InlineResponse2001 get_app_versions(application_id, enterprise_id, version_code=version_code, build_number=build_number, limit=limit, offset=offset)

List App versions

Returns AppVersion list

### Example
```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.host = 'SERVER_URL'
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
application_id = 'application_id_example' # str | A UUID string identifying this application.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
version_code = 'version_code_example' # str | filter by version code (optional)
build_number = 'build_number_example' # str | filter by build number (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 0 # int | The initial index from which to return the results. (optional) (default to 0)

try:
    # List App versions
    api_response = api_instance.get_app_versions(application_id, enterprise_id, version_code=version_code, build_number=build_number, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_app_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | [**str**](.md)| A UUID string identifying this application. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **version_code** | **str**| filter by version code | [optional] 
 **build_number** | **str**| filter by build number | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] [default to 0]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> Application get_application(application_id, enterprise_id)

Get application information

Returns Application instance

### Example
```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.host = 'SERVER_URL'
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
application_id = 'application_id_example' # str | A UUID string identifying this application.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Get application information
    api_response = api_instance.get_application(application_id, enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | [**str**](.md)| A UUID string identifying this application. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

[**Application**](Application.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_install_devices**
> InlineResponse2002 get_install_devices(version_id, application_id, enterprise_id, search=search, limit=limit, offset=offset)

List install devices

Returns list of devices with the specified app version installed

### Example
```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.host = 'SERVER_URL'
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
version_id = 'version_id_example' # str | A UUID string identifying this app version.
application_id = 'application_id_example' # str | A UUID string identifying this application.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
search = 'search_example' # str | A search term (optional)
limit = 56 # int | Number of results to return per page (optional)
offset = 56 # int | The initial index from which to return the results (optional)

try:
    # List install devices
    api_response = api_instance.get_install_devices(version_id, application_id, enterprise_id, search=search, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_install_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | [**str**](.md)| A UUID string identifying this app version. | 
 **application_id** | [**str**](.md)| A UUID string identifying this application. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **search** | **str**| A search term | [optional] 
 **limit** | **int**| Number of results to return per page | [optional] 
 **offset** | **int**| The initial index from which to return the results | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> InlineResponse201 upload(enterprise_id, app_file)

Upload an application to enterprise

Returns application

### Example
```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.host = 'SERVER_URL'
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
app_file = '/path/to/file.txt' # file | Valid APK file

try:
    # Upload an application to enterprise
    api_response = api_instance.upload(enterprise_id, app_file)
    print(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying this enterprise. | 
 **app_file** | **file**| Valid APK file | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

