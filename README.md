Esper Manage python SDK
==================

Python client library for Esper Manage APIs. You can find out more about Esper at [https://shoonya.io](https://shoonya.io).

- API version: 1.0.0
- Package version: 0.0.1


## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

### Option 1: pip install

From Python package index

```sh
pip install esperclient
```

### Option 2: pip install

You can install directly from Github

```sh
pip install git+https://github.com/esper-io/esper-client-py.git
```

### Option 3: Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

## Getting Started

Please follow the [installation procedure](#installation--usage):

Then import the package:
```python
import esperclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import esperclient
from esperclient.rest import ApiException

# Configure HTTP basic authorization: basic_security
configuration = esperclient.Configuration()
configuration.host = 'SERVER_URL'
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esperclient.CommandsApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise
device_id = 'device_id_example' # str | ID of the device
command = esperclient.DeviceCommandRequest() # DeviceCommandRequest | command name to fire

try:
    # Run commands on device
    api_response = api_instance.run_command(enterprise_id, device_id, command)
    print(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->run_command: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://demo.esper.io/api*


Class | Method | HTTP request
------------ | ------------- | -------------
*CommandsApi* | [**run_command**](docs/CommandsApi.md#run_command) | **POST** /enterprise/{enterprise_id}/device/{device_id}/command/
*DeviceApi* | [**get_all_devices**](docs/DeviceApi.md#get_all_devices) | **GET** /enterprise/{enterprise_id}/device/
*DeviceApi* | [**get_device_by_id**](docs/DeviceApi.md#get_device_by_id) | **GET** /enterprise/{enterprise_id}/device/{device_id}/


## Documentation For Models

 - [Device](docs/Device.md)
 - [DeviceCommandRequest](docs/DeviceCommandRequest.md)
 - [DeviceCommandResponse](docs/DeviceCommandResponse.md)
 - [EmmDevice](docs/EmmDevice.md)
 - [InlineResponse200](docs/InlineResponse200.md)


## Documentation For Enums

 - [DeviceCommandEnum](docs/DeviceCommandEnum.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header

## basic_security

- **Type**: HTTP basic authentication


## Author

developer@esper.io


## License

```
Copyright 2019 Shoonya, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
