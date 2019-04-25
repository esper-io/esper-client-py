# esperclient.EnterpriseApplicationApi

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload**](EnterpriseApplicationApi.md#upload) | **POST** /enterprise/{enterprise_id}/application/upload/ | upload an application to enterprise


# **upload**
> InlineResponse201 upload(enterprise_id, enterprise, app_file)

upload an application to enterprise

Returns application

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
api_instance = esperclient.EnterpriseApplicationApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
enterprise = 'enterprise_example' # str | enterprise id
app_file = '/path/to/file.txt' # file | valid APK file

try:
    # upload an application to enterprise
    api_response = api_instance.upload(enterprise_id, enterprise, app_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterpriseApplicationApi->upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying this enterprise. | 
 **enterprise** | [**str**](.md)| enterprise id | 
 **app_file** | **file**| valid APK file | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[basic_security](../README.md#basic_security)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

