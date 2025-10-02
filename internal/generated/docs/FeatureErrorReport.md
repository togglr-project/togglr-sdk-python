# FeatureErrorReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | **str** |  | 
**error_message** | **str** |  | 
**context** | **Dict[str, object]** |  | [optional] 

## Example

```python
from togglr_client.models.feature_error_report import FeatureErrorReport

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureErrorReport from a JSON string
feature_error_report_instance = FeatureErrorReport.from_json(json)
# print the JSON string representation of the object
print(FeatureErrorReport.to_json())

# convert the object into a dict
feature_error_report_dict = feature_error_report_instance.to_dict()
# create an instance of FeatureErrorReport from a dict
feature_error_report_from_dict = FeatureErrorReport.from_dict(feature_error_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


