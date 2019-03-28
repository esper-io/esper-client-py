# esper.CommandsApi

All URIs are relative to *https://127.0.0.1:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_command**](CommandsApi.md#run_command) | **POST** /enterprise/{enterprise_id}/device/{device_id}/command/ | Run commands on device

# **run_command**
> DeviceCommandResponse run_command(body, enterprise_id, device_id)

Run commands on device

Fire basic commands on device like lock, ping etc

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
api_instance = esper.CommandsApi(esper.ApiClient(configuration))
body = esper.DeviceCommandRequest() # DeviceCommandRequest | command name to fire
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
device_id = 'device_id_example' # str | ID of the device

try:
    # Run commands on device
    api_response = api_instance.run_command(body, enterprise_id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->run_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceCommandRequest**](DeviceCommandRequest.md)| command name to fire | 
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 
 **device_id** | [**str**](.md)| ID of the device | 

### Return type

[**DeviceCommandResponse**](DeviceCommandResponse.md)

### Authorization

[basic_security](../README.md#basic_security)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

