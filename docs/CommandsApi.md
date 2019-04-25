# esperclient.CommandsApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_command**](CommandsApi.md#run_command) | **POST** /enterprise/{enterprise_id}/device/{device_id}/command/ | Run commands on device


# **run_command**
> DeviceCommand run_command(enterprise_id, device_id, command)

Run commands on device

Fire commands on device like lock, ping etc

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
api_instance = esperclient.CommandsApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
device_id = 'device_id_example' # str | ID of the device
command = esperclient.CommandRequest() # CommandRequest | command name to fire

try:
    # Run commands on device
    api_response = api_instance.run_command(enterprise_id, device_id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->run_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 
 **device_id** | [**str**](.md)| ID of the device | 
 **command** | [**CommandRequest**](CommandRequest.md)| command name to fire | 

### Return type

[**DeviceCommand**](DeviceCommand.md)

### Authorization

[basic_security](../README.md#basic_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

