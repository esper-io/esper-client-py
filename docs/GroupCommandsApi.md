# esperclient.GroupCommandsApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_group_command**](GroupCommandsApi.md#get_group_command) | **GET** /v0/group-command/{command_id}/ | Get command information
[**lock_group**](GroupCommandsApi.md#lock_group) | **POST** /v0/group-command/lock/ | Lock devices in a group
[**reboot_group**](GroupCommandsApi.md#reboot_group) | **POST** /v0/group-command/reboot/ | Reboot devices in a group


# **get_group_command**
> GroupCommand get_group_command(command_id)

Get command information

Returns GroupCommand instance

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.GroupCommandsApi()
command_id = 'command_id_example' # str | A UUID string identifying this device group command.

try:
    # Get command information
    api_response = api_instance.get_group_command(command_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupCommandsApi->get_group_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | [**str**](.md)| A UUID string identifying this device group command. | 

### Return type

[**GroupCommand**](GroupCommand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_group**
> GroupCommand lock_group(data)

Lock devices in a group

Creates GroupCommand instance

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.GroupCommandsApi()
data = esperclient.GroupCommandRequest() # GroupCommandRequest | 

try:
    # Lock devices in a group
    api_response = api_instance.lock_group(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupCommandsApi->lock_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**GroupCommandRequest**](GroupCommandRequest.md)|  | 

### Return type

[**GroupCommand**](GroupCommand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reboot_group**
> GroupCommand reboot_group(data)

Reboot devices in a group

Creates GroupCommand instance

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.GroupCommandsApi()
data = esperclient.GroupCommandRequest() # GroupCommandRequest | 

try:
    # Reboot devices in a group
    api_response = api_instance.reboot_group(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupCommandsApi->reboot_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**GroupCommandRequest**](GroupCommandRequest.md)|  | 

### Return type

[**GroupCommand**](GroupCommand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

