# ErrorTooManyRequests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ErrorError**](ErrorError.md) |  | 

## Example

```python
from togglr_client.models.error_too_many_requests import ErrorTooManyRequests

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorTooManyRequests from a JSON string
error_too_many_requests_instance = ErrorTooManyRequests.from_json(json)
# print the JSON string representation of the object
print(ErrorTooManyRequests.to_json())

# convert the object into a dict
error_too_many_requests_dict = error_too_many_requests_instance.to_dict()
# create an instance of ErrorTooManyRequests from a dict
error_too_many_requests_from_dict = ErrorTooManyRequests.from_dict(error_too_many_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


