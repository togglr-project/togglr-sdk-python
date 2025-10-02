# FeatureHealth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** |  | 
**environment_key** | **str** |  | 
**enabled** | **bool** |  | 
**auto_disabled** | **bool** |  | 
**error_rate** | **float** |  | [optional] 
**threshold** | **float** |  | [optional] 
**last_error_at** | **datetime** |  | [optional] 

## Example

```python
from togglr_client.models.feature_health import FeatureHealth

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureHealth from a JSON string
feature_health_instance = FeatureHealth.from_json(json)
# print the JSON string representation of the object
print(FeatureHealth.to_json())

# convert the object into a dict
feature_health_dict = feature_health_instance.to_dict()
# create an instance of FeatureHealth from a dict
feature_health_from_dict = FeatureHealth.from_dict(feature_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


