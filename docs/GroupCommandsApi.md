# esperclient.GroupCommandsApi

All URIs are relative to *https://foo.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_group_command**](GroupCommandsApi.md#get_group_command) | **GET** /enterprise/{enterprise_id}/devicegroup/{group_id}/command/{command_id}/ | Get group command status
[**run_group_command**](GroupCommandsApi.md#run_group_command) | **POST** /enterprise/{enterprise_id}/devicegroup/{group_id}/command/ | Run commands on group devices


# **get_group_command**
> GroupCommand get_group_command(command_id, group_id, enterprise_id)

Get group command status

Returns GroupCommand instance

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
api_instance = esperclient.GroupCommandsApi(esperclient.ApiClient(configuration))
command_id = 'command_id_example' # str | A UUID string identifying this device command.
group_id = 'group_id_example' # str | A UUID string identifying this group.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Get group command status
    api_response = api_instance.get_group_command(command_id, group_id, enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling GroupCommandsApi->get_group_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | [**str**](.md)| A UUID string identifying this device command. | 
 **group_id** | [**str**](.md)| A UUID string identifying this group. | 
 **enterprise_id** | [**str**](.md)| A UUID string identifying enterprise. | 

### Return type

[**GroupCommand**](GroupCommand.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_group_command**
> GroupCommand run_group_command(enterprise_id, group_id, data)

Run commands on group devices

Fire commands on all the group devices

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
api_instance = esperclient.GroupCommandsApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
group_id = 'group_id_example' # str | ID of the group
data = esperclient.GroupCommandRequest() # GroupCommandRequest | Group command request

try:
    # Run commands on group devices
    api_response = api_instance.run_group_command(enterprise_id, group_id, data)
    print(api_response)
except ApiException as e:
    print("Exception when calling GroupCommandsApi->run_group_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 
 **group_id** | [**str**](.md)| ID of the group | 
 **data** | [**GroupCommandRequest**](GroupCommandRequest.md)| Group command request | 

### Return type

[**GroupCommand**](GroupCommand.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

