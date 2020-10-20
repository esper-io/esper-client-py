# Content
> esperclient.models.content

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique content Identifier | 
**download_url** | **str** | URL to download the content | [optional] 
**name** | **str** | Name of the content | [optional] 
**key** | **str** |  | [optional] 
**is_dir** | **bool** |  | [optional] [default to False]
**kind** | **str** | The mime type of the content | [optional] 
**hash** | **str** | Hash string of the content | [optional] 
**size** | **str** | Size of the content in bytes | [optional] 
**path** | **str** | Path to the content | [optional] 
**permissions** | **str** | The permssion string for the content | [optional] 
**tags** | **list[str]** | Tags for the content | [optional] 
**description** | **str** | Description for the content | [optional] 
**created** | **datetime** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**enterprise** | **str** | URL of the enterprise resource | [optional] 
**owner** | [**Owner**](Owner.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


