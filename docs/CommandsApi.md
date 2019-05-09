# esperclient.CommandsApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_command**](CommandsApi.md#get_command) | **GET** /enterprise/{enterprise_id}/device/{device_id}/command/{command_id}/ | Get command status
[**run_command**](CommandsApi.md#run_command) | **POST** /enterprise/{enterprise_id}/device/{device_id}/command/ | Run commands on device


# **get_command**
> DeviceCommand get_command(command_id, device_id, enterprise_id)

Get command status

Return DeviceCommand instance

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
api_instance = esperclient.CommandsApi(esperclient.ApiClient(configuration))
command_id = 'command_id_example' # str | A UUID string identifying this device command.
device_id = 'device_id_example' # str | A UUID string identifying this device.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Get command status
    api_response = api_instance.get_command(command_id, device_id, enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->get_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | [**str**](.md)| A UUID string identifying this device command. | 
 **device_id** | [**str**](.md)| A UUID string identifying this device. | 
 **enterprise_id** | [**str**](.md)| A UUID string identifying enterprise. | 

### Return type

[**DeviceCommand**](DeviceCommand.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_command**
> DeviceCommand run_command(enterprise_id, device_id, command)

Run commands on device

Fire commands on device like reboot, ping etc

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
api_instance = esperclient.CommandsApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
device_id = 'device_id_example' # str | ID of the device
command = esperclient.CommandRequest() # CommandRequest | Command request body

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
 **command** | [**CommandRequest**](CommandRequest.md)| Command request body | 

### Return type

[**DeviceCommand**](DeviceCommand.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

