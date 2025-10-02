# ErrorInternalServerError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorError**](ErrorError.md) |  | 

## Example

```python
from togglr_client.models.error_internal_server_error import ErrorInternalServerError

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorInternalServerError from a JSON string
error_internal_server_error_instance = ErrorInternalServerError.from_json(json)
# print the JSON string representation of the object
print(ErrorInternalServerError.to_json())

# convert the object into a dict
error_internal_server_error_dict = error_internal_server_error_instance.to_dict()
# create an instance of ErrorInternalServerError from a dict
error_internal_server_error_from_dict = ErrorInternalServerError.from_dict(error_internal_server_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


