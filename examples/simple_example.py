#!/usr/bin/env python3
"""Simple example of using togglr-sdk-python."""

import togglr
from togglr import Client, RequestContext, TrackEvent, EventType


def main():
    """Main example function."""
    # Create client with default configuration
    client = togglr.new_client(
        api_key="42b6f8f1-630c-400c-97bd-a3454a07f700",
        base_url="http://localhost:8090",
        timeout=1.0,
        cache={"enabled": True, "max_size": 1000, "ttl_seconds": 10},
        # insecure=True,
    )
    
    # Use context manager to ensure proper cleanup
    with client:
        # Create request context
        context = RequestContext.new() \
            .with_user_id("user123") \
            .with_country("US") \
            .with_device_type("mobile") \
            .with_os("iOS") \
            .with_os_version("15.0") \
            .with_browser("Safari") \
            .with_language("en-US")
        
        # Evaluate feature flag
        try:
            value, enabled, found = client.evaluate("new_ui", context)
            if found:
                print(f"Feature enabled: {enabled}, value: {value}")
            else:
                print("Feature not found")
        except togglr.TogglrError as e:
            print(f"Error evaluating feature: {e}")
        
        # Simple enabled check
        try:
            is_enabled = client.is_enabled("new_ui", context)
            print(f"Feature is enabled: {is_enabled}")
        except togglr.FeatureNotFoundError:
            print("Feature not found")
        except togglr.TogglrError as e:
            print(f"Error checking feature: {e}")
        
        # With default value
        is_enabled = client.is_enabled_or_default("new_ui", context, default=False)
        print(f"Feature enabled (with default): {is_enabled}")
        
        # Health check
        if client.health_check():
            print("API is healthy")
        else:
            print("API is not healthy")
        
        # Example: Report an error for a feature
        try:
            client.report_error(
                feature_key="new_ui",
                error_type="timeout",
                error_message="Service did not respond in 5s",
                context={
                    "service": "payment-gateway",
                    "timeout_ms": 5000,
                    "retry_count": 3
                }
            )
            print("Error reported successfully - queued for processing")
        except togglr.TogglrError as e:
            print(f"Error reporting feature error: {e}")
        
        # Example: Get feature health status
        try:
            feature_health = client.get_feature_health("new_ui")
            print(f"Feature health: enabled={feature_health.enabled}, "
                  f"auto_disabled={feature_health.auto_disabled}")
            if feature_health.error_rate is not None:
                print(f"Error rate: {feature_health.error_rate * 100:.2f}%")
            if feature_health.last_error_at is not None:
                print(f"Last error at: {feature_health.last_error_at}")
        except togglr.TogglrError as e:
            print(f"Error getting feature health: {e}")
        
        # Example: Check if feature is healthy
        try:
            is_healthy = client.is_feature_healthy("new_ui")
            print(f"Feature is healthy: {is_healthy}")
        except togglr.TogglrError as e:
            print(f"Error checking feature health: {e}")
        
        # Example: Track events for analytics
        # Track impression event (recommended for each evaluation)
        impression_context = RequestContext.new() \
            .with_user_id("user123") \
            .with_country("US") \
            .with_device_type("mobile")
        
        impression_event = TrackEvent.new("A", EventType.SUCCESS) \
            .with_request_context(impression_context) \
            .with_dedup_key("impression-user123-new_ui")
        
        try:
            client.track_event("new_ui", impression_event)
            print("Impression event tracked successfully")
        except togglr.TogglrError as e:
            print(f"Error tracking impression event: {e}")
        
        # Track conversion event with reward
        conversion_context = RequestContext.new() \
            .with_user_id("user123") \
            .set("conversion_type", "purchase") \
            .set("order_value", 99.99)
        
        conversion_event = TrackEvent.new("A", EventType.SUCCESS) \
            .with_reward(1.0) \
            .with_request_context(conversion_context) \
            .with_dedup_key("conversion-user123-new_ui")
        
        try:
            client.track_event("new_ui", conversion_event)
            print("Conversion event tracked successfully")
        except togglr.TogglrError as e:
            print(f"Error tracking conversion event: {e}")
        
        # Track error event
        error_context = RequestContext.new() \
            .with_user_id("user123") \
            .set("error_type", "timeout") \
            .set("error_message", "Service did not respond in 5s")
        
        error_event = TrackEvent.new("B", EventType.ERROR) \
            .with_request_context(error_context) \
            .with_dedup_key("error-user123-new_ui")
        
        try:
            client.track_event("new_ui", error_event)
            print("Error event tracked successfully")
        except togglr.TogglrError as e:
            print(f"Error tracking error event: {e}")


if __name__ == "__main__":
    main()
