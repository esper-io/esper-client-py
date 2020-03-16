Esper SDK for Python
==================

[![Build Status](https://travis-ci.com/esper-io/esper-client-py.svg?branch=master)](https://travis-ci.com/esper-io/esper-client-py) [![Gitter](https://badges.gitter.im/esper-dev/esper-sdk.svg)](https://gitter.im/esper-dev/esper-sdk?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Esper provides a Python client library to communicate with the Esper APIs to programmatically control and monitor your enterprise's Android-based Dedicated Devices using Esper Manage. To read more about the various capabilities of Esper Manage and Esper managed devices, please visit [esper.io](https://esper.io).


- API version: 1.0.0
- Package version: 0.0.12


## Requirements.

Python 3.4+

Additionally, you need a dedicated Esper environment set up on Esper Cloud through our Esper Dev Trial. For more details checkout [Esper Requirements](https://docs.esper.io/home/pythonsdk.html#pre-requisites)

## Installation

#### Using `pip install`

From PyPI
```sh
pip install esperclient
```

or

From [Github](https://github.com/esper-io/esper-client-py)
```sh
pip install git+https://github.com/esper-io/esper-client-py.git
```

#### From source

Download/Clone the project and install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
git clone https://github.com/esper-io/esper-client-py.git

cd esper-client-py

python setup.py install
```

> You need not install setuptools separately, they are packaged along with downloaded library


## Getting Started

Please follow the [installation procedure](#installation) stated above and then run the following:

```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization: apiKey
configuration = esperclient.Configuration()
configuration.host = 'SERVER_URL'
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = esperclient.DeviceApi(esperclient.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise

try:
    # Fetch all devices in an enterprise
    api_response = api_instance.get_all_devices(enterprise_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_all_devices: %s\n" % e)
```

## Documentation for API Endpoints

Given below is a detailed documentation for each of the API endpoint along with supported request options. All URIs are relative to *https://foo-api.esper.cloud/api*


Class | Method | HTTP request
------------ | ------------- | -------------
*ApplicationApi* | [**delete_app_version**](docs/ApplicationApi.md#delete_app_version) | **DELETE** /enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/
*ApplicationApi* | [**delete_application**](docs/ApplicationApi.md#delete_application) | **DELETE** /enterprise/{enterprise_id}/application/{application_id}/
*ApplicationApi* | [**get_all_applications**](docs/ApplicationApi.md#get_all_applications) | **GET** /enterprise/{enterprise_id}/application/
*ApplicationApi* | [**get_app_version**](docs/ApplicationApi.md#get_app_version) | **GET** /enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/
*ApplicationApi* | [**get_app_versions**](docs/ApplicationApi.md#get_app_versions) | **GET** /enterprise/{enterprise_id}/application/{application_id}/version/
*ApplicationApi* | [**get_application**](docs/ApplicationApi.md#get_application) | **GET** /enterprise/{enterprise_id}/application/{application_id}/
*ApplicationApi* | [**upload**](docs/ApplicationApi.md#upload) | **POST** /enterprise/{enterprise_id}/application/upload/
*CommandsApi* | [**get_command**](docs/CommandsApi.md#get_command) | **GET** /enterprise/{enterprise_id}/device/{device_id}/command/{command_id}/
*CommandsApi* | [**run_command**](docs/CommandsApi.md#run_command) | **POST** /enterprise/{enterprise_id}/device/{device_id}/command/
*DeviceApi* | [**get_all_devices**](docs/DeviceApi.md#get_all_devices) | **GET** /enterprise/{enterprise_id}/device/
*DeviceApi* | [**get_app_installs**](docs/DeviceApi.md#get_app_installs) | **GET** /enterprise/{enterprise_id}/device/{device_id}/install/
*DeviceApi* | [**get_device_app_by_id**](docs/DeviceApi.md#get_device_app_by_id) | **GET** /enterprise/{enterprise_id}/device/{device_id}/app/{app_id}/
*DeviceApi* | [**get_device_apps**](docs/DeviceApi.md#get_device_apps) | **GET** /enterprise/{enterprise_id}/device/{device_id}/app/
*DeviceApi* | [**get_device_by_id**](docs/DeviceApi.md#get_device_by_id) | **GET** /enterprise/{enterprise_id}/device/{device_id}/
*DeviceApi* | [**get_device_event**](docs/DeviceApi.md#get_device_event) | **GET** /enterprise/{enterprise_id}/device/{device_id}/status/
*DeviceGroupApi* | [**create_group**](docs/DeviceGroupApi.md#create_group) | **POST** /enterprise/{enterprise_id}/devicegroup/
*DeviceGroupApi* | [**delete_group**](docs/DeviceGroupApi.md#delete_group) | **DELETE** /enterprise/{enterprise_id}/devicegroup/{group_id}/
*DeviceGroupApi* | [**get_all_groups**](docs/DeviceGroupApi.md#get_all_groups) | **GET** /enterprise/{enterprise_id}/devicegroup/
*DeviceGroupApi* | [**get_group_by_id**](docs/DeviceGroupApi.md#get_group_by_id) | **GET** /enterprise/{enterprise_id}/devicegroup/{group_id}/
*DeviceGroupApi* | [**partial_update_group**](docs/DeviceGroupApi.md#partial_update_group) | **PATCH** /enterprise/{enterprise_id}/devicegroup/{group_id}/
*DeviceGroupApi* | [**update_group**](docs/DeviceGroupApi.md#update_group) | **PUT** /enterprise/{enterprise_id}/devicegroup/{group_id}/
*EnterpriseApi* | [**get_enterprise**](docs/EnterpriseApi.md#get_enterprise) | **GET** /v1/enterprise/{enterprise_id}/
*EnterpriseApi* | [**partial_update_enterprise**](docs/EnterpriseApi.md#partial_update_enterprise) | **PATCH** /v1/enterprise/{enterprise_id}/
*GroupCommandsApi* | [**get_group_command**](docs/GroupCommandsApi.md#get_group_command) | **GET** /enterprise/{enterprise_id}/devicegroup/{group_id}/command/{command_id}/
*GroupCommandsApi* | [**run_group_command**](docs/GroupCommandsApi.md#run_group_command) | **POST** /enterprise/{enterprise_id}/devicegroup/{group_id}/command/
*TokenApi* | [**get_token_info**](docs/TokenApi.md#get_token_info) | **GET** /v1/token-info/


## Documentation For Models

 - [AppInstall](docs/AppInstall.md)
 - [AppInstallApplication](docs/AppInstallApplication.md)
 - [AppInstallVersion](docs/AppInstallVersion.md)
 - [AppPermission](docs/AppPermission.md)
 - [AppVersion](docs/AppVersion.md)
 - [Application](docs/Application.md)
 - [ApplicationVersion](docs/ApplicationVersion.md)
 - [CommandArgs](docs/CommandArgs.md)
 - [CommandRequest](docs/CommandRequest.md)
 - [Device](docs/Device.md)
 - [DeviceApp](docs/DeviceApp.md)
 - [DeviceAppPermission](docs/DeviceAppPermission.md)
 - [DeviceCommand](docs/DeviceCommand.md)
 - [DeviceGroup](docs/DeviceGroup.md)
 - [DeviceGroupUpdate](docs/DeviceGroupUpdate.md)
 - [DeviceStatus](docs/DeviceStatus.md)
 - [EmmDevice](docs/EmmDevice.md)
 - [Enterprise](docs/Enterprise.md)
 - [EnterpriseDetail](docs/EnterpriseDetail.md)
 - [EnterpriseUpdateV1](docs/EnterpriseUpdateV1.md)
 - [EnterpriseV1](docs/EnterpriseV1.md)
 - [GoogleEMM](docs/GoogleEMM.md)
 - [GoogleEnterprise](docs/GoogleEnterprise.md)
 - [GroupCommand](docs/GroupCommand.md)
 - [GroupCommandArgs](docs/GroupCommandArgs.md)
 - [GroupCommandRequest](docs/GroupCommandRequest.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [TokenInfoV1](docs/TokenInfoV1.md)


## Documentation For Enums

 - [AppInstallStateEnum](docs/AppInstallStateEnum.md)
 - [DeviceCommandEnum](docs/DeviceCommandEnum.md)
 - [EMMEnterpriseStateEnum](docs/EMMEnterpriseStateEnum.md)
 - [GroupCommandEnum](docs/GroupCommandEnum.md)
 - [SettingsGPSStateEnum](docs/SettingsGPSStateEnum.md)
 - [SettingsRotateStateEnum](docs/SettingsRotateStateEnum.md)
 - [SettingsVolumeStreamEnum](docs/SettingsVolumeStreamEnum.md)


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
