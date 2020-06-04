# V0DeviceCommandEnum


### Description

Following commands are supported  ``` * REBOOT: Reboot a device * UPDATE_HEARTBEAT: Ping a device * UPDATE_DEVICE_CONFIG: Push additional configurations to the Device * INSTALL: Install an app on a device. Requires `app_version` in command arguments where `app_version` is the version id of app uploaded on Esper * UNINSTALL: UnInstall an app from device. Requires `package_name` in command arguments where `package_name` is the app package uploaded on Esper ``` 

## Properties
Name | Type
------------ | -------------
**REBOOT** | string
**UPDATE_HEARTBEAT** | string
**UPDATE_DEVICE_CONFIG** | string
**INSTALL** | string
**UNINSTALL** | string

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


