# esperclient.TokenApi

All URIs are relative to *https://foo-api.esper.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token_info**](TokenApi.md#get_token_info) | **GET** /v1/token-info/ | Token Information
[**renew_token**](TokenApi.md#renew_token) | **GET** /v0/enterprise/{enterprise_id}/developerapp/{developerapp_id}/renew-token/ | Renew Token


# **get_token_info**
> TokenInfoV1 get_token_info()

Token Information

API to get resource information associated with your token like your enterprise, user etc

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
api_instance = esperclient.TokenApi(esperclient.ApiClient(configuration))

try:
    # Token Information
    api_response = api_instance.get_token_info()
    print(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->get_token_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenInfoV1**](TokenInfoV1.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_token**
> TokenRenewV0 renew_token(enterprise_id, developerapp_id, access_token)

Renew Token

API to renew your token

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
api_instance = esperclient.TokenApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
developerapp_id = 'developerapp_id_example' # str | A UUID string identifying the developerapp
access_token = 'access_token_example' # str | Token to be renewed

try:
    # Renew Token
    api_response = api_instance.renew_token(enterprise_id, developerapp_id, access_token)
    print(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->renew_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| A UUID string identifying this enterprise. | 
 **developerapp_id** | [**str**](.md)| A UUID string identifying the developerapp | 
 **access_token** | **str**| Token to be renewed | 

### Return type

[**TokenRenewV0**](TokenRenewV0.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

