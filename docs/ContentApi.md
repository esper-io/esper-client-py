# esperclient.ContentApi

All URIs are relative to *https://foo-api.esper.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_content**](ContentApi.md#delete_content) | **DELETE** /v0/enterprise/{enterprise_id}/content/{content_id}/ | Delete Content
[**get_all_content**](ContentApi.md#get_all_content) | **GET** /v0/enterprise/{enterprise_id}/content/ | List content in the enterprise
[**get_content**](ContentApi.md#get_content) | **GET** /v0/enterprise/{enterprise_id}/content/{content_id}/ | Get content information
[**patch_content**](ContentApi.md#patch_content) | **PATCH** /v0/enterprise/{enterprise_id}/content/{content_id}/ | Patch a content instance
[**post_content**](ContentApi.md#post_content) | **POST** /v0/enterprise/{enterprise_id}/content/upload/ | Upload new content


# **delete_content**
> delete_content(content_id, enterprise_id)

Delete Content

Empty response

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
api_instance = esperclient.ContentApi(esperclient.ApiClient(configuration))
content_id = 'content_id_example' # str | A UUID string identifying a content instance.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Delete Content
    api_instance.delete_content(content_id, enterprise_id)
except ApiException as e:
    print("Exception when calling ContentApi->delete_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | [**str**](.md)| A UUID string identifying a content instance. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_content**
> InlineResponse20011 get_all_content(enterprise_id, search=search, limit=limit, offset=offset)

List content in the enterprise

Returns Content list

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
api_instance = esperclient.ContentApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
search = 'search_example' # str | Seach by tags, description (optional)
limit = 20 # int | Number of results to return per page. (optional) (default to 20)
offset = 0 # int | The initial index from which to return the results. (optional) (default to 0)

try:
    # List content in the enterprise
    api_response = api_instance.get_all_content(enterprise_id, search=search, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->get_all_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying this enterprise. | 
 **search** | **str**| Seach by tags, description | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] [default to 20]
 **offset** | **int**| The initial index from which to return the results. | [optional] [default to 0]

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content**
> Content get_content(content_id, enterprise_id)

Get content information

Returns Content instance

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
api_instance = esperclient.ContentApi(esperclient.ApiClient(configuration))
content_id = 'content_id_example' # str | A UUID string identifying a content instance.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Get content information
    api_response = api_instance.get_content(content_id, enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->get_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | [**str**](.md)| A UUID string identifying a content instance. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 

### Return type

[**Content**](Content.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_content**
> Content patch_content(content_id, enterprise_id, data=data)

Patch a content instance

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
api_instance = esperclient.ContentApi(esperclient.ApiClient(configuration))
content_id = 'content_id_example' # str | A UUID string identifying a content instance.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.
data = esperclient.Data() # Data |  (optional)

try:
    # Patch a content instance
    api_response = api_instance.patch_content(content_id, enterprise_id, data=data)
    print(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->patch_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | [**str**](.md)| A UUID string identifying a content instance. | 
 **enterprise_id** | **str**| A UUID string identifying enterprise. | 
 **data** | [**Data**](Data.md)|  | [optional] 

### Return type

[**Content**](Content.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content**
> Content post_content(enterprise_id, app_file)

Upload new content

Returns Content instance

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
api_instance = esperclient.ContentApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying this enterprise.
app_file = '/path/to/file.txt' # file | Valid file to upload

try:
    # Upload new content
    api_response = api_instance.post_content(enterprise_id, app_file)
    print(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->post_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | **str**| A UUID string identifying this enterprise. | 
 **app_file** | **file**| Valid file to upload | 

### Return type

[**Content**](Content.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

