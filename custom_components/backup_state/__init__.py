"""
The Backup State component for Home Assistant.
"""

import asyncio
import logging

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import HomeAssistantType

from .const import (
    DOMAIN,
    UUID,
    SW_MANUFACTURER,
    SW_NAME,
    SW_VERSION
)

CONFIG_SCHEMA = vol.Schema({DOMAIN: vol.Schema({})}, extra=vol.ALLOW_EXTRA)

PLATFORMS = ["sensor"]

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistantType, config: ConfigEntry):
    """Set up component"""
    hass.data[DOMAIN] = {}

    if DOMAIN not in config:
        return True

    return True


async def async_setup_entry(hass: HomeAssistantType, entry: ConfigEntry):
    """Load config entries"""

    hass.data[DOMAIN][entry.entry_id] = "f1e28691-9aa0-4b25-8350-ecf5128f8cd2"

    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, component)
        )

    return True


async def async_unload_entry(hass: HomeAssistantType, entry: ConfigEntry):
    """Unload config entries"""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, component)
                for component in PLATFORMS
            ]
        )
    )

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


class BackupStateDevice():
    def __init__(self, device):
        self._device = device

    @property
    def device_info(self):
        """Return device information"""
        return {
            "identifiers": {
                (DOMAIN,
                 UUID,
                 self._device)
            },
            "name": SW_NAME,
            "manufacturer": SW_MANUFACTURER,
            "model": "",
            "sw_version": SW_VERSION,
        }
