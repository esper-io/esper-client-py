# AppVersion
> esperclient.models.app_version

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**installed_count** | **int** |  | [optional] 
**permissions** | [**list[AppPermission]**](AppPermission.md) |  | 
**app_file** | **str** |  | [optional] 
**app_icon** | **str** |  | [optional] 
**version_code** | **str** |  | 
**version_name** | **str** | Human-readable version string (e.g., "1.0.02"). Available when legacy_format=false. | [optional]
**build_number** | **str** | Deprecated. Use version_code instead. | [optional] 
**size_in_mb** | **float** |  | [optional] 
**hash_string** | **str** |  | [optional] 
**release_name** | **str** |  | [optional] 
**release_comments** | **str** |  | [optional] 
**release_track** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**updated_on** | **datetime** |  | [optional] 
**min_sdk_version** | **str** |  | [optional] 
**target_sdk_version** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**enterprise** | **str** |  | 
**application** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


