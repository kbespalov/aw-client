# swagger_client
Provides the set of endpoints to manage arbitrage watcher service.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/kbespalov/aw-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
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

## Documentation for API Endpoints

All URIs are relative to *https://localhost/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*WatcherApi* | [**api_watcher_markets**](docs/WatcherApi.md#api_watcher_markets) | **GET** /markets | Returns a list of markets available for watching
*WatcherApi* | [**api_watcher_start**](docs/WatcherApi.md#api_watcher_start) | **POST** /start | Start the watching process
*WatcherApi* | [**api_watcher_status**](docs/WatcherApi.md#api_watcher_status) | **GET** /status | Returns a status of the watcher
*WatcherApi* | [**api_watcher_stop**](docs/WatcherApi.md#api_watcher_stop) | **POST** /stop | Stop the watcher process


## Documentation For Models

 - [ApplicationConfig](docs/ApplicationConfig.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2001CurrentParameters](docs/InlineResponse2001CurrentParameters.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [Parameters](docs/Parameters.md)
 - [WatcherConfig](docs/WatcherConfig.md)


## Documentation For Authorization


## endpoint_security

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string


## Author



