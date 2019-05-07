# esperclient.DeviceGroupApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](DeviceGroupApi.md#create_group) | **POST** /enterprise/{enterprise_id}/devicegroup/ | Create a device group
[**delete_group**](DeviceGroupApi.md#delete_group) | **DELETE** /enterprise/{enterprise_id}/devicegroup/{group_id}/ | Delete a device group
[**get_all_groups**](DeviceGroupApi.md#get_all_groups) | **GET** /enterprise/{enterprise_id}/devicegroup/ | List device groups
[**get_group_by_id**](DeviceGroupApi.md#get_group_by_id) | **GET** /enterprise/{enterprise_id}/devicegroup/{group_id}/ | Get device group information
[**partial_update_group**](DeviceGroupApi.md#partial_update_group) | **PATCH** /enterprise/{enterprise_id}/devicegroup/{group_id}/ | Partial update group
[**update_group**](DeviceGroupApi.md#update_group) | **PUT** /enterprise/{enterprise_id}/devicegroup/{group_id}/ | Update device group


# **create_group**
> DeviceGroup create_group(enterprise_id, data)

Create a device group

Returns EnterpriseDeviceGroup instance

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
api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
data = esperclient.DeviceGroup() # DeviceGroup | 

try:
    # Create a device group
    api_response = api_instance.create_group(enterprise_id, data)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **data** | [**DeviceGroup**](DeviceGroup.md)|  | 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id, enterprise_id)

Delete a device group

Emtpy response

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
api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))
group_id = 'group_id_example' # str | A UUID string identifying this enterprise device group.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Delete a device group
    api_instance.delete_group(group_id, enterprise_id)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| A UUID string identifying this enterprise device group. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_groups**
> InlineResponse2006 get_all_groups(enterprise_id, name=name, limit=limit, offset=offset)

List device groups

Returns EnterpriseDeviceGroup list

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
api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
name = 'name_example' # str | filter by group name (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # List device groups
    api_response = api_instance.get_all_groups(enterprise_id, name=name, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->get_all_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **name** | **str**| filter by group name | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_by_id**
> DeviceGroup get_group_by_id(group_id, enterprise_id)

Get device group information

Returns EnterpriseDeviceGroup instance

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
api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))
group_id = 'group_id_example' # str | A UUID string identifying this enterprise device group.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Get device group information
    api_response = api_instance.get_group_by_id(group_id, enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->get_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| A UUID string identifying this enterprise device group. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_group**
> DeviceGroup partial_update_group(group_id, enterprise_id, data)

Partial update group

Returns EnterpriseDeviceGroup instance

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
api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))
group_id = 'group_id_example' # str | A UUID string identifying this enterprise device group.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
data = esperclient.DeviceGroupUpdate() # DeviceGroupUpdate | 

try:
    # Partial update group
    api_response = api_instance.partial_update_group(group_id, enterprise_id, data)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->partial_update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| A UUID string identifying this enterprise device group. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **data** | [**DeviceGroupUpdate**](DeviceGroupUpdate.md)|  | 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> DeviceGroup update_group(group_id, enterprise_id, data)

Update device group

Returns EnterpriseDeviceGroup instance

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
api_instance = esperclient.DeviceGroupApi(esperclient.ApiClient(configuration))
group_id = 'group_id_example' # str | A UUID string identifying this enterprise device group.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
data = esperclient.DeviceGroupUpdate() # DeviceGroupUpdate | 

try:
    # Update device group
    api_response = api_instance.update_group(group_id, enterprise_id, data)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)| A UUID string identifying this enterprise device group. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **data** | [**DeviceGroupUpdate**](DeviceGroupUpdate.md)|  | 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

