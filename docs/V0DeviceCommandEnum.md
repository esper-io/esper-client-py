# V0DeviceCommandEnum


### Description

Following commands are supported  ``` * REBOOT: Reboot a device * UPDATE_HEARTBEAT: Ping a device * UPDATE_DEVICE_CONFIG: Push additional configurations to the Device * INSTALL: Install an app on a device. Requires `app_version` in command arguments where `app_version` is the version id of app uploaded on Esper * UNINSTALL: UnInstall an app from device. Requires `package_name` in command arguments where `package_name` is the app package uploaded on Esper * SET_NEW_POLICY : Apply policy on device. Requires `policy_url` in command arguments where `policy_url` is the URL to the policy  * ADD_WIFI_AP : Add wifi access points for device. Requires `wifi_access_points` in command arguments where `wifi_access_points` is the data with access points * REMOVE_WIFI_AP : Remove Wifi access points for device. Requires `wifi_access_points` in command arguments where `wifi_access_points` is the data with access points * SET_KIOSK_APP : Command to set the Kiosk app for a device. Requires `package_name` in command arguments where `package_name` is the app package uploaded on Esper * SET_DEVICE_LOCKDOWN_STATE : Set lockdown state for a device. Requires `state` and `message` in command arguments where `state` is LOCKED/UNLOCKED and `message` is the message to be added with command * SET_APP_STATE : Set the state of an app - SHOW/HIDE/DISABLE. Requries `app_state` and `package_name`  in command arguments where `app_state` is the state of app and `package_name` is the app package uploaded on Esper * WIPE : Wipes the device. * UPDATE_LATEST_DPC : Prompt device to update the DPC app to the latest versions.  ``` 

## Properties
Name | Type
------------ | -------------
**REBOOT** | string
**UPDATE_HEARTBEAT** | string
**UPDATE_DEVICE_CONFIG** | string
**INSTALL** | string
**UNINSTALL** | string
**SET_NEW_POLICY** | string
**ADD_WIFI_AP** | string
**REMOVE_WIFI_AP** | string
**SET_KIOSK_APP** | string
**SET_DEVICE_LOCKDOWN_STATE** | string
**SET_APP_STATE** | string
**WIPE** | string
**UPDATE_LATEST_DPC** | string

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


