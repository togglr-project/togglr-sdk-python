# EvaluateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** |  | 
**enabled** | **bool** |  | 
**value** | **str** |  | 

## Example

```python
from togglr_client.models.evaluate_response import EvaluateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluateResponse from a JSON string
evaluate_response_instance = EvaluateResponse.from_json(json)
# print the JSON string representation of the object
print(EvaluateResponse.to_json())

# convert the object into a dict
evaluate_response_dict = evaluate_response_instance.to_dict()
# create an instance of EvaluateResponse from a dict
evaluate_response_from_dict = EvaluateResponse.from_dict(evaluate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


