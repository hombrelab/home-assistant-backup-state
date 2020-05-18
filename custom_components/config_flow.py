"""
Config flow for the Backup State component.
"""

import logging

import voluptuous as vol

from homeassistant.components import mqtt
from homeassistant import config_entries, exceptions
from homeassistant.config_entries import ConfigFlow

from .const import (
    DOMAIN,
    NAME,
    TOPIC,
    DEFAULT_NAME,
    DEFAULT_TOPIC
)

_LOGGER = logging.getLogger(__name__)


@config_entries.HANDLERS.register(DOMAIN)
class BackupStateConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = 1

    CONNECTION_CLASS = config_entries.CONN_CLASS_UNKNOWN

    async def async_step_user(self, user_input=None):
        if user_input is None:
            return await self._show_setup_form(user_input)

        errors = {}

        try:
            for entry in self._async_current_entries():
                if user_input[NAME] == entry.data[NAME]:
                    raise ValidationError
        except ValidationError:
            errors["base"] = "name_error"
            return await self._show_setup_form(errors)

        try:
            await is_valid(user_input)
        except ValidationError:
            errors["base"] = "variables_error"
            return await self._show_setup_form(errors)

        data = {
            NAME: user_input[NAME],
            TOPIC: user_input[TOPIC],
        }

        return self.async_create_entry(
            title=user_input[NAME],
            data=data,
        )

    async def _show_setup_form(self, errors=None):
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(NAME, default=DEFAULT_NAME): str,
                    vol.Required(TOPIC, default=DEFAULT_TOPIC): str,
                }
            ),
            errors=errors or {},
        )


async def is_valid(user_input):
    if not user_input[NAME].strip():
        user_input[NAME] = DEFAULT_NAME

    if not user_input[TOPIC].strip():
        raise ValidationError


class ValidationError(exceptions.HomeAssistantError):
    """Error to indicate that data is not valid"""
