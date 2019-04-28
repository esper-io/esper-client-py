# esperclient.DeviceApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_devices**](DeviceApi.md#get_all_devices) | **GET** /enterprise/{enterprise_id}/device/ | Fetch all devices in an enterprise
[**get_app_installs**](DeviceApi.md#get_app_installs) | **GET** /enterprise/{enterprise_id}/device/{device_id}/install/ | List installed apps
[**get_device_by_id**](DeviceApi.md#get_device_by_id) | **GET** /enterprise/{enterprise_id}/device/{device_id}/ | Fetch device details by ID
[**get_device_event**](DeviceApi.md#get_device_event) | **GET** /enterprise/{enterprise_id}/device/{device_id}/status/ | Get latest device event


# **get_all_devices**
> InlineResponse2003 get_all_devices(enterprise_id, name=name, search=search, limit=limit, offset=offset)

Fetch all devices in an enterprise

Returns a list of devices

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
api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
name = 'name_example' # str | Filter by device name (optional)
search = 'search_example' # str | A search term. Search by device name or imei (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # Fetch all devices in an enterprise
    api_response = api_instance.get_all_devices(enterprise_id, name=name, search=search, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_all_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 
 **name** | **str**| Filter by device name | [optional] 
 **search** | **str**| A search term. Search by device name or imei | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_installs**
> InlineResponse2005 get_app_installs(enterprise_id, device_id, device=device, package_name=package_name, application_name=application_name, install_state=install_state, limit=limit, offset=offset)

List installed apps

Returns AppInstall list

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
api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
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
    api_response = api_instance.get_app_installs(enterprise_id, device_id, device=device, package_name=package_name, application_name=application_name, install_state=install_state, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_app_installs: %s\n" % e)
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

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_id**
> Device get_device_by_id(enterprise_id, device_id)

Fetch device details by ID

Returns details of a device

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
api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
device_id = 'device_id_example' # str | ID of the device

try:
    # Fetch device details by ID
    api_response = api_instance.get_device_by_id(enterprise_id, device_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 
 **device_id** | [**str**](.md)| ID of the device | 

### Return type

[**Device**](Device.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_event**
> InlineResponse2006 get_device_event(enterprise_id, device_id, latest_event)

Get latest device event

Returns DeviceStatus instance

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
api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
device_id = 'device_id_example' # str | A UUID string identifying device.
latest_event = 8.14 # float | Flag to get latest event

try:
    # Get latest device event
    api_response = api_instance.get_device_event(enterprise_id, device_id, latest_event)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_device_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying this enterprise. | 
 **device_id** | **str**| A UUID string identifying device. | 
 **latest_event** | **float**| Flag to get latest event | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

