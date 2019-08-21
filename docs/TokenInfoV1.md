# TokenInfoV1
> esperclient.models.token_info_v1

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Token id | 
**enterprise** | **str** | Id of the enterprise resource | 
**user** | **str** | Id of the user resource | [optional] 
**developer_app** | **str** | Id of the developer app resource that you created using the esper dev console | [optional] 
**source_refresh_token** | **str** | The refresh token is used to refresh your expired API token | [optional] 
**token** | **str** | API token for accessing esper APIs | [optional] 
**expires_on** | **datetime** | Date and time of when your API token will get expired | [optional] 
**scope** | **list[str]** | This defines what access scopes does your API token has | [optional] 
**created_on** | **datetime** | Date and time of when this resource was created | [optional] 
**updated_on** | **datetime** | Date and time of when this resource was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


