import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_USERNAME, CONF_PASSWORD

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

class IStoreOSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for iStoreOS Router."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        _LOGGER.debug("iStoreOS async_step_user called")

        if user_input is not None:
            # 确保同一个 host 只能添加一次
            await self.async_set_unique_id(user_input[CONF_HOST])
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title="iStoreOS Router", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_HOST, default="192.168.1.1"): str,
                vol.Required(CONF_USERNAME, default="root"): str,
                vol.Required(CONF_PASSWORD): str,
            })
        )