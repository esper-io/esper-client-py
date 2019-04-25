# esperclient.DeviceCommandsApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_command**](DeviceCommandsApi.md#get_device_command) | **GET** /v0/device-command/{command_id}/ | Get command information
[**lock_device**](DeviceCommandsApi.md#lock_device) | **POST** /v0/device-command/lock/ | Lock a device
[**reboot_device**](DeviceCommandsApi.md#reboot_device) | **POST** /v0/device-command/reboot/ | Reboot a device


# **get_device_command**
> DeviceCommand get_device_command(command_id)

Get command information

Returns DeviceCommand instance

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.DeviceCommandsApi()
command_id = 'command_id_example' # str | A UUID string identifying this device command.

try:
    # Get command information
    api_response = api_instance.get_device_command(command_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceCommandsApi->get_device_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | [**str**](.md)| A UUID string identifying this device command. | 

### Return type

[**DeviceCommand**](DeviceCommand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_device**
> DeviceCommand lock_device(data)

Lock a device

Creates DeviceCommand instance

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.DeviceCommandsApi()
data = esperclient.DeviceCommandRequest() # DeviceCommandRequest | 

try:
    # Lock a device
    api_response = api_instance.lock_device(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceCommandsApi->lock_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DeviceCommandRequest**](DeviceCommandRequest.md)|  | 

### Return type

[**DeviceCommand**](DeviceCommand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reboot_device**
> DeviceCommand reboot_device(data)

Reboot a device

Creates DeviceCommand instance

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.DeviceCommandsApi()
data = esperclient.DeviceCommandRequest() # DeviceCommandRequest | 

try:
    # Reboot a device
    api_response = api_instance.reboot_device(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceCommandsApi->reboot_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DeviceCommandRequest**](DeviceCommandRequest.md)|  | 

### Return type

[**DeviceCommand**](DeviceCommand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

