# esperclient.EnterprisePolicyApi

All URIs are relative to *https://foo-api.esper.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy**](EnterprisePolicyApi.md#create_policy) | **POST** /enterprise/{enterprise_id}/policy/ | Create a new Enterprise Policy
[**delete_enterprise_policy**](EnterprisePolicyApi.md#delete_enterprise_policy) | **DELETE** /enterprise/{enterprise_id}/policy/{policy_id}/ | Delete a Enterprise Policy
[**get_policy_by_id**](EnterprisePolicyApi.md#get_policy_by_id) | **GET** /enterprise/{enterprise_id}/policy/{policy_id}/ | Get Enterprise Policy
[**list_policies**](EnterprisePolicyApi.md#list_policies) | **GET** /enterprise/{enterprise_id}/policy/ | List all policies in enterprise
[**partialupdate_policy**](EnterprisePolicyApi.md#partialupdate_policy) | **PATCH** /enterprise/{enterprise_id}/policy/{policy_id}/ | Partial update EnterprisePolicy
[**update_policy**](EnterprisePolicyApi.md#update_policy) | **PUT** /enterprise/{enterprise_id}/policy/{policy_id}/ | Update Enterprise Policy


# **create_policy**
> EnterprisePolicy create_policy(enterprise_id, request)

Create a new Enterprise Policy

API to create a new Enterprise Policy

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
api_instance = esperclient.EnterprisePolicyApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
request = esperclient.EnterprisePolicy() # EnterprisePolicy | The request body to create an Enteprise Policy

try:
    # Create a new Enterprise Policy
    api_response = api_instance.create_policy(enterprise_id, request)
    print(api_response)
except ApiException as e:
    print("Exception when calling EnterprisePolicyApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 
 **request** | [**EnterprisePolicy**](EnterprisePolicy.md)| The request body to create an Enteprise Policy | 

### Return type

[**EnterprisePolicy**](EnterprisePolicy.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_enterprise_policy**
> delete_enterprise_policy(policy_id, enterprise_id)

Delete a Enterprise Policy

Emtpy response

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
api_instance = esperclient.EnterprisePolicyApi(esperclient.ApiClient(configuration))
policy_id = 56 # int | An integer identifying this EnterprisePolicy.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Delete a Enterprise Policy
    api_instance.delete_enterprise_policy(policy_id, enterprise_id)
except ApiException as e:
    print("Exception when calling EnterprisePolicyApi->delete_enterprise_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| An integer identifying this EnterprisePolicy. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_by_id**
> EnterprisePolicy get_policy_by_id(policy_id, enterprise_id)

Get Enterprise Policy

Returns EnterprisePolicy instance

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
api_instance = esperclient.EnterprisePolicyApi(esperclient.ApiClient(configuration))
policy_id = 56 # int | An integer identifying this EnterprisePolicy.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Get Enterprise Policy
    api_response = api_instance.get_policy_by_id(policy_id, enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling EnterprisePolicyApi->get_policy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| An integer identifying this EnterprisePolicy. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

[**EnterprisePolicy**](EnterprisePolicy.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policies**
> InlineResponse2008 list_policies(enterprise_id, name=name, is_active=is_active, limit=limit, offset=offset)

List all policies in enterprise

Returns Policies list

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
api_instance = esperclient.EnterprisePolicyApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
name = 'name_example' # str | filter by policy name (optional)
is_active = true # bool | filter by Active policies (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 0 # int | The initial index from which to return the results. (optional) (default to 0)

try:
    # List all policies in enterprise
    api_response = api_instance.list_policies(enterprise_id, name=name, is_active=is_active, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling EnterprisePolicyApi->list_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| ID of the enterprise | 
 **name** | **str**| filter by policy name | [optional] 
 **is_active** | **bool**| filter by Active policies | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] [default to 0]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partialupdate_policy**
> EnterprisePolicy partialupdate_policy(policy_id, enterprise_id, data)

Partial update EnterprisePolicy

Returns EnterprisePolicy instance

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
api_instance = esperclient.EnterprisePolicyApi(esperclient.ApiClient(configuration))
policy_id = 56 # int | An integer identifying this EnterprisePolicy.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
data = esperclient.EnterprisePolicyPartialUpdate() # EnterprisePolicyPartialUpdate | 

try:
    # Partial update EnterprisePolicy
    api_response = api_instance.partialupdate_policy(policy_id, enterprise_id, data)
    print(api_response)
except ApiException as e:
    print("Exception when calling EnterprisePolicyApi->partialupdate_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| An integer identifying this EnterprisePolicy. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **data** | [**EnterprisePolicyPartialUpdate**](EnterprisePolicyPartialUpdate.md)|  | 

### Return type

[**EnterprisePolicy**](EnterprisePolicy.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> EnterprisePolicy update_policy(policy_id, enterprise_id, data)

Update Enterprise Policy

Returns Enterprise Policy instance

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
api_instance = esperclient.EnterprisePolicyApi(esperclient.ApiClient(configuration))
policy_id = 56 # int | An integer identifying this EnterprisePolicy.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
data = esperclient.EnterprisePolicy() # EnterprisePolicy | 

try:
    # Update Enterprise Policy
    api_response = api_instance.update_policy(policy_id, enterprise_id, data)
    print(api_response)
except ApiException as e:
    print("Exception when calling EnterprisePolicyApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| An integer identifying this EnterprisePolicy. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **data** | [**EnterprisePolicy**](EnterprisePolicy.md)|  | 

### Return type

[**EnterprisePolicy**](EnterprisePolicy.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

