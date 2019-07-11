# DeviceAppPermission
> esperclient.models.device_app_permission

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**permission** | **str** |  | 
**grant_state** | **str** | * PERMISSION_GRANT_STATE_DEFAULT &#x3D; 0 * PERMISSION_GRANT_STATE_DENIED &#x3D; 1 * PERMISSION_GRANT_STATE_GRANTED &#x3D; 2  For state details check [Android docs](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#PERMISSION_GRANT_STATE_DEFAULT)  | [optional] 
**created_on** | **datetime** |  | [optional] 
**updated_on** | **datetime** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**app** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


