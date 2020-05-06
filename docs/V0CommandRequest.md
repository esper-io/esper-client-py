# V0CommandRequest
> esperclient.models.v0_command_request

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique command request identifier | [optional] 
**enterprise** | **str** | Esper account identifier | [optional] 
**command_type** | **str** | Identifies the type of command  &#x60;&#x60;&#x60; * DEVICE: command request is meant for devices * GROUP: command request is meant for groups * DYNAMIC: command request is meant for dynamic set of devices   i.e subset of devices from different groups or otherwise. &#x60;&#x60;&#x60;  | [optional] 
**devices** | **list[str]** | list of devices to run commands | [optional] 
**groups** | **list[str]** | list of groups to run commands | [optional] 
**device_type** | **str** | Type of devices to run commands on  &#x60;&#x60;&#x60; * active: Run commands on currently online devices * inactive: Run commands on currently offline devices * all: Run commands on all the devices.   Commands will be queued for offline devices until they come back online. &#x60;&#x60;&#x60;  | [optional] [default to 'active']
**command** | [**V0DeviceCommandEnum**](V0DeviceCommandEnum.md) |  | [optional] 
**command_args** | [**V0CommandArgs**](V0CommandArgs.md) |  | [optional] 
**schedule** | [**V0CommandScheduleEnum**](V0CommandScheduleEnum.md) |  | [optional] 
**schedule_args** | [**V0CommandScheduleArgs**](V0CommandScheduleArgs.md) |  | [optional] 
**issued_by** | **str** | command is issued by this user | [optional] 
**created_on** | **datetime** | Timestamp of command request | [optional] 
**status** | [**list[V0CommandRequestStatus]**](V0CommandRequestStatus.md) | Show creent status of commands issued during in this request | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


