"""
Zone Task Manager for Home Assistant.

A comprehensive task management system organized by zones/areas in your home.
"""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN
from .logger import LOGGER_MAIN as _LOGGER, log_entry_setup

# Platforms that will be set up for this integration
PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.CALENDAR,
]


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Zone Task Manager component."""
    # Store an empty dict for our domain
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Zone Task Manager from a config entry."""
    log_entry_setup(entry.entry_id, entry.data)
    
    # Store data for this specific config entry
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "zones": {},
        "tasks": {},
        "config": entry.data,
    }
    
    # Forward the setup to configured platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    # Register services
    # TODO: Services will be registered in services.py
    
    _LOGGER.info("Zone Task Manager integration setup complete")
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a Zone Task Manager config entry."""
    _LOGGER.debug("Unloading Zone Task Manager integration")
    
    # Unload platforms
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    
    # Remove the config entry from the data store
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
        
        # If this was the last config entry, clean up the domain
        if not hass.data[DOMAIN]:
            hass.data.pop(DOMAIN)
    
    return unload_ok


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload Zone Task Manager config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry) 