# esperclient.DeviceAppApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_app_by_id**](DeviceAppApi.md#device_app_by_id) | **GET** /enterprise/{enterprise_id}/device/{device_id}/app/{app_id}/ | Get app information
[**device_app_install_list**](DeviceAppApi.md#device_app_install_list) | **GET** /enterprise/{enterprise_id}/device/{device_id}/install/ | List installed apps
[**device_app_list**](DeviceAppApi.md#device_app_list) | **GET** /enterprise/{enterprise_id}/device/{device_id}/app/ | List all device apps


# **device_app_by_id**
> DeviceApp device_app_by_id(app_id, enterprise_id, device_id)

Get app information

Returns DeviceApp instance

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.DeviceAppApi()
app_id = 'app_id_example' # str | A UUID string identifying this device app.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this device.
device_id = 'device_id_example' # str | A UUID string identifying this enteprise.

try:
    # Get app information
    api_response = api_instance.device_app_by_id(app_id, enterprise_id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceAppApi->device_app_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | [**str**](.md)| A UUID string identifying this device app. | 
 **enterprise_id** | **str**| A UUID string identifying this device. | 
 **device_id** | **str**| A UUID string identifying this enteprise. | 

### Return type

[**DeviceApp**](DeviceApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_app_install_list**
> InlineResponse2005 device_app_install_list(enterprise_id, device_id, device=device, package_name=package_name, application_name=application_name, install_state=install_state, limit=limit, offset=offset)

List installed apps

Returns AppInstall list

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.DeviceAppApi()
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
device_id = 'device_id_example' # str | A UUID string identifying device.
device = 'device_example' # str | filter by device id (optional)
package_name = 'package_name_example' # str | filter by package name (optional)
application_name = 'application_name_example' # str | filter by application name (optional)
install_state = 'install_state_example' # str | filter by install state (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # List installed apps
    api_response = api_instance.device_app_install_list(enterprise_id, device_id, device=device, package_name=package_name, application_name=application_name, install_state=install_state, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceAppApi->device_app_install_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying this enterprise. | 
 **device_id** | **str**| A UUID string identifying device. | 
 **device** | **str**| filter by device id | [optional] 
 **package_name** | **str**| filter by package name | [optional] 
 **application_name** | **str**| filter by application name | [optional] 
 **install_state** | **str**| filter by install state | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_app_list**
> InlineResponse2004 device_app_list(enterprise_id, device_id, package_name=package_name, whitelisted=whitelisted, search=search, limit=limit, offset=offset)

List all device apps

Returns DeviceApp list

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.DeviceAppApi()
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
device_id = 'device_id_example' # str | A UUID string identifying device.
package_name = 'package_name_example' # str | package name contains filter (optional)
whitelisted = 'whitelisted_example' # str | Whitelist filter (optional)
search = 'search_example' # str | A search term. Search by app_name. (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # List all device apps
    api_response = api_instance.device_app_list(enterprise_id, device_id, package_name=package_name, whitelisted=whitelisted, search=search, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceAppApi->device_app_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying this enterprise. | 
 **device_id** | **str**| A UUID string identifying device. | 
 **package_name** | **str**| package name contains filter | [optional] 
 **whitelisted** | **str**| Whitelist filter | [optional] 
 **search** | **str**| A search term. Search by app_name. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

