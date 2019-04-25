# DeviceStatusTiles

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**device** | [**DeviceCustom**](DeviceCustom.md) |  | 
**network_info** | **str** |  | 
**model** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**battery_level** | **float** |  | [optional] 
**security_state** | **int** | Security state enum * SECURE &#x3D; 1 * LOW_RISK &#x3D; 10 * MEDIUM_RISK &#x3D; 20 * HIGH_RISK &#x3D; 30 * DEVICE_STATE_UNSPECIFIED &#x3D; 100  | [optional] 
**security_reason** | **int** | Security reason enum * BOOTLOADER_UNLOCKED &#x3D; 1 * CUSTOM_ROM_INSTALLED_OR_BOOTLOADER_UNLOCKED&#x3D; 10 * DEVICE_ROOTED_OR_TAMPERED &#x3D; 20 * OUTDATED_SECURITY_PATCHES &#x3D; 30 * ERROR_FETCHING_VALUES &#x3D; 40 * NOT_APPLICABLE &#x3D; 50  | [optional] 
**security_advise** | **int** | Security advice enum * LOCK_BOOTLOADER &#x3D; 1 * RESTORE_TO_FACTORY_ROM &#x3D; 10 * UPDATE_SECURITY_PATCHES &#x3D; 20 * NOT_APPLICABLE &#x3D; 30  | [optional] 
**wifi_ssid** | **str** |  | [optional] 
**updated_on** | **datetime** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_gms** | **bool** |  | [optional] 
**enterprise** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


