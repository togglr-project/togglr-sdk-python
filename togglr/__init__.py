"""Togglr Python SDK for feature flag management."""

from .client import Client, ClientConfig
from .context import RequestContext
from .errors import (
    TogglrError,
    UnauthorizedError,
    BadRequestError,
    NotFoundError,
    InternalServerError,
    TooManyRequestsError,
    FeatureNotFoundError,
)
from .version import __version__

# Import generated models
from internal.generated.togglr_client.models.feature_error_report import FeatureErrorReport
from internal.generated.togglr_client.models.feature_health import FeatureHealth

__all__ = [
    "Client",
    "ClientConfig", 
    "RequestContext",
    "TogglrError",
    "UnauthorizedError",
    "BadRequestError",
    "NotFoundError",
    "InternalServerError",
    "TooManyRequestsError",
    "FeatureNotFoundError",
    "FeatureErrorReport",
    "FeatureHealth",
    "__version__",
]

__version__ = "1.0.0"
