# ErrorPermissionDenied


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorError**](ErrorError.md) |  | 

## Example

```python
from togglr_client.models.error_permission_denied import ErrorPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorPermissionDenied from a JSON string
error_permission_denied_instance = ErrorPermissionDenied.from_json(json)
# print the JSON string representation of the object
print(ErrorPermissionDenied.to_json())

# convert the object into a dict
error_permission_denied_dict = error_permission_denied_instance.to_dict()
# create an instance of ErrorPermissionDenied from a dict
error_permission_denied_from_dict = ErrorPermissionDenied.from_dict(error_permission_denied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


