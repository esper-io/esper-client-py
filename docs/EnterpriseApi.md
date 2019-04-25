# esperclient.EnterpriseApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_enterprises**](EnterpriseApi.md#get_all_enterprises) | **GET** /enterprise/ | List all enterprises
[**get_enterprise**](EnterpriseApi.md#get_enterprise) | **GET** /enterprise/{enterprise_id}/ | Get your enteprise information
[**partial_update_enterprise**](EnterpriseApi.md#partial_update_enterprise) | **PATCH** /enterprise/{enterprise_id}/ | Partial update enterprise information


# **get_all_enterprises**
> InlineResponse200 get_all_enterprises()

List all enterprises

Returns Enterprise list

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.EnterpriseApi()

try:
    # List all enterprises
    api_response = api_instance.get_all_enterprises()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApi->get_all_enterprises: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprise**
> Enterprise get_enterprise(enterprise_id)

Get your enteprise information

Returns Enterprise instance

### Example
```python
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.EnterpriseApi()
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.

try:
    # Get your enteprise information
    api_response = api_instance.get_enterprise(enterprise_id)
    pprint(api_response)
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

No authorization required

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
from __future__ import print_function
import time
import esperclient
from esperclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esperclient.EnterpriseApi()
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
data = esperclient.Enterprise() # Enterprise | 

try:
    # Partial update enterprise information
    api_response = api_instance.partial_update_enterprise(enterprise_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApi->partial_update_enterprise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| A UUID string identifying this enterprise. | 
 **data** | [**Enterprise**](Enterprise.md)|  | 

### Return type

[**Enterprise**](Enterprise.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

