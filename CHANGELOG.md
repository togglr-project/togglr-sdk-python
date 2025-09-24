# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-XX

### Added
- Initial release of togglr-sdk-python
- Support for feature flag evaluation
- Request context with predefined attributes
- Caching support with TTL
- Retry logic with exponential backoff
- Health check functionality
- Comprehensive error handling
- Type hints throughout
- Unit tests
- Examples and documentation
- OpenAPI client generation from specs/sdk.yml
- CLI for client generation
- Makefile for common tasks

### Features
- **Client**: Main client for feature flag evaluation
- **RequestContext**: Builder pattern for request context
- **Configuration**: Flexible configuration with method chaining
- **Caching**: Optional LRU cache with TTL
- **Error Handling**: Specific error types for different scenarios
- **Logging**: Optional custom logger support
- **Metrics**: Optional custom metrics support
- **Retries**: Configurable retry logic with backoff
- **Health Checks**: API health monitoring

### API
- `Client.evaluate(feature_key, context)` - Full feature evaluation
- `Client.is_enabled(feature_key, context)` - Simple enabled check
- `Client.is_enabled_or_default(feature_key, context, default)` - Check with fallback
- `Client.health_check()` - API health check
- `RequestContext.new()` - Create new context
- `RequestContext.with_*()` - Chainable context builders
- `ClientConfig.default(api_key)` - Create default config
- `ClientConfig.with_*()` - Chainable config builders

### Dependencies
- httpx >= 0.24.0
- pydantic >= 2.0.0
- typing-extensions >= 4.0.0
- cachetools >= 5.3.0 (optional)
