# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - 2025-01-02

### Changed
- **Error Reporting API Simplification**: Updated error reporting to use asynchronous processing
  - `report_error(feature_key, error_type, error_message, context)` - Now returns `None` (simplified API)
  - 202 responses now always indicate successful queuing for processing (no more pending changes)
  - Removed `is_pending` return value as it's no longer needed

### Added
- **Error Reporting**: New methods for reporting feature execution errors
  - `report_error(feature_key, error_type, error_message, context)` - Report a single error with automatic retries, returns `None`
  - Support for different error types (timeout, validation, service_unavailable, etc.)
  - Context data support for error reports

- **Feature Health Monitoring**: New methods for monitoring feature health
  - `get_feature_health(feature_key)` - Get detailed health status with automatic retries
  - `is_feature_healthy(feature_key)` - Simple boolean health check

- **New Types**:
  - `FeatureErrorReport` - Structure for error reporting (from generated client)
  - `FeatureHealth` - Structure for health monitoring with detailed information
  - Support for 202 responses with `is_pending` boolean return value

- **Enhanced Examples**:
  - Updated simple example with error reporting and health monitoring
  - Updated advanced example demonstrating comprehensive usage
  - Error reporting examples with different error types
  - Health monitoring examples

### Changed
- **Retry Logic**: All methods now automatically apply retries based on client configuration
- **202 Response Handling**: 202 responses now return `(health, is_pending)` with `is_pending = True` instead of error
- **Generated Client Integration**: Now uses generated OpenAPI client for new endpoints
- **Code Cleanup**: Removed unnecessary fallback imports and simplified client code
- Updated README with comprehensive documentation for new features
- Enhanced error handling and response processing
- Improved example structure and organization

### Technical Details
- Full integration with generated OpenAPI client
- Automatic retry logic based on client configuration
- Proper handling of 202 responses with pending change indication
- Backward compatible - no breaking changes to existing API
- Type hints for all new methods and return values

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
