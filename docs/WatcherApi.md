# swagger_client.WatcherApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_watcher_markets**](WatcherApi.md#api_watcher_markets) | **GET** /markets | Returns a list of markets available for watching
[**api_watcher_start**](WatcherApi.md#api_watcher_start) | **POST** /start | Start the watching process
[**api_watcher_status**](WatcherApi.md#api_watcher_status) | **GET** /status | Returns a status of the watcher
[**api_watcher_stop**](WatcherApi.md#api_watcher_stop) | **POST** /stop | Stop the watcher process


# **api_watcher_markets**
> list[str] api_watcher_markets()

Returns a list of markets available for watching

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: endpoint_security
swagger_client.configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WatcherApi()

try: 
    # Returns a list of markets available for watching
    api_response = api_instance.api_watcher_markets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatcherApi->api_watcher_markets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[endpoint_security](../README.md#endpoint_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_watcher_start**
> InlineResponse200 api_watcher_start(parameters=parameters)

Start the watching process

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: endpoint_security
swagger_client.configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WatcherApi()
parameters = swagger_client.Parameters() # Parameters | Any subset of parameters of the watcher service that will overwrite the defaults values. If not specified, will be used defaults values See `WatcherParameters` model definition to explore default values.  (optional)

try: 
    # Start the watching process
    api_response = api_instance.api_watcher_start(parameters=parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatcherApi->api_watcher_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**Parameters**](Parameters.md)| Any subset of parameters of the watcher service that will overwrite the defaults values. If not specified, will be used defaults values See &#x60;WatcherParameters&#x60; model definition to explore default values.  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[endpoint_security](../README.md#endpoint_security)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_watcher_status**
> InlineResponse2001 api_watcher_status()

Returns a status of the watcher

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: endpoint_security
swagger_client.configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WatcherApi()

try: 
    # Returns a status of the watcher
    api_response = api_instance.api_watcher_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatcherApi->api_watcher_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[endpoint_security](../README.md#endpoint_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_watcher_stop**
> InlineResponse2002 api_watcher_stop()

Stop the watcher process

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: endpoint_security
swagger_client.configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WatcherApi()

try: 
    # Stop the watcher process
    api_response = api_instance.api_watcher_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatcherApi->api_watcher_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[endpoint_security](../README.md#endpoint_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

