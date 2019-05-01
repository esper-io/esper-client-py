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
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.CommandsApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
device_id = 'device_id_example' # str | ID of the device
command = esperclient.CommandRequest() # CommandRequest | command name to fire

try:
    # Run commands on device
    api_response = api_instance.run_command(enterprise_id, device_id, command)
    print(api_response)
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

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

