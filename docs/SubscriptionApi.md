# esperclient.SubscriptionApi

All URIs are relative to *https://foo-api.esper.cloud/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](SubscriptionApi.md#create_subscription) | **POST** /v0/enterprise/{enterprise_id}/subscription/ | Create a Subscription
[**delete_subscription**](SubscriptionApi.md#delete_subscription) | **DELETE** /v0/enterprise/{enterprise_id}/subscription/{subscription_id}/ | Delete a subscription
[**get_all_subscriptions**](SubscriptionApi.md#get_all_subscriptions) | **GET** /v0/enterprise/{enterprise_id}/subscription/ | List Subscriptions in Enterprise
[**get_subscription**](SubscriptionApi.md#get_subscription) | **GET** /v0/enterprise/{enterprise_id}/subscription/{subscription_id}/ | Get subscription information


# **create_subscription**
> EventSubscription create_subscription(data, enterprise_id)

Create a Subscription

Returns Subscription instance

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
api_instance = esperclient.SubscriptionApi(esperclient.ApiClient(configuration))
data = esperclient.EventSubscriptionArgs() # EventSubscriptionArgs | 
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying the enterprise.

try:
    # Create a Subscription
    api_response = api_instance.create_subscription(data, enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**EventSubscriptionArgs**](EventSubscriptionArgs.md)|  | 
 **enterprise_id** | [**str**](.md)| A UUID string identifying the enterprise. | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(subscription_id, enterprise_id)

Delete a subscription

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
api_instance = esperclient.SubscriptionApi(esperclient.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | A UUID string identifying the subscription.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying the enterprise.

try:
    # Delete a subscription
    api_instance.delete_subscription(subscription_id, enterprise_id)
except ApiException as e:
    print("Exception when calling SubscriptionApi->delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| A UUID string identifying the subscription. | 
 **enterprise_id** | [**str**](.md)| A UUID string identifying the enterprise. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subscriptions**
> InlineResponse20012 get_all_subscriptions(enterprise_id, limit=limit, offset=offset)

List Subscriptions in Enterprise

API to view all the subscriptions in an enterprise

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
api_instance = esperclient.SubscriptionApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying the enterprise.
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    # List Subscriptions in Enterprise
    api_response = api_instance.get_all_subscriptions(enterprise_id, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_all_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_id** | [**str**](.md)| A UUID string identifying the enterprise. | 
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

# **get_subscription**
> EventSubscription get_subscription(subscription_id, enterprise_id)

Get subscription information

Returns subscription instance

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
api_instance = esperclient.SubscriptionApi(esperclient.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | A UUID string identifying the subscription.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying the enterprise.

try:
    # Get subscription information
    api_response = api_instance.get_subscription(subscription_id, enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| A UUID string identifying the subscription. | 
 **enterprise_id** | [**str**](.md)| A UUID string identifying the enterprise. | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

