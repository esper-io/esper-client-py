# Device
> esperclient.models.device

### Description
A class which describes an Esper-provisioned device.  It contains, as properties, a multitude of device qualities.  Objects of this class are commonly returned from API calls, sometimes in lists.

Returned by:
* [get_device_by_id](DeviceApi.md#get_device_by_id)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**device_name** | **str** |  | [optional] 
**alias_name** | **str** | Device friendly name | [optional] 
**policy_name** | **str** |  | [optional] 
**status** | **int** | Current status of device | [optional] 
**state** | **int** | Current state of device | [optional] 
**current_command** | **str** | Current command associated with device | [optional] 
**suid** | **str** | Device generated unique id | [optional] 
**fcm_id** | **str** |  | [optional] 
**enterprise** | **str** |  | [optional] 
**policy** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**groups** | **list[str]** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**api_level** | **int** |  | [optional] 
**template_name** | **str** |  | [optional] 
**mqtt_id** | **str** |  | [optional] 
**software_info** | **object** |  | [optional] 
**hardware_info** | **object** |  | [optional] 
**displays** | **object** |  | [optional] 
**network_info** | **object** |  | [optional] 
**memory_info** | **object** |  | [optional] 
**audio_constraints** | **object** |  | [optional] 
**provisioned_on** | **datetime** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**updated_on** | **datetime** |  | [optional] 
**emm_device** | [**EmmDevice**](EmmDevice.md) |  | [optional] 
**is_gms** | **bool** |  | [optional] [default to True]
**is_active** | **bool** |  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


