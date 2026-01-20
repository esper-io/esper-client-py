# Esper SDK for Python

[![Build Status](https://travis-ci.com/esper-io/esper-client-py.svg?branch=master)](https://travis-ci.com/esper-io/esper-client-py) [![Gitter](https://badges.gitter.im/esper-dev/esper-sdk.svg)](https://gitter.im/esper-dev/esper-sdk?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

**Esper SDK for Python** is a comprehensive Python client library that enables programmatic interaction with the Esper Manage platform APIs. Esper Manage is an enterprise-grade Android Device Management (MDM/EMM) solution designed for managing dedicated Android devices at scale.

- **API version**: 1.0.0
- **Package version**: 0.1.2

## What is Esper Manage?

Esper Manage is a cloud-based Android Enterprise Mobile Device Management (MDM/EMM) platform that provides:

- **Device Management**: Monitor, configure, and control Android devices remotely
- **Application Management**: Upload, distribute, and manage applications across device fleets
- **Policy Enforcement**: Configure device settings, security policies, and restrictions
- **Remote Commands**: Execute commands on devices remotely (reboot, lock, factory reset, etc.)
- **Geofencing**: Define location-based policies and triggers
- **Content Management**: Distribute files and content to devices
- **Event Subscriptions**: Subscribe to device events and webhooks
- **Device Grouping**: Organize devices into groups for bulk operations

## What Does This Library Do?

The `esper-client-py` library provides a Python interface to interact with all Esper Manage APIs. It abstracts the complexity of HTTP requests, authentication, and data serialization, allowing developers to:

- **Manage Devices**: Query device lists, get device details, check device status, and manage device groups
- **Handle Applications**: Upload APK files, manage application versions, track installations, and view app permissions
- **Execute Commands**: Send remote commands to individual devices or device groups, check command status, and view command history
- **Configure Policies**: Create and manage enterprise policies for device security, updates, and restrictions
- **Manage Content**: Upload and distribute files to devices
- **Set Up Geofences**: Create and manage geofences for location-based device management
- **Subscribe to Events**: Set up event subscriptions for real-time device event notifications
- **Manage Authentication**: Handle API tokens and authentication

## Use Cases

### 1. **Enterprise Device Fleet Management**
Manage large fleets of Android devices deployed across multiple locations:
- Automate device provisioning and enrollment
- Monitor device health and status at scale
- Apply consistent configurations across device groups
- Track device inventory and compliance

### 2. **Application Deployment Automation**
Automate application lifecycle management:
- Upload new app versions programmatically
- Deploy applications to specific devices or groups
- Track installation status across devices
- Manage app updates and rollbacks

### 3. **Remote Device Control**
Execute remote operations on devices:
- Reboot devices remotely
- Lock/unlock devices
- Factory reset devices
- Change device settings (WiFi, Bluetooth, GPS, etc.)
- Install/uninstall applications remotely

### 4. **Policy and Compliance Management**
Enforce security and compliance policies:
- Configure device password policies
- Set up device update policies
- Manage Google account permissions
- Enforce device restrictions

### 5. **Location-Based Management**
Implement geofencing for location-aware device management:
- Create geofences around specific locations
- Trigger actions when devices enter/exit geofences
- Enforce location-based policies

### 6. **Integration and Automation**
Build custom integrations and automation:
- Integrate Esper Manage with existing IT systems
- Automate device onboarding workflows
- Create custom dashboards and reporting tools
- Build CI/CD pipelines for app deployment

### 7. **Monitoring and Alerting**
Set up monitoring and alerting systems:
- Subscribe to device events
- Monitor device status changes
- Track application installations
- Receive notifications for device issues

## Requirements

- **Python**: 3.4 or higher
- **Esper Account**: A dedicated Esper environment set up on Esper Cloud through [Esper Dev Trial](https://docs.esper.io/home/pythonsdk.html#pre-requisites)

## Installation

### Using `pip install`

**From PyPI:**
```sh
pip install esperclient
```

**From GitHub:**
```sh
pip install git+https://github.com/esper-io/esper-client-py.git
```

### From Source

Download/Clone the project and install via [Setuptools](http://pypi.python.org/pypi/setuptools):

```sh
git clone https://github.com/esper-io/esper-client-py.git
cd esper-client-py
python setup.py install
```

> **Note**: Setuptools are packaged along with the downloaded library, so you don't need to install them separately.

## Getting Started

### Basic Setup

1. **Configure API credentials:**
```python
import esperclient
from esperclient.rest import ApiException

# Configure API key authorization
configuration = esperclient.Configuration()
configuration.host = 'https://your-environment.esper.cloud/api'  # Your Esper environment URL
configuration.api_key['Authorization'] = 'YOUR_API_KEY'  # Your API key from Esper dashboard
configuration.api_key_prefix['Authorization'] = 'Bearer'

# Create an API client instance
api_client = esperclient.ApiClient(configuration)
```

2. **Example: Fetch all devices in an enterprise**
```python
# Create an instance of the Device API
device_api = esperclient.DeviceApi(api_client)
enterprise_id = 'your-enterprise-id'  # Your enterprise UUID

try:
    # Fetch all devices
    devices_response = device_api.get_all_devices(enterprise_id)
    print(f"Total devices: {devices_response.count}")
    for device in devices_response.results:
        print(f"Device: {device.device_name} - Status: {device.current_state}")
except ApiException as e:
    print(f"Exception when calling DeviceApi->get_all_devices: {e}")
```

### Common Use Cases Examples

#### Upload and Install an Application

```python
application_api = esperclient.ApplicationApi(api_client)

# Upload an APK file
with open('path/to/your/app.apk', 'rb') as apk_file:
    try:
        upload_response = application_api.upload(
            enterprise_id,
            file=apk_file,
            application_name='My App',
            package_name='com.example.myapp'
        )
        print(f"Application uploaded: {upload_response.id}")
    except ApiException as e:
        print(f"Error uploading application: {e}")
```

#### Send a Remote Command to a Device

```python
from esperclient.models import V0CommandRequest, V0CommandArgs, V0DeviceCommandEnum

commands_api = esperclient.CommandsV2Api(api_client)

# Create a command request
command_request = V0CommandRequest(
    command=V0DeviceCommandEnum.REBOOT,  # Command type
    device_ids=[device_id],  # List of device UUIDs
    args=V0CommandArgs()  # Optional command arguments
)

try:
    response = commands_api.create_command(enterprise_id, command_request)
    print(f"Command created: {response.id}")
    
    # Check command status
    status = commands_api.get_command_request_status(enterprise_id, response.id)
    print(f"Command status: {status.status}")
except ApiException as e:
    print(f"Error executing command: {e}")
```

#### Create a Device Group

```python
from esperclient.models import DeviceGroup

device_group_api = esperclient.DeviceGroupApi(api_client)

group = DeviceGroup(
    name='Production Devices',
    description='All production devices'
)

try:
    created_group = device_group_api.create_group(enterprise_id, group)
    print(f"Group created: {created_group.id}")
except ApiException as e:
    print(f"Error creating group: {e}")
```

#### Get Device Status and Events

```python
device_api = esperclient.DeviceApi(api_client)

try:
    # Get device details
    device = device_api.get_device_by_id(enterprise_id, device_id)
    print(f"Device: {device.device_name}")
    print(f"Model: {device.model}")
    print(f"Android Version: {device.android_version}")
    
    # Get device status/events
    status = device_api.get_device_event(enterprise_id, device_id)
    print(f"Current State: {status.current_state}")
    print(f"Last Seen: {status.last_seen}")
except ApiException as e:
    print(f"Error fetching device info: {e}")
```

## API Reference

The library provides access to the following API classes:

### Core APIs

| API Class | Description |
|-----------|-------------|
| `DeviceApi` | Manage devices, query device information, get device status |
| `ApplicationApi` | Upload applications, manage app versions, track installations |
| `CommandsApi` | Execute commands on individual devices (legacy) |
| `CommandsV2Api` | Execute commands on devices or groups (recommended) |
| `DeviceGroupApi` | Create and manage device groups |
| `GroupCommandsApi` | Execute commands on device groups |

### Management APIs

| API Class | Description |
|-----------|-------------|
| `EnterpriseApi` | Manage enterprise settings and configuration |
| `EnterprisePolicyApi` | Create and manage enterprise policies |
| `ContentApi` | Upload and manage content/files |
| `GeofenceApi` | Create and manage geofences |
| `SubscriptionApi` | Manage event subscriptions |
| `TokenApi` | Manage API tokens and authentication |

### Complete API Documentation

For detailed API documentation, see the [API Endpoints Documentation](#documentation-for-api-endpoints) section below.

## Documentation for API Endpoints

All URIs are relative to `https://your-environment.esper.cloud/api`

### Device Management

| Class | Method | HTTP Request | Description |
|-------|--------|--------------|-------------|
| `DeviceApi` | `get_all_devices` | **GET** `/enterprise/{enterprise_id}/device/` | Fetch all devices in an enterprise |
| `DeviceApi` | `get_device_by_id` | **GET** `/enterprise/{enterprise_id}/device/{device_id}/` | Get device details by ID |
| `DeviceApi` | `get_device_event` | **GET** `/enterprise/{enterprise_id}/device/{device_id}/status/` | Get device status/events |
| `DeviceApi` | `get_device_apps` | **GET** `/enterprise/{enterprise_id}/device/{device_id}/app/` | List apps installed on device |
| `DeviceApi` | `get_app_installs` | **GET** `/enterprise/{enterprise_id}/device/{device_id}/install/` | List app installations |

### Application Management

| Class | Method | HTTP Request | Description |
|-------|--------|--------------|-------------|
| `ApplicationApi` | `upload` | **POST** `/enterprise/{enterprise_id}/application/upload/` | Upload an APK file |
| `ApplicationApi` | `get_all_applications` | **GET** `/enterprise/{enterprise_id}/application/` | List all applications |
| `ApplicationApi` | `get_application` | **GET** `/enterprise/{enterprise_id}/application/{application_id}/` | Get application details |
| `ApplicationApi` | `get_app_versions` | **GET** `/enterprise/{enterprise_id}/application/{application_id}/version/` | List app versions |
| `ApplicationApi` | `get_install_devices` | **GET** `/enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/installdevices` | Get devices with app installed |
| `ApplicationApi` | `delete_application` | **DELETE** `/enterprise/{enterprise_id}/application/{application_id}/` | Delete an application |
| `ApplicationApi` | `delete_app_version` | **DELETE** `/enterprise/{enterprise_id}/application/{application_id}/version/{version_id}/` | Delete an app version |

### Command Execution

| Class | Method | HTTP Request | Description |
|-------|--------|--------------|-------------|
| `CommandsV2Api` | `create_command` | **POST** `/v0/enterprise/{enterprise_id}/command/` | Create a command request |
| `CommandsV2Api` | `get_command_request_status` | **GET** `/v0/enterprise/{enterprise_id}/command/{request_id}/status/` | Get command status |
| `CommandsV2Api` | `get_device_command_history` | **GET** `/v0/enterprise/{enterprise_id}/device/{device_id}/command-history/` | Get device command history |
| `CommandsV2Api` | `list_command_request` | **GET** `/v0/enterprise/{enterprise_id}/command/` | List command requests |
| `CommandsApi` | `run_command` | **POST** `/enterprise/{enterprise_id}/device/{device_id}/command/` | Run command on device (legacy) |
| `GroupCommandsApi` | `run_group_command` | **POST** `/enterprise/{enterprise_id}/devicegroup/{group_id}/command/` | Run command on device group |

### Device Groups

| Class | Method | HTTP Request | Description |
|-------|--------|--------------|-------------|
| `DeviceGroupApi` | `create_group` | **POST** `/enterprise/{enterprise_id}/devicegroup/` | Create a device group |
| `DeviceGroupApi` | `get_all_groups` | **GET** `/enterprise/{enterprise_id}/devicegroup/` | List all device groups |
| `DeviceGroupApi` | `get_group_by_id` | **GET** `/enterprise/{enterprise_id}/devicegroup/{group_id}/` | Get group details |
| `DeviceGroupApi` | `update_group` | **PUT** `/enterprise/{enterprise_id}/devicegroup/{group_id}/` | Update a device group |
| `DeviceGroupApi` | `partial_update_group` | **PATCH** `/enterprise/{enterprise_id}/devicegroup/{group_id}/` | Partially update a group |
| `DeviceGroupApi` | `delete_group` | **DELETE** `/enterprise/{enterprise_id}/devicegroup/{group_id}/` | Delete a device group |

### Enterprise & Policies

| Class | Method | HTTP Request | Description |
|-------|--------|--------------|-------------|
| `EnterpriseApi` | `get_enterprise` | **GET** `/v1/enterprise/{enterprise_id}/` | Get enterprise details |
| `EnterpriseApi` | `partial_update_enterprise` | **PATCH** `/v1/enterprise/{enterprise_id}/` | Update enterprise settings |
| `EnterprisePolicyApi` | `create_policy` | **POST** `/enterprise/{enterprise_id}/policy/` | Create an enterprise policy |
| `EnterprisePolicyApi` | `list_policies` | **GET** `/enterprise/{enterprise_id}/policy/` | List all policies |
| `EnterprisePolicyApi` | `get_policy_by_id` | **GET** `/enterprise/{enterprise_id}/policy/{policy_id}/` | Get policy details |
| `EnterprisePolicyApi` | `update_policy` | **PUT** `/enterprise/{enterprise_id}/policy/{policy_id}/` | Update a policy |
| `EnterprisePolicyApi` | `delete_enterprise_policy` | **DELETE** `/enterprise/{enterprise_id}/policy/{policy_id}/` | Delete a policy |

### Content Management

| Class | Method | HTTP Request | Description |
|-------|--------|--------------|-------------|
| `ContentApi` | `post_content` | **POST** `/v0/enterprise/{enterprise_id}/content/upload/` | Upload content |
| `ContentApi` | `get_all_content` | **GET** `/v0/enterprise/{enterprise_id}/content/` | List all content |
| `ContentApi` | `get_content` | **GET** `/v0/enterprise/{enterprise_id}/content/{content_id}/` | Get content details |
| `ContentApi` | `patch_content` | **PATCH** `/v0/enterprise/{enterprise_id}/content/{content_id}/` | Update content |
| `ContentApi` | `delete_content` | **DELETE** `/v0/enterprise/{enterprise_id}/content/{content_id}/` | Delete content |

### Geofencing

| Class | Method | HTTP Request | Description |
|-------|--------|--------------|-------------|
| `GeofenceApi` | `create_geofence` | **POST** `/v0/enterprise/{enterprise_id}/geofence/` | Create a geofence |
| `GeofenceApi` | `get_all_geofences` | **GET** `/v0/enterprise/{enterprise_id}/geofence/` | List all geofences |
| `GeofenceApi` | `get_geofence` | **GET** `/v0/enterprise/{enterprise_id}/geofence/{geofence_id}/` | Get geofence details |
| `GeofenceApi` | `update_geofence` | **PUT** `/v0/enterprise/{enterprise_id}/geofence/{geofence_id}/` | Update a geofence |
| `GeofenceApi` | `delete_geofence` | **DELETE** `/v0/enterprise/{enterprise_id}/geofence/{geofence_id}/` | Delete a geofence |

### Event Subscriptions

| Class | Method | HTTP Request | Description |
|-------|--------|--------------|-------------|
| `SubscriptionApi` | `create_subscription` | **POST** `/v0/enterprise/{enterprise_id}/subscription/` | Create event subscription |
| `SubscriptionApi` | `get_all_subscriptions` | **GET** `/v0/enterprise/{enterprise_id}/subscription/` | List all subscriptions |
| `SubscriptionApi` | `get_subscription` | **GET** `/v0/enterprise/{enterprise_id}/subscription/{subscription_id}/` | Get subscription details |
| `SubscriptionApi` | `delete_subscription` | **DELETE** `/v0/enterprise/{enterprise_id}/subscription/{subscription_id}/` | Delete subscription |

### Authentication

| Class | Method | HTTP Request | Description |
|-------|--------|--------------|-------------|
| `TokenApi` | `get_token_info` | **GET** `/v1/token-info/` | Get token information |
| `TokenApi` | `renew_token` | **POST** `/v0/enterprise/{enterprise_id}/developerapp/{developerapp_id}/renew-token/` | Renew API token |

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
- [Content](docs/Content.md)
- [Data](docs/Data.md)
- [Device](docs/Device.md)
- [DeviceApp](docs/DeviceApp.md)
- [DeviceAppPermission](docs/DeviceAppPermission.md)
- [DeviceCommand](docs/DeviceCommand.md)
- [DeviceGroup](docs/DeviceGroup.md)
- [DeviceGroupPartialUpdate](docs/DeviceGroupPartialUpdate.md)
- [DeviceGroupUpdate](docs/DeviceGroupUpdate.md)
- [DeviceStatus](docs/DeviceStatus.md)
- [EmmDevice](docs/EmmDevice.md)
- [EnterprisePolicy](docs/EnterprisePolicy.md)
- [EnterprisePolicyData](docs/EnterprisePolicyData.md)
- [EnterprisePolicyDataDevicePasswordPolicy](docs/EnterprisePolicyDataDevicePasswordPolicy.md)
- [EnterprisePolicyDataDeviceUpdatePolicy](docs/EnterprisePolicyDataDeviceUpdatePolicy.md)
- [EnterprisePolicyDataFrpGoogles](docs/EnterprisePolicyDataFrpGoogles.md)
- [EnterprisePolicyDataGoogleAccountPermission](docs/EnterprisePolicyDataGoogleAccountPermission.md)
- [EnterprisePolicyDataPhonePolicy](docs/EnterprisePolicyDataPhonePolicy.md)
- [EnterprisePolicyPartialUpdate](docs/EnterprisePolicyPartialUpdate.md)
- [EnterpriseUpdateV1](docs/EnterpriseUpdateV1.md)
- [EnterpriseV1](docs/EnterpriseV1.md)
- [EventSubscription](docs/EventSubscription.md)
- [EventSubscriptionArgs](docs/EventSubscriptionArgs.md)
- [Geofence](docs/Geofence.md)
- [GeofenceUpdate](docs/GeofenceUpdate.md)
- [GoogleEMM](docs/GoogleEMM.md)
- [GroupCommand](docs/GroupCommand.md)
- [GroupCommandArgs](docs/GroupCommandArgs.md)
- [GroupCommandRequest](docs/GroupCommandRequest.md)
- [InlineResponse200](docs/InlineResponse200.md)
- [InlineResponse2001](docs/InlineResponse2001.md)
- [InlineResponse20010](docs/InlineResponse20010.md)
- [InlineResponse20011](docs/InlineResponse20011.md)
- [InlineResponse20012](docs/InlineResponse20012.md)
- [InlineResponse20013](docs/InlineResponse20013.md)
- [InlineResponse2002](docs/InlineResponse2002.md)
- [InlineResponse2003](docs/InlineResponse2003.md)
- [InlineResponse2004](docs/InlineResponse2004.md)
- [InlineResponse2005](docs/InlineResponse2005.md)
- [InlineResponse2006](docs/InlineResponse2006.md)
- [InlineResponse2007](docs/InlineResponse2007.md)
- [InlineResponse2008](docs/InlineResponse2008.md)
- [InlineResponse2009](docs/InlineResponse2009.md)
- [InlineResponse201](docs/InlineResponse201.md)
- [InstallDevices](docs/InstallDevices.md)
- [Owner](docs/Owner.md)
- [TokenInfoV1](docs/TokenInfoV1.md)
- [TokenRenewV0](docs/TokenRenewV0.md)
- [V0CommandArgs](docs/V0CommandArgs.md)
- [V0CommandRequest](docs/V0CommandRequest.md)
- [V0CommandRequestStatus](docs/V0CommandRequestStatus.md)
- [V0CommandScheduleArgs](docs/V0CommandScheduleArgs.md)
- [V0CommandStatus](docs/V0CommandStatus.md)

## Documentation For Enums

- [AppInstallStateEnum](docs/AppInstallStateEnum.md)
- [DeviceCommandEnum](docs/DeviceCommandEnum.md)
- [GroupCommandEnum](docs/GroupCommandEnum.md)
- [SettingsGPSStateEnum](docs/SettingsGPSStateEnum.md)
- [SettingsRotateStateEnum](docs/SettingsRotateStateEnum.md)
- [SettingsVolumeStreamEnum](docs/SettingsVolumeStreamEnum.md)
- [V0CommandScheduleArgsTimeTypeEnum](docs/V0CommandScheduleArgsTimeTypeEnum.md)
- [V0CommandScheduleEnum](docs/V0CommandScheduleEnum.md)
- [V0DeviceCommandEnum](docs/V0DeviceCommandEnum.md)

## Documentation For Authorization

## apiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

## Author

developer@esper.io

## Additional Resources

- **Esper Documentation**: [https://docs.esper.io](https://docs.esper.io)
- **Esper Website**: [https://esper.io](https://esper.io)
- **Python SDK Documentation**: [https://docs.esper.io/home/pythonsdk.html](https://docs.esper.io/home/pythonsdk.html)
- **GitHub Repository**: [https://github.com/esper-io/esper-client-py](https://github.com/esper-io/esper-client-py)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

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

## Support

For support, please contact:
- **Email**: developer@esper.io
- **Gitter**: [esper-dev/esper-sdk](https://gitter.im/esper-dev/esper-sdk)
