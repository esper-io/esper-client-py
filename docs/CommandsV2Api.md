# esperclient.CommandsV2Api

All URIs are relative to *https://foo-api.esper.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_command**](CommandsV2Api.md#create_command) | **POST** /v0/enterprise/{enterprise_id}/command/ | Create a command request
[**get_command_request_status**](CommandsV2Api.md#get_command_request_status) | **GET** /v0/enterprise/{enterprise_id}/command/{request_id}/status/ | get status list for command request
[**get_device_command_history**](CommandsV2Api.md#get_device_command_history) | **GET** /v0/enterprise/{enterprise_id}/device/{device_id}/command-history/ | get command history for device
[**list_command_request**](CommandsV2Api.md#list_command_request) | **GET** /v0/enterprise/{enterprise_id}/command/ | List command requests
[**partial_update_command_status**](CommandsV2Api.md#partial_update_command_status) | **PATCH** /v0/enterprise/{enterprise_id}/command/{request_id}/status/{command_id}/ | Update command status


# **create_command**
> V0CommandRequest create_command(enterprise_id, request)

Create a command request

API to create a command request for the device.

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
api_instance = esperclient.CommandsV2Api(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
request = esperclient.V0CommandRequest() # V0CommandRequest | The request body to create a command for set of devices or groups

try:
    # Create a command request
    api_response = api_instance.create_command(enterprise_id, request)
    print(api_response)
except ApiException as e:
    print("Exception when calling CommandsV2Api->create_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 
 **request** | [**V0CommandRequest**](V0CommandRequest.md)| The request body to create a command for set of devices or groups | 

### Return type

[**V0CommandRequest**](V0CommandRequest.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_command_request_status**
> InlineResponse2009 get_command_request_status(enterprise_id, request_id, device=device, state=state)

get status list for command request

API to get and filter command request status

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
api_instance = esperclient.CommandsV2Api(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
request_id = 'request_id_example' # str | ID for the command request
device = 'device_example' # str | Filter status result by device id. (optional)
state = 'state_example' # str | Filter by command state (optional)

try:
    # get status list for command request
    api_response = api_instance.get_command_request_status(enterprise_id, request_id, device=device, state=state)
    print(api_response)
except ApiException as e:
    print("Exception when calling CommandsV2Api->get_command_request_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 
 **request_id** | [**str**](.md)| ID for the command request | 
 **device** | **str**| Filter status result by device id. | [optional] 
 **state** | **str**| Filter by command state | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_command_history**
> InlineResponse2009 get_device_command_history(enterprise_id, device_id, state=state)

get command history for device

API to get and filter deivce command history

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
api_instance = esperclient.CommandsV2Api(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | Id of the enterprise
device_id = 'device_id_example' # str | Id for the command request
state = 'state_example' # str | Filter by command state (optional)

try:
    # get command history for device
    api_response = api_instance.get_device_command_history(enterprise_id, device_id, state=state)
    print(api_response)
except ApiException as e:
    print("Exception when calling CommandsV2Api->get_device_command_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| Id of the enterprise | 
 **device_id** | [**str**](.md)| Id for the command request | 
 **state** | **str**| Filter by command state | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_command_request**
> InlineResponse2008 list_command_request(enterprise_id, command_type=command_type, devices=devices, device_type=device_type, command=command, issued_by=issued_by)

List command requests

API to get and filter command requests

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
api_instance = esperclient.CommandsV2Api(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
command_type = 'command_type_example' # str | Filter by type of command request i.e device, group etc (optional)
devices = 'devices_example' # str | Filter by device IDs. Accepts comma separated values. (optional)
device_type = 'device_type_example' # str | Filter by device type i.e active, inactive etc (optional)
command = 'command_example' # str | Filter by command name (optional)
issued_by = 'issued_by_example' # str | Filter by user. Accepts user id. (optional)

try:
    # List command requests
    api_response = api_instance.list_command_request(enterprise_id, command_type=command_type, devices=devices, device_type=device_type, command=command, issued_by=issued_by)
    print(api_response)
except ApiException as e:
    print("Exception when calling CommandsV2Api->list_command_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 
 **command_type** | **str**| Filter by type of command request i.e device, group etc | [optional] 
 **devices** | **str**| Filter by device IDs. Accepts comma separated values. | [optional] 
 **device_type** | **str**| Filter by device type i.e active, inactive etc | [optional] 
 **command** | **str**| Filter by command name | [optional] 
 **issued_by** | **str**| Filter by user. Accepts user id. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_command_status**
> V0CommandStatus partial_update_command_status(enterprise_id, request_id, command_id, action, data=data)

Update command status

API to patch the state of command

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
api_instance = esperclient.CommandsV2Api(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
request_id = 'request_id_example' # str | ID for the command request
command_id = 'command_id_example' # str | ID for the command
action = 'action_example' # str | Action to be performed on device
data = esperclient.V0CommandStatusUpdate() # V0CommandStatusUpdate |  (optional)

try:
    # Update command status
    api_response = api_instance.partial_update_command_status(enterprise_id, request_id, command_id, action, data=data)
    print(api_response)
except ApiException as e:
    print("Exception when calling CommandsV2Api->partial_update_command_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 
 **request_id** | [**str**](.md)| ID for the command request | 
 **command_id** | [**str**](.md)| ID for the command | 
 **action** | **str**| Action to be performed on device | 
 **data** | [**V0CommandStatusUpdate**](V0CommandStatusUpdate.md)|  | [optional] 

### Return type

[**V0CommandStatus**](V0CommandStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

