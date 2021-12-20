# DeviceApp
> esperclient.models.device_app

### Description
A class which encapsulates the metadata of a single app.  This app may be installed or not installed on its particular device.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**permissions** | [**list[DeviceAppPermission]**](DeviceAppPermission.md) |  | [optional] 
**app_name** | **str** |  | 
**package_name** | **str** |  | 
**whitelisted** | **bool** |  | [optional] 
**is_data_clearable** | **bool** |  | [optional] 
**is_uninstallable** | **bool** |  | [optional] 
**product_id** | **str** |  | [optional] 
**version_code** | **str** |  | [optional] 
**version_name** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**updated_on** | **datetime** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**device** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


