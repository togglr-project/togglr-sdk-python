# Togglr Python SDK Makefile

.PHONY: help install dev-install generate build test lint format clean

# Default target
help:
	@echo "Available targets:"
	@echo "  install      - Install the package"
	@echo "  dev-install  - Install with development dependencies"
	@echo "  generate     - Generate client from OpenAPI spec"
	@echo "  build        - Build the package"
	@echo "  test         - Run tests"
	@echo "  lint         - Run linting"
	@echo "  format       - Format code"
	@echo "  clean        - Clean generated files"

# Installation
install:
	pip install -e .

dev-install:
	pip install -e ".[dev]"

# Generate client from OpenAPI spec
generate:
	@echo "Generating client from OpenAPI specification..."
	@mkdir -p internal/generated
	openapi-generator-cli generate \
		-i ../togglr/specs/sdk.yml \
		-g python \
		-o internal/generated \
		--package-name togglr_client \
		--additional-properties=packageName=togglr_client,projectName=togglr-sdk-python,packageVersion=1.0.0

# Build package
build:
	python -m build

# Testing
test:
	pytest

# Linting
lint:
	flake8 togglr tests
	mypy togglr

# Format code
format:
	black togglr tests examples
	isort togglr tests examples

# Clean generated files
clean:
	rm -rf internal/generated/*
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
