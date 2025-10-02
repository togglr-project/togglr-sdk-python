#!/usr/bin/env python3
"""Simple example of using togglr-sdk-python."""

import togglr
from togglr import Client, RequestContext


def main():
    """Main example function."""
    # Create client with default configuration
    client = togglr.new_client(
        api_key="your-api-key-here",
        base_url="http://localhost:8090",
        timeout=1.0,
        cache={"enabled": True, "max_size": 1000, "ttl_seconds": 10}
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
            health, is_pending = client.report_error(
                feature_key="new_ui",
                error_type="timeout",
                error_message="Service did not respond in 5s",
                context={
                    "service": "payment-gateway",
                    "timeout_ms": 5000,
                    "retry_count": 3
                }
            )
            print(f"Feature health after error report: enabled={health.enabled}, "
                  f"auto_disabled={health.auto_disabled}, pending_change={is_pending}")
            if health.error_rate is not None:
                print(f"Error rate: {health.error_rate * 100:.2f}%")
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


if __name__ == "__main__":
    main()
