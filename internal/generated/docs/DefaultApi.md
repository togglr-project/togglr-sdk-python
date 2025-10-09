# togglr_client.DefaultApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feature_health**](DefaultApi.md#get_feature_health) | **GET** /sdk/v1/features/{feature_key}/health | Get health status of feature (including auto-disable state)
[**report_feature_error**](DefaultApi.md#report_feature_error) | **POST** /sdk/v1/features/{feature_key}/report-error | Report feature execution error (for auto-disable)
[**sdk_v1_features_feature_key_evaluate_post**](DefaultApi.md#sdk_v1_features_feature_key_evaluate_post) | **POST** /sdk/v1/features/{feature_key}/evaluate | Evaluate feature for given context
[**sdk_v1_health_get**](DefaultApi.md#sdk_v1_health_get) | **GET** /sdk/v1/health | Health check for SDK server
[**track_feature_event**](DefaultApi.md#track_feature_event) | **POST** /sdk/v1/features/{feature_key}/track | Track event for a feature (impression / conversion / error / custom)


# **get_feature_health**
> FeatureHealth get_feature_health(feature_key)

Get health status of feature (including auto-disable state)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import togglr_client
from togglr_client.models.feature_health import FeatureHealth
from togglr_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090
# See configuration.py for a list of all supported configuration parameters.
configuration = togglr_client.Configuration(
    host = "http://localhost:8090"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with togglr_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = togglr_client.DefaultApi(api_client)
    feature_key = 'feature_key_example' # str | 

    try:
        # Get health status of feature (including auto-disable state)
        api_response = api_instance.get_feature_health(feature_key)
        print("The response of DefaultApi->get_feature_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_feature_health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_key** | **str**|  | 

### Return type

[**FeatureHealth**](FeatureHealth.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Health status of feature |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Feature not found |  -  |
**500** | Internal server error |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_feature_error**
> report_feature_error(feature_key, feature_error_report)

Report feature execution error (for auto-disable)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import togglr_client
from togglr_client.models.feature_error_report import FeatureErrorReport
from togglr_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090
# See configuration.py for a list of all supported configuration parameters.
configuration = togglr_client.Configuration(
    host = "http://localhost:8090"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with togglr_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = togglr_client.DefaultApi(api_client)
    feature_key = 'feature_key_example' # str | 
    feature_error_report = togglr_client.FeatureErrorReport() # FeatureErrorReport | 

    try:
        # Report feature execution error (for auto-disable)
        api_instance.report_feature_error(feature_key, feature_error_report)
    except Exception as e:
        print("Exception when calling DefaultApi->report_feature_error: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_key** | **str**|  | 
 **feature_error_report** | [**FeatureErrorReport**](FeatureErrorReport.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Error reported |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Feature not found |  -  |
**500** | Internal server error |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_v1_features_feature_key_evaluate_post**
> EvaluateResponse sdk_v1_features_feature_key_evaluate_post(feature_key, request_body)

Evaluate feature for given context

Returns feature evaluation result for given project and context.
The project is derived from the API key.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import togglr_client
from togglr_client.models.evaluate_response import EvaluateResponse
from togglr_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090
# See configuration.py for a list of all supported configuration parameters.
configuration = togglr_client.Configuration(
    host = "http://localhost:8090"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with togglr_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = togglr_client.DefaultApi(api_client)
    feature_key = 'feature_key_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Evaluate feature for given context
        api_response = api_instance.sdk_v1_features_feature_key_evaluate_post(feature_key, request_body)
        print("The response of DefaultApi->sdk_v1_features_feature_key_evaluate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sdk_v1_features_feature_key_evaluate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_key** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**EvaluateResponse**](EvaluateResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Evaluation result |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Feature not found |  -  |
**500** | Internal server error |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_v1_health_get**
> HealthResponse sdk_v1_health_get()

Health check for SDK server

### Example


```python
import togglr_client
from togglr_client.models.health_response import HealthResponse
from togglr_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090
# See configuration.py for a list of all supported configuration parameters.
configuration = togglr_client.Configuration(
    host = "http://localhost:8090"
)


# Enter a context with an instance of the API client
with togglr_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = togglr_client.DefaultApi(api_client)

    try:
        # Health check for SDK server
        api_response = api_instance.sdk_v1_health_get()
        print("The response of DefaultApi->sdk_v1_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sdk_v1_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Health information |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_feature_event**
> track_feature_event(feature_key, track_request)

Track event for a feature (impression / conversion / error / custom)

Send a feedback event related to a feature evaluation. Events are written to TimescaleDB
(hypertable) and used for analytics, auto-disable and training MAB algorithms.
The project is derived from the API key.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import togglr_client
from togglr_client.models.track_request import TrackRequest
from togglr_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090
# See configuration.py for a list of all supported configuration parameters.
configuration = togglr_client.Configuration(
    host = "http://localhost:8090"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with togglr_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = togglr_client.DefaultApi(api_client)
    feature_key = 'feature_key_example' # str | 
    track_request = {"variant_key":"A","event_type":"impression","reward":0,"context":{"user.id":"123","country":"RU"}} # TrackRequest | 

    try:
        # Track event for a feature (impression / conversion / error / custom)
        api_instance.track_feature_event(feature_key, track_request)
    except Exception as e:
        print("Exception when calling DefaultApi->track_feature_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_key** | **str**|  | 
 **track_request** | [**TrackRequest**](TrackRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Event accepted for processing |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Feature not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

