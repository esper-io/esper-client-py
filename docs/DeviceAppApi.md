# esperclient.DeviceAppApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_app_by_id**](DeviceAppApi.md#get_device_app_by_id) | **GET** /enterprise/{enterprise_id}/device/{device_id}/app/{app_id}/ | Get app information
[**get_device_apps**](DeviceAppApi.md#get_device_apps) | **GET** /enterprise/{enterprise_id}/device/{device_id}/app/ | List all device apps


# **get_device_app_by_id**
> DeviceApp get_device_app_by_id(app_id, enterprise_id, device_id)

Get app information

Returns DeviceApp instance

### Example
```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.DeviceAppApi(esperclient.ApiClient(configuration))
app_id = 'app_id_example' # str | A UUID string identifying this device app.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this device.
device_id = 'device_id_example' # str | A UUID string identifying this enteprise.

try:
    # Get app information
    api_response = api_instance.get_device_app_by_id(app_id, enterprise_id, device_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceAppApi->get_device_app_by_id: %s\n" % e)
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

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_apps**
> InlineResponse2004 get_device_apps(enterprise_id, device_id, package_name=package_name, whitelisted=whitelisted, search=search, limit=limit, offset=offset)

List all device apps

Returns DeviceApp list

### Example
```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.DeviceAppApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
device_id = 'device_id_example' # str | A UUID string identifying device.
package_name = 'package_name_example' # str | package name contains filter (optional)
whitelisted = 'whitelisted_example' # str | Whitelist filter (optional)
search = 'search_example' # str | A search term. Search by app_name. (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # List all device apps
    api_response = api_instance.get_device_apps(enterprise_id, device_id, package_name=package_name, whitelisted=whitelisted, search=search, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceAppApi->get_device_apps: %s\n" % e)
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

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

