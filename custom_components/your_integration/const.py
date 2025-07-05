"""Constants for the Your Integration integration."""
from __future__ import annotations

# Domain for your integration - this should be unique and match your folder name
DOMAIN = "your_integration"

# Configuration keys
CONF_HOST = "host"
CONF_PORT = "port"
CONF_TOKEN = "token"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Default values
DEFAULT_PORT = 8080
DEFAULT_SCAN_INTERVAL = 30

# Attributes
ATTR_DEVICE_ID = "device_id"
ATTR_LAST_SEEN = "last_seen"

# Services (if you plan to add custom services)
SERVICE_CUSTOM_ACTION = "custom_action" 