Esper Manage python SDK
==================

Python client library to communicate with Esper Manage APIs that help you programmatically control and monitor your enterprise's dedicated Esper endpoint. To read more about the various capabilities of Esper endpoints and Esper managed devices, please visit [esper.io](https://esper.io).


- API version: 1.0.0
- Package version: 0.0.6


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
python setup.py install
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.host = 'SERVER_URL'
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.ApplicationApi(esperclient.ApiClient(configuration))
version_id = 'version_id_example' # str | A UUID string identifying this app version.
application_id = 'application_id_example' # str | A UUID string identifying this application.
enterprise_id = 'enterprise_id_example' # str | A UUID string identifying enterprise.

try:
    # Delete app version
    api_instance.delete_app_version(version_id, application_id, enterprise_id)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_app_version: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://DOMAIN.shoonyacloud.com/api*


Class | Method | HTTP request
------------ | ------------- | -------------
*ApplicationApi* | [**delete_app_version**](docs/ApplicationApi.md#delete_app_version) | **DELETE** /enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/
*ApplicationApi* | [**delete_application**](docs/ApplicationApi.md#delete_application) | **DELETE** /enterprise/{enterprise_id}/application/{application_id}/
*ApplicationApi* | [**get_all_applications**](docs/ApplicationApi.md#get_all_applications) | **GET** /enterprise/{enterprise_id}/application/
*ApplicationApi* | [**get_app_version**](docs/ApplicationApi.md#get_app_version) | **GET** /enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/
*ApplicationApi* | [**get_app_versions**](docs/ApplicationApi.md#get_app_versions) | **GET** /enterprise/{enterprise_id}/application/{application_id}/version/
*ApplicationApi* | [**get_application**](docs/ApplicationApi.md#get_application) | **GET** /enterprise/{enterprise_id}/application/{application_id}/
*ApplicationApi* | [**upload**](docs/ApplicationApi.md#upload) | **POST** /enterprise/{enterprise_id}/application/upload/
*CommandsApi* | [**run_command**](docs/CommandsApi.md#run_command) | **POST** /enterprise/{enterprise_id}/device/{device_id}/command/
*DeviceApi* | [**get_all_devices**](docs/DeviceApi.md#get_all_devices) | **GET** /enterprise/{enterprise_id}/device/
*DeviceApi* | [**get_app_installs**](docs/DeviceApi.md#get_app_installs) | **GET** /enterprise/{enterprise_id}/device/{device_id}/install/
*DeviceApi* | [**get_device_by_id**](docs/DeviceApi.md#get_device_by_id) | **GET** /enterprise/{enterprise_id}/device/{device_id}/
*DeviceApi* | [**get_device_event**](docs/DeviceApi.md#get_device_event) | **GET** /enterprise/{enterprise_id}/device/{device_id}/status/
*DeviceAppApi* | [**get_device_app_by_id**](docs/DeviceAppApi.md#get_device_app_by_id) | **GET** /enterprise/{enterprise_id}/device/{device_id}/app/{app_id}/
*DeviceAppApi* | [**get_device_apps**](docs/DeviceAppApi.md#get_device_apps) | **GET** /enterprise/{enterprise_id}/device/{device_id}/app/
*DeviceGroupApi* | [**create_group**](docs/DeviceGroupApi.md#create_group) | **POST** /enterprise/{enterprise_id}/devicegroup/
*DeviceGroupApi* | [**delete_group**](docs/DeviceGroupApi.md#delete_group) | **DELETE** /enterprise/{enterprise_id}/devicegroup/{group_id}/
*DeviceGroupApi* | [**get_all_groups**](docs/DeviceGroupApi.md#get_all_groups) | **GET** /enterprise/{enterprise_id}/devicegroup/
*DeviceGroupApi* | [**get_group_by_id**](docs/DeviceGroupApi.md#get_group_by_id) | **GET** /enterprise/{enterprise_id}/devicegroup/{group_id}/
*DeviceGroupApi* | [**partial_update_group**](docs/DeviceGroupApi.md#partial_update_group) | **PATCH** /enterprise/{enterprise_id}/devicegroup/{group_id}/
*DeviceGroupApi* | [**update_group**](docs/DeviceGroupApi.md#update_group) | **PUT** /enterprise/{enterprise_id}/devicegroup/{group_id}/
*EnterpriseApi* | [**get_all_enterprises**](docs/EnterpriseApi.md#get_all_enterprises) | **GET** /enterprise/
*EnterpriseApi* | [**get_enterprise**](docs/EnterpriseApi.md#get_enterprise) | **GET** /enterprise/{enterprise_id}/
*EnterpriseApi* | [**partial_update_enterprise**](docs/EnterpriseApi.md#partial_update_enterprise) | **PATCH** /enterprise/{enterprise_id}/
*PolicyApi* | [**create_policy**](docs/PolicyApi.md#create_policy) | **POST** /enterprise/{enterprise_id}/policy/
*PolicyApi* | [**delete_policy**](docs/PolicyApi.md#delete_policy) | **DELETE** /enterprise/{enterprise_id}/policy/{policy_id}/
*PolicyApi* | [**get_all_policies**](docs/PolicyApi.md#get_all_policies) | **GET** /enterprise/{enterprise_id}/policy/
*PolicyApi* | [**get_policy_by_id**](docs/PolicyApi.md#get_policy_by_id) | **GET** /enterprise/{enterprise_id}/policy/{policy_id}/
*PolicyApi* | [**partial_update_policy**](docs/PolicyApi.md#partial_update_policy) | **PATCH** /enterprise/{enterprise_id}/policy/{policy_id}/
*PolicyApi* | [**update_policy**](docs/PolicyApi.md#update_policy) | **PUT** /enterprise/{enterprise_id}/policy/{policy_id}/


## Documentation For Models

 - [AppInstall](docs/AppInstall.md)
 - [AppPermission](docs/AppPermission.md)
 - [AppVersion](docs/AppVersion.md)
 - [Application](docs/Application.md)
 - [ApplicationVersion](docs/ApplicationVersion.md)
 - [CommandRequest](docs/CommandRequest.md)
 - [Device](docs/Device.md)
 - [DeviceApp](docs/DeviceApp.md)
 - [DeviceAppPermission](docs/DeviceAppPermission.md)
 - [DeviceCommand](docs/DeviceCommand.md)
 - [DeviceCustom](docs/DeviceCustom.md)
 - [DeviceCustomGroup](docs/DeviceCustomGroup.md)
 - [DeviceStatus](docs/DeviceStatus.md)
 - [DeviceStatusTiles](docs/DeviceStatusTiles.md)
 - [EmmDevice](docs/EmmDevice.md)
 - [Enterprise](docs/Enterprise.md)
 - [EnterpriseDetail](docs/EnterpriseDetail.md)
 - [EnterpriseDeviceGroup](docs/EnterpriseDeviceGroup.md)
 - [EnterprisePolicy](docs/EnterprisePolicy.md)
 - [GoogleEnterprise](docs/GoogleEnterprise.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [UnauthorizedResponse](docs/UnauthorizedResponse.md)


## Documentation For Enums

 - [AppInstallStateEnum](docs/AppInstallStateEnum.md)
 - [DeviceCommandEnum](docs/DeviceCommandEnum.md)
 - [EMMEnterpriseStateEnum](docs/EMMEnterpriseStateEnum.md)


## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

developer@esper.io


## License

Copyright 2019 Shoonya Enterprises Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
