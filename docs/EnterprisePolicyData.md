# EnterprisePolicyData
> esperclient.models.enterprise_policy_data

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyguard_disabled** | **bool** | Should KeyGuard be disabled? | [optional] 
**safe_boot_disabled** | **bool** | Should SafeBoot be disabled? | [optional] 
**status_bar_disabled** | **bool** | Should Status Bar be disabled? | [optional] 
**factory_reset_disabled** | **bool** | Should Factory Reset be disabled? | [optional] 
**screenshot_disabled** | **bool** | Should Screenshot capability be disabled? | [optional] 
**usb_connectivity_disabled** | **bool** | Should USB connectivity be disabled? | [optional] 
**sms_disabled** | **bool** | Should SMS functionality be disabled? | [optional] 
**outgoing_calls_disabled** | **bool** | Should Outgoing Calls be disabled? | [optional] 
**camera_disabled** | **bool** | Should Camera be disabled? | [optional] 
**nfc_beam_disabled** | **bool** | Should NFC capability be disabled? | [optional] 
**disable_play_store** | **bool** | Should Google Play Store be disabled on the device? | [optional] 
**usb_file_transfer_disabled** | **bool** | Should USB File transfer capability be disabled? | [optional] 
**tethering_disabled** | **bool** | Should USB Tethering capability be enabled? | [optional] 
**date_time_config_disabled** | **bool** | Should Date/Time configuration capability be disabled? | [optional] 
**app_uninstall_disabled** | **bool** | Should App uninstall capability be disabled? | [optional] 
**google_assistant_disabled** | **bool** | Should Google Assistant feature be disabled? | [optional] 
**disable_local_app_install** | **bool** | Should Side-loading of Applications be disabled? | [optional] 
**adb_disabled** | **bool** | Should Android Debugger be disabled? | [optional] 
**phone_policy** | [**EnterprisePolicyDataPhonePolicy**](EnterprisePolicyDataPhonePolicy.md) |  | [optional] 
**frp_googles** | [**list[EnterprisePolicyDataFrpGoogles]**](EnterprisePolicyDataFrpGoogles.md) | Details regarding Factory Reset Protection capability. List of permitted Google People IDs, emails and such | [optional] 
**google_account_permission** | [**EnterprisePolicyDataGoogleAccountPermission**](EnterprisePolicyDataGoogleAccountPermission.md) |  | [optional] 
**device_password_policy** | [**EnterprisePolicyDataDevicePasswordPolicy**](EnterprisePolicyDataDevicePasswordPolicy.md) |  | [optional] 
**minimum_password_length** | **int** | What is the minimum length for your device&#39;s password | [optional] 
**permission_policy** | **str** | What permission should be applied by default for all apps, henceforth? | [optional] 
**device_update_policy** | [**EnterprisePolicyDataDeviceUpdatePolicy**](EnterprisePolicyDataDeviceUpdatePolicy.md) |  | [optional] 
**settings_access_level** | **str** | Type of Android settings app to be applied? Default System Settings or ESPER Settings App? | [optional] 
**settings_app_password** | **str** | Lock Password (optional) for the ESPER Settings app | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


