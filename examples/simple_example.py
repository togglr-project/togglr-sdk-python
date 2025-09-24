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


if __name__ == "__main__":
    main()
