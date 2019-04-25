# esperclient.PolicyApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy**](PolicyApi.md#create_policy) | **POST** /enterprise/{enterprise_id}/policy/ | Create a policy
[**delete_policy**](PolicyApi.md#delete_policy) | **DELETE** /enterprise/{enterprise_id}/policy/{policy_id}/ | Delete a policy
[**get_all_policies**](PolicyApi.md#get_all_policies) | **GET** /enterprise/{enterprise_id}/policy/ | List enterprise policies
[**get_policy_by_id**](PolicyApi.md#get_policy_by_id) | **GET** /enterprise/{enterprise_id}/policy/{policy_id}/ | Get policy details
[**partial_update_policy**](PolicyApi.md#partial_update_policy) | **PATCH** /enterprise/{enterprise_id}/policy/{policy_id}/ | Partial update policy
[**update_policy**](PolicyApi.md#update_policy) | **PUT** /enterprise/{enterprise_id}/policy/{policy_id}/ | Update/Replace information


# **create_policy**
> EnterprisePolicy create_policy(enterprise_id, data)

Create a policy

Return EnterprisePolicy instance

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.PolicyApi()
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
data = esperclient.EnterprisePolicy() # EnterprisePolicy | 

try:
    # Create a policy
    api_response = api_instance.create_policy(enterprise_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **data** | [**EnterprisePolicy**](EnterprisePolicy.md)|  | 

### Return type

[**EnterprisePolicy**](EnterprisePolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(policy_id, enterprise_id)

Delete a policy

Empty response

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.PolicyApi()
policy_id = 56 # int | A unique integer value identifying this enterprise policy.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Delete a policy
    api_instance.delete_policy(policy_id, enterprise_id)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| A unique integer value identifying this enterprise policy. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_policies**
> InlineResponse2008 get_all_policies(enterprise_id, name=name, limit=limit, offset=offset)

List enterprise policies

Returns EnterprisePolicy list

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.PolicyApi()
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
name = 'name_example' # str | filter by name (starts with) (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # List enterprise policies
    api_response = api_instance.get_all_policies(enterprise_id, name=name, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_all_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **name** | **str**| filter by name (starts with) | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_by_id**
> EnterprisePolicy get_policy_by_id(policy_id, enterprise_id)

Get policy details

Returns EnterprisePolicy instance

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.PolicyApi()
policy_id = 56 # int | A unique integer value identifying this enterprise policy.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Get policy details
    api_response = api_instance.get_policy_by_id(policy_id, enterprise_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| A unique integer value identifying this enterprise policy. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

[**EnterprisePolicy**](EnterprisePolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_policy**
> EnterprisePolicy partial_update_policy(policy_id, enterprise_id, data)

Partial update policy

Returns updated policy

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.PolicyApi()
policy_id = 56 # int | A unique integer value identifying this enterprise policy.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
data = esperclient.EnterprisePolicy() # EnterprisePolicy | 

try:
    # Partial update policy
    api_response = api_instance.partial_update_policy(policy_id, enterprise_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->partial_update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| A unique integer value identifying this enterprise policy. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **data** | [**EnterprisePolicy**](EnterprisePolicy.md)|  | 

### Return type

[**EnterprisePolicy**](EnterprisePolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> EnterprisePolicy update_policy(policy_id, enterprise_id, data)

Update/Replace information

Returns updated policy

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.PolicyApi()
policy_id = 56 # int | A unique integer value identifying this enterprise policy.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
data = esperclient.EnterprisePolicy() # EnterprisePolicy | 

try:
    # Update/Replace information
    api_response = api_instance.update_policy(policy_id, enterprise_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| A unique integer value identifying this enterprise policy. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **data** | [**EnterprisePolicy**](EnterprisePolicy.md)|  | 

### Return type

[**EnterprisePolicy**](EnterprisePolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

