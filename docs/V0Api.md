# esperclient.V0Api

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_command**](V0Api.md#get_device_command) | **GET** /v0/device-command/{command_id}/ | Get command information
[**get_group_command**](V0Api.md#get_group_command) | **GET** /v0/group-command/{command_id}/ | Get command information
[**install_device_app**](V0Api.md#install_device_app) | **POST** /v0/device-command/install/ | Install an app on device
[**lock_device**](V0Api.md#lock_device) | **POST** /v0/device-command/lock/ | Lock a device
[**lock_group**](V0Api.md#lock_group) | **POST** /v0/group-command/lock/ | Lock devices in a group
[**reboot_device**](V0Api.md#reboot_device) | **POST** /v0/device-command/reboot/ | Reboot a device
[**reboot_group**](V0Api.md#reboot_group) | **POST** /v0/group-command/reboot/ | Reboot devices in a group


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
api_instance = esperclient.V0Api()
command_id = 'command_id_example' # str | A UUID string identifying this device command.

try:
    # Get command information
    api_response = api_instance.get_device_command(command_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V0Api->get_device_command: %s\n" % e)
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

# Configure HTTP basic authorization: basic_security
configuration = esperclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esperclient.V0Api(esperclient.ApiClient(configuration))
command_id = 'command_id_example' # str | A UUID string identifying this device group command.

try:
    # Get command information
    api_response = api_instance.get_group_command(command_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V0Api->get_group_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | [**str**](.md)| A UUID string identifying this device group command. | 

### Return type

[**GroupCommand**](GroupCommand.md)

### Authorization

[basic_security](../README.md#basic_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_device_app**
> DeviceCommand install_device_app(data)

Install an app on device

Creates DeviceCommand instance

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
api_instance = esperclient.V0Api(esperclient.ApiClient(configuration))
data = esperclient.DeviceCommandRequest() # DeviceCommandRequest | 

try:
    # Install an app on device
    api_response = api_instance.install_device_app(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V0Api->install_device_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DeviceCommandRequest**](DeviceCommandRequest.md)|  | 

### Return type

[**DeviceCommand**](DeviceCommand.md)

### Authorization

[basic_security](../README.md#basic_security)

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

# Configure HTTP basic authorization: basic_security
configuration = esperclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esperclient.V0Api(esperclient.ApiClient(configuration))
data = esperclient.DeviceCommandRequest() # DeviceCommandRequest | 

try:
    # Lock a device
    api_response = api_instance.lock_device(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V0Api->lock_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DeviceCommandRequest**](DeviceCommandRequest.md)|  | 

### Return type

[**DeviceCommand**](DeviceCommand.md)

### Authorization

[basic_security](../README.md#basic_security)

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

# Configure HTTP basic authorization: basic_security
configuration = esperclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esperclient.V0Api(esperclient.ApiClient(configuration))
data = esperclient.GroupCommandRequest() # GroupCommandRequest | 

try:
    # Lock devices in a group
    api_response = api_instance.lock_group(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V0Api->lock_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**GroupCommandRequest**](GroupCommandRequest.md)|  | 

### Return type

[**GroupCommand**](GroupCommand.md)

### Authorization

[basic_security](../README.md#basic_security)

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

# Configure HTTP basic authorization: basic_security
configuration = esperclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esperclient.V0Api(esperclient.ApiClient(configuration))
data = esperclient.DeviceCommandRequest() # DeviceCommandRequest | 

try:
    # Reboot a device
    api_response = api_instance.reboot_device(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V0Api->reboot_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DeviceCommandRequest**](DeviceCommandRequest.md)|  | 

### Return type

[**DeviceCommand**](DeviceCommand.md)

### Authorization

[basic_security](../README.md#basic_security)

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

# Configure HTTP basic authorization: basic_security
configuration = esperclient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esperclient.V0Api(esperclient.ApiClient(configuration))
data = esperclient.GroupCommandRequest() # GroupCommandRequest | 

try:
    # Reboot devices in a group
    api_response = api_instance.reboot_group(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V0Api->reboot_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**GroupCommandRequest**](GroupCommandRequest.md)|  | 

### Return type

[**GroupCommand**](GroupCommand.md)

### Authorization

[basic_security](../README.md#basic_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

