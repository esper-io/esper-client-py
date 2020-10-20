# esperclient.GeofenceApi

All URIs are relative to *https://foo-api.esper.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_geofence**](GeofenceApi.md#create_geofence) | **POST** /v0/enterprise/{enterprise_id}/geofence/ | Create a geofence
[**delete_geofence**](GeofenceApi.md#delete_geofence) | **DELETE** /v0/enterprise/{enterprise_id}/geofence/{geofence_id}/ | Delete a geofence
[**get_all_geofences**](GeofenceApi.md#get_all_geofences) | **GET** /v0/enterprise/{enterprise_id}/geofence/ | List Geofences in Enterprise
[**get_geofence**](GeofenceApi.md#get_geofence) | **GET** /v0/enterprise/{enterprise_id}/geofence/{geofence_id}/ | Get geofence information
[**partial_update_geofence**](GeofenceApi.md#partial_update_geofence) | **PATCH** /v0/enterprise/{enterprise_id}/geofence/{geofence_id}/ | Partially updates geofence information
[**update_geofence**](GeofenceApi.md#update_geofence) | **PUT** /v0/enterprise/{enterprise_id}/geofence/{geofence_id}/ | Update geofence information


# **create_geofence**
> Geofence create_geofence(data, enterprise_id)

Create a geofence

Returns Geofence instance

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
api_instance = esperclient.GeofenceApi(esperclient.ApiClient(configuration))
data = esperclient.Geofence() # Geofence | 
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying the enterprise.

try:
    # Create a geofence
    api_response = api_instance.create_geofence(data, enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling GeofenceApi->create_geofence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Geofence**](Geofence.md)|  | 
 **enterprise_id** | [**str**](.md)| A UUID string identifying the enterprise. | 

### Return type

[**Geofence**](Geofence.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_geofence**
> delete_geofence(geofence_id, enterprise_id)

Delete a geofence

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
api_instance = esperclient.GeofenceApi(esperclient.ApiClient(configuration))
geofence_id = 'geofence_id_example' # str | A UUID string identifying the geofence.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying the enterprise.

try:
    # Delete a geofence
    api_instance.delete_geofence(geofence_id, enterprise_id)
except ApiException as e:
    print("Exception when calling GeofenceApi->delete_geofence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | [**str**](.md)| A UUID string identifying the geofence. | 
 **enterprise_id** | [**str**](.md)| A UUID string identifying the enterprise. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_geofences**
> InlineResponse20012 get_all_geofences(enterprise_id, search=search, limit=limit, offset=offset)

List Geofences in Enterprise

API to view all the geofences in an enterprise

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
api_instance = esperclient.GeofenceApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying the enterprise.
search = 'search_example' # str | A search term. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # List Geofences in Enterprise
    api_response = api_instance.get_all_geofences(enterprise_id, search=search, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling GeofenceApi->get_all_geofences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| A UUID string identifying the enterprise. | 
 **search** | **str**| A search term. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_geofence**
> Geofence get_geofence(geofence_id, enterprise_id)

Get geofence information

Returns geofence instance

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
api_instance = esperclient.GeofenceApi(esperclient.ApiClient(configuration))
geofence_id = 'geofence_id_example' # str | A UUID string identifying the geofence.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying the enterprise.

try:
    # Get geofence information
    api_response = api_instance.get_geofence(geofence_id, enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling GeofenceApi->get_geofence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | [**str**](.md)| A UUID string identifying the geofence. | 
 **enterprise_id** | [**str**](.md)| A UUID string identifying the enterprise. | 

### Return type

[**Geofence**](Geofence.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_geofence**
> Geofence partial_update_geofence(geofence_id, enterprise_id, data)

Partially updates geofence information

Returns geofence instance

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
api_instance = esperclient.GeofenceApi(esperclient.ApiClient(configuration))
geofence_id = 'geofence_id_example' # str | A UUID string identifying the geofence.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying the enterprise.
data = esperclient.GeofenceUpdate() # GeofenceUpdate | 

try:
    # Partially updates geofence information
    api_response = api_instance.partial_update_geofence(geofence_id, enterprise_id, data)
    print(api_response)
except ApiException as e:
    print("Exception when calling GeofenceApi->partial_update_geofence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | [**str**](.md)| A UUID string identifying the geofence. | 
 **enterprise_id** | [**str**](.md)| A UUID string identifying the enterprise. | 
 **data** | [**GeofenceUpdate**](GeofenceUpdate.md)|  | 

### Return type

[**Geofence**](Geofence.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_geofence**
> Geofence update_geofence(geofence_id, enterprise_id, data)

Update geofence information

Returns geofence instance

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
api_instance = esperclient.GeofenceApi(esperclient.ApiClient(configuration))
geofence_id = 'geofence_id_example' # str | A UUID string identifying the geofence.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying the enterprise.
data = esperclient.Geofence() # Geofence | 

try:
    # Update geofence information
    api_response = api_instance.update_geofence(geofence_id, enterprise_id, data)
    print(api_response)
except ApiException as e:
    print("Exception when calling GeofenceApi->update_geofence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | [**str**](.md)| A UUID string identifying the geofence. | 
 **enterprise_id** | [**str**](.md)| A UUID string identifying the enterprise. | 
 **data** | [**Geofence**](Geofence.md)|  | 

### Return type

[**Geofence**](Geofence.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

