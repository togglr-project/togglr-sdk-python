# TrackRequest

Event sent from SDK. SDK SHOULD send an impression event for each evaluation (recommended). Conversions / errors / custom events are used to update algorithm statistics. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant_key** | **str** | Variant key returned by evaluate (e.g. \&quot;A\&quot;, \&quot;v2\&quot;). | 
**event_type** | **str** | Type of event (e.g. \&quot;success\&quot;, \&quot;failure\&quot;, \&quot;error\&quot;). | 
**reward** | **float** | Numeric reward associated with event (e.g. 1.0 for conversion). Default 0. | [optional] 
**context** | **Dict[str, object]** | Arbitrary context passed by SDK (user id, session, metadata). | [optional] 
**created_at** | **datetime** | Event timestamp. If omitted, server time will be used. | [optional] 
**dedup_key** | **str** | Optional idempotency key to deduplicate duplicate events from SDK retries. | [optional] 

## Example

```python
from togglr_client.models.track_request import TrackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackRequest from a JSON string
track_request_instance = TrackRequest.from_json(json)
# print the JSON string representation of the object
print(TrackRequest.to_json())

# convert the object into a dict
track_request_dict = track_request_instance.to_dict()
# create an instance of TrackRequest from a dict
track_request_from_dict = TrackRequest.from_dict(track_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


