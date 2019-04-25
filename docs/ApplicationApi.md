# esperclient.ApplicationApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](ApplicationApi.md#delete) | **DELETE** /enterprise/{enterprise_id}/application/{application_id}/ | Delete an application
[**delete_app_version**](ApplicationApi.md#delete_app_version) | **DELETE** /enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/ | Delete app version
[**get**](ApplicationApi.md#get) | **GET** /enterprise/{enterprise_id}/application/{application_id}/ | Get application information
[**get_app_version**](ApplicationApi.md#get_app_version) | **GET** /enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/ | Get app version information
[**get_app_versions**](ApplicationApi.md#get_app_versions) | **GET** /enterprise/{enterprise_id}/application/{application_id}/version/ | List App versions
[**list**](ApplicationApi.md#list) | **GET** /enterprise/{enterprise_id}/application/ | List apps in enterprise


# **delete**
> delete(application_id, enterprise_id)

Delete an application

Empty response

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_security
configuration = esperclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
application_id = 'application_id_example' # str | A UUID string identifying this application.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Delete an application
    api_instance.delete(application_id, enterprise_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | [**str**](.md)| A UUID string identifying this application. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

void (empty response body)

### Authorization

[basic_security](../README.md#basic_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_version**
> delete_app_version(version_id, application_id, enterprise_id)

Delete app version

Empty response

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.ApplicationApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Application get(application_id, enterprise_id)

Get application information

Returns Application instance

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_security
configuration = esperclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
application_id = 'application_id_example' # str | A UUID string identifying this application.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Get application information
    api_response = api_instance.get(application_id, enterprise_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | [**str**](.md)| A UUID string identifying this application. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

[**Application**](Application.md)

### Authorization

[basic_security](../README.md#basic_security)

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
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_security
configuration = esperclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
version_id = 'version_id_example' # str | A UUID string identifying this app version.
application_id = 'application_id_example' # str | A UUID string identifying this application.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Get app version information
    api_response = api_instance.get_app_version(version_id, application_id, enterprise_id)
    pprint(api_response)
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

[basic_security](../README.md#basic_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_versions**
> InlineResponse2002 get_app_versions(application_id, enterprise_id, version_code=version_code, build_number=build_number, limit=limit, offset=offset)

List App versions

Returns AppVersion list

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_security
configuration = esperclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
application_id = 'application_id_example' # str | A UUID string identifying this application.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
version_code = 'version_code_example' # str | filter by version code (optional)
build_number = 'build_number_example' # str | filter by build number (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # List App versions
    api_response = api_instance.get_app_versions(application_id, enterprise_id, version_code=version_code, build_number=build_number, limit=limit, offset=offset)
    pprint(api_response)
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
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[basic_security](../README.md#basic_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> InlineResponse2001 list(enterprise_id, application_name=application_name, package_name=package_name, limit=limit, offset=offset)

List apps in enterprise

Returns Application list

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_security
configuration = esperclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
application_name = 'application_name_example' # str | filter by application name (optional)
package_name = 'package_name_example' # str | filter by package name (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # List apps in enterprise
    api_response = api_instance.list(enterprise_id, application_name=application_name, package_name=package_name, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying this enterprise. | 
 **application_name** | **str**| filter by application name | [optional] 
 **package_name** | **str**| filter by package name | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basic_security](../README.md#basic_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

