"""
Your Custom Integration for Home Assistant.

This integration provides [describe your integration's purpose].
"""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

# List of platforms supported by your integration
PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    # Platform.SWITCH,
    # Platform.BINARY_SENSOR,
    # Add other platforms as needed
]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Your Integration from a config entry."""
    _LOGGER.debug("Setting up %s integration", DOMAIN)
    
    # Store an instance of the "connecting" class that does the work of speaking
    # with your actual devices/service.
    # This is where you would create your API client, websocket connection, etc.
    hass.data.setdefault(DOMAIN, {})
    
    # Example: Create API client
    # session = async_get_clientsession(hass)
    # api_client = YourAPIClient(session, entry.data["host"], entry.data["token"])
    # hass.data[DOMAIN][entry.entry_id] = api_client
    
    # Forward the setup to the sensor platform
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.debug("Unloading %s integration", DOMAIN)
    
    # Unload platforms
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        # Remove the config entry from the hass data object
        hass.data[DOMAIN].pop(entry.entry_id, None)
        
        # If this was the last config entry, remove the domain from hass data
        if not hass.data[DOMAIN]:
            hass.data.pop(DOMAIN)
    
    return unload_ok


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry) 