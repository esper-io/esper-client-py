# esper.DeviceApi

All URIs are relative to *https://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_devices**](DeviceApi.md#get_all_devices) | **GET** /enterprise/{enterprise_id}/device/ | Fetch all devices in an enterprise
[**get_device_by_id**](DeviceApi.md#get_device_by_id) | **GET** /enterprise/{enterprise_id}/device/{device_id}/ | Fetch device details by ID

# **get_all_devices**
> DeviceListResponse get_all_devices(enterprise_id)

Fetch all devices in an enterprise

Returns a list of devices

### Example
```python
from __future__ import print_function
import time
import esper
from esper.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic_security
configuration = esper.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esper.DeviceApi(esper.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise

try:
    # Fetch all devices in an enterprise
    api_response = api_instance.get_all_devices(enterprise_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_all_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 

### Return type

[**DeviceListResponse**](DeviceListResponse.md)

### Authorization

[basic_security](../README.md#basic_security)

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
from __future__ import print_function
import time
import esper
from esper.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic_security
configuration = esper.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esper.DeviceApi(esper.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
device_id = 'device_id_example' # str | ID of the device

try:
    # Fetch device details by ID
    api_response = api_instance.get_device_by_id(enterprise_id, device_id)
    pprint(api_response)
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

[basic_security](../README.md#basic_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

