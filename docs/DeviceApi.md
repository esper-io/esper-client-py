# esperclient.DeviceApi

All URIs are relative to *https://foo-api.esper.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_devices**](DeviceApi.md#get_all_devices) | **GET** /enterprise/{enterprise_id}/device/ | Fetch all devices in an enterprise
[**get_app_installs**](DeviceApi.md#get_app_installs) | **GET** /enterprise/{enterprise_id}/device/{device_id}/install/ | List installed apps
[**get_device_app_by_id**](DeviceApi.md#get_device_app_by_id) | **GET** /enterprise/{enterprise_id}/device/{device_id}/app/{app_id}/ | Get device app details
[**get_device_apps**](DeviceApi.md#get_device_apps) | **GET** /enterprise/{enterprise_id}/device/{device_id}/app/ | List all device apps
[**get_device_by_id**](DeviceApi.md#get_device_by_id) | **GET** /enterprise/{enterprise_id}/device/{device_id}/ | Fetch device details by ID
[**get_device_event**](DeviceApi.md#get_device_event) | **GET** /enterprise/{enterprise_id}/device/{device_id}/status/ | Get latest device event


# **get_all_devices**
> InlineResponse2003 get_all_devices(enterprise_id, name=name, group=group, imei=imei, serial=serial, state=state, brand=brand, is_gms=is_gms, search=search, tags=tags, limit=limit, offset=offset)

Fetch the data for all devices in an Enterprise from Esper's cloud servers.

Returns a list of Device objects, containing device state data retrieved from Esper servers.

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
api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
name = 'name_example' # str | Filter by device name (optional)
group = 'group_example' # str | Filter by group id (optional)
imei = 'imei_example' # str | filter by imei (optional)
serial = 'serial_example' # str | filter by serial number (optional)
state = 56 # int | filter by device state (optional)
brand = 'brand_example' # str | filter by brand (optional)
is_gms = true # bool | filter for gms devices (optional)
search = 'search_example' # str | A search term. Search by device name, imei or mac address (optional)
tags = 'tags_example' # str | A partial text search for device tags (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 0 # int | The initial index from which to return the results. (optional) (default to 0)

try:
    # Fetch all devices in an enterprise
    api_response = api_instance.get_all_devices(enterprise_id, name=name, group=group, imei=imei, serial=serial, state=state, brand=brand, is_gms=is_gms, search=search, tags=tags, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_all_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 
 **name** | **str**| Filter by device name | [optional] 
 **group** | [**str**](.md)| Filter by group id | [optional] 
 **imei** | **str**| filter by imei | [optional] 
 **serial** | **str**| filter by serial number | [optional] 
 **state** | **int**| filter by device state | [optional] 
 **brand** | **str**| filter by brand | [optional] 
 **is_gms** | **bool**| filter for gms devices | [optional] 
 **search** | **str**| A search term. Search by device name, imei or mac address | [optional] 
 **tags** | **str**| A partial text search for device tags | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] [default to 0]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_installs**
> InlineResponse2005 get_app_installs(enterprise_id, device_id, device=device, package_name=package_name, application_name=application_name, install_state=install_state, limit=limit, offset=offset)

Fetch a list all of the apps which are installed on a single device.

Returns a list of AppInstall objects.

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
api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
device_id = 'device_id_example' # str | A UUID string identifying device.
device = 'device_example' # str | filter by device id (optional)
package_name = 'package_name_example' # str | filter by package name (optional)
application_name = 'application_name_example' # str | filter by application name (optional)
install_state = 'install_state_example' # str | filter by install state (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 0 # int | The initial index from which to return the results. (optional) (default to 0)

try:
    # List installed apps
    api_response = api_instance.get_app_installs(enterprise_id, device_id, device=device, package_name=package_name, application_name=application_name, install_state=install_state, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_app_installs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying this enterprise. | 
 **device_id** | **str**| A UUID string identifying device. | 
 **device** | **str**| filter by device id | [optional] 
 **package_name** | **str**| filter by package name | [optional] 
 **application_name** | **str**| filter by application name | [optional] 
 **install_state** | **str**| filter by install state | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] [default to 0]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_app_by_id**
> DeviceApp get_device_app_by_id(app_id, enterprise_id, device_id)

Fetch the details of a specified app (which may or may not be installed) associated with a specified device.

Returns a DeviceApp object containing the app details.

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
api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
app_id = 'app_id_example' # str | A UUID string identifying this device app.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this device.
device_id = 'device_id_example' # str | A UUID string identifying this enteprise.

try:
    # Get device app details
    api_response = api_instance.get_device_app_by_id(app_id, enterprise_id, device_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_device_app_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | [**str**](.md)| A UUID string identifying this device app. | 
 **enterprise_id** | **str**| A UUID string identifying this device. | 
 **device_id** | **str**| A UUID string identifying this enteprise. | 

### Return type

[**DeviceApp**](DeviceApp.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_apps**
> InlineResponse2004 get_device_apps(enterprise_id, device_id, package_name=package_name, whitelisted=whitelisted, search=search, limit=limit, offset=offset)

Fetch a list of all apps (installed or not) associated with a specified device.

Returns a list of DeviceApp objects.

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
api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
device_id = 'device_id_example' # str | A UUID string identifying device.
package_name = 'package_name_example' # str | Filter by Package name (optional)
whitelisted = 'whitelisted_example' # str | Whitelist filter (optional)
search = 'search_example' # str | A search term. Search by app_name. (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # List all device apps
    api_response = api_instance.get_device_apps(enterprise_id, device_id, package_name=package_name, whitelisted=whitelisted, search=search, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_device_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying this enterprise. | 
 **device_id** | **str**| A UUID string identifying device. | 
 **package_name** | **str**| Filter by Package name | [optional] 
 **whitelisted** | **str**| Whitelist filter | [optional] 
 **search** | **str**| A search term. Search by app_name. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_id**
> Device get_device_by_id(enterprise_id, device_id)

Fetch device details based on a specified device ID.

Returns a single Device object.

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
api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
device_id = 'device_id_example' # str | ID of the device

try:
    # Fetch device details by ID
    api_response = api_instance.get_device_by_id(enterprise_id, device_id)
    print(api_response)
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

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_event**
> InlineResponse2006 get_device_event(enterprise_id, device_id, latest_event)

Fetch the latest registered device event from the Esper cloud servers, for one specified device.

Returns a list of DeviceStatus objects.

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
api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
device_id = 'device_id_example' # str | A UUID string identifying device.
latest_event = 56 # int | Flag to get latest event

try:
    # Get latest device event
    api_response = api_instance.get_device_event(enterprise_id, device_id, latest_event)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_device_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying this enterprise. | 
 **device_id** | **str**| A UUID string identifying device. | 
 **latest_event** | **int**| Flag to get latest event | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

