# esperclient.EnterpriseApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_enterprises**](EnterpriseApi.md#get_all_enterprises) | **GET** /enterprise/ | List all enterprises
[**get_enterprise**](EnterpriseApi.md#get_enterprise) | **GET** /enterprise/{enterprise_id}/ | Get your enterprise information
[**partial_update_enterprise**](EnterpriseApi.md#partial_update_enterprise) | **PATCH** /enterprise/{enterprise_id}/ | Partial update enterprise information


# **get_all_enterprises**
> InlineResponse200 get_all_enterprises()

List all enterprises

Returns Enterprise list

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
api_instance = esperclient.EnterpriseApi(esperclient.ApiClient(configuration))

try:
    # List all enterprises
    api_response = api_instance.get_all_enterprises()
    print(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApi->get_all_enterprises: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprise**
> Enterprise get_enterprise(enterprise_id)

Get your enterprise information

Returns Enterprise instance

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
api_instance = esperclient.EnterpriseApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.

try:
    # Get your enterprise information
    api_response = api_instance.get_enterprise(enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApi->get_enterprise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| A UUID string identifying this enterprise. | 

### Return type

[**Enterprise**](Enterprise.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_enterprise**
> Enterprise partial_update_enterprise(enterprise_id, data)

Partial update enterprise information

Returns updated enterprise

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
api_instance = esperclient.EnterpriseApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
data = esperclient.EnterpriseUpdate() # EnterpriseUpdate | 

try:
    # Partial update enterprise information
    api_response = api_instance.partial_update_enterprise(enterprise_id, data)
    print(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApi->partial_update_enterprise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| A UUID string identifying this enterprise. | 
 **data** | [**EnterpriseUpdate**](EnterpriseUpdate.md)|  | 

### Return type

[**Enterprise**](Enterprise.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

