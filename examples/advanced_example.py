#!/usr/bin/env python3
"""Advanced example of using togglr-sdk-python with custom configuration."""

import time
from typing import Any, Dict

import togglr
from togglr import Client, ClientConfig, RequestContext


class CustomLogger:
    """Custom logger implementation."""
    
    def __call__(self, message: str, **kwargs) -> None:
        """Log a message with optional context."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        context = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(f"[{timestamp}] {message}" + (f" ({context})" if context else ""))


class CustomMetrics:
    """Custom metrics implementation."""
    
    def __init__(self):
        self.evaluate_requests = 0
        self.cache_hits = 0
        self.cache_misses = 0
        self.errors = 0
    
    def inc_evaluate_request(self) -> None:
        """Increment evaluate request counter."""
        self.evaluate_requests += 1
    
    def inc_cache_hit(self) -> None:
        """Increment cache hit counter."""
        self.cache_hits += 1
    
    def inc_cache_miss(self) -> None:
        """Increment cache miss counter."""
        self.cache_misses += 1
    
    def inc_evaluate_error(self, error_code: str) -> None:
        """Increment error counter."""
        self.errors += 1
    
    def observe_evaluate_latency(self, latency: float) -> None:
        """Observe evaluation latency."""
        pass  # Implement latency tracking if needed
    
    def print_stats(self) -> None:
        """Print current metrics."""
        print(f"Metrics: requests={self.evaluate_requests}, "
              f"cache_hits={self.cache_hits}, cache_misses={self.cache_misses}, "
              f"errors={self.errors}")


def main():
    """Main advanced example function."""
    # Create custom logger and metrics
    logger = CustomLogger()
    metrics = CustomMetrics()
    
    # Create custom configuration
    config = ClientConfig.default("your-api-key-here") \
        .with_base_url("http://localhost:8090") \
        .with_timeout(2.0) \
        .with_retries(3) \
        .with_cache(enabled=True, max_size=500, ttl_seconds=30) \
        .with_backoff(base_delay=0.2, max_delay=5.0, factor=1.5) \
        .with_logger(logger) \
        .with_metrics(metrics)
    
    # Create client with custom configuration
    client = Client(config)
    
    try:
        # Test health check
        if not client.health_check():
            print("API is not healthy, exiting")
            return
        
        # Create different contexts for testing
        contexts = [
            RequestContext.new()
                .with_user_id("user1")
                .with_country("US")
                .with_device_type("desktop")
                .with_os("Windows")
                .with_browser("Chrome"),
            
            RequestContext.new()
                .with_user_id("user2")
                .with_country("RU")
                .with_device_type("mobile")
                .with_os("Android")
                .with_os_version("12.0")
                .with_language("ru-RU"),
            
            RequestContext.new()
                .with_user_id("user3")
                .with_country("DE")
                .with_device_type("tablet")
                .with_os("iOS")
                .with_os_version("16.0")
                .with_browser("Safari")
                .with_language("de-DE")
                .with_age(25)
                .with_gender("female")
        ]
        
        # Test different feature flags
        feature_keys = ["new_ui", "beta_features", "premium_content", "dark_mode"]
        
        for i, context in enumerate(contexts):
            print(f"\n--- Testing context {i+1} ---")
            print(f"Context: {context.to_dict()}")
            
            for feature_key in feature_keys:
                try:
                    # Full evaluation
                    value, enabled, found = client.evaluate(feature_key, context)
                    if found:
                        print(f"  {feature_key}: enabled={enabled}, value={value}")
                    else:
                        print(f"  {feature_key}: not found")
                    
                    # Simple enabled check with default
                    is_enabled = client.is_enabled_or_default(feature_key, context, default=False)
                    print(f"  {feature_key} (with default): {is_enabled}")
                    
                except togglr.TogglrError as e:
                    print(f"  {feature_key}: error - {e}")
        
        # Print metrics
        print("\n--- Metrics ---")
        metrics.print_stats()
        
        # Test caching by evaluating the same feature multiple times
        print("\n--- Testing cache ---")
        context = contexts[0]
        feature_key = "new_ui"
        
        for i in range(5):
            start_time = time.time()
            try:
                value, enabled, found = client.evaluate(feature_key, context)
                elapsed = time.time() - start_time
                print(f"  Attempt {i+1}: {elapsed:.3f}s, enabled={enabled}, value={value}")
            except togglr.TogglrError as e:
                print(f"  Attempt {i+1}: error - {e}")
        
        # Print final metrics
        print("\n--- Final Metrics ---")
        metrics.print_stats()
        
    finally:
        client.close()


if __name__ == "__main__":
    main()
