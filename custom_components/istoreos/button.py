from homeassistant.components.button import ButtonEntity
from . import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    fetcher = hass.data[DOMAIN][config_entry.entry_id]["fetcher"]

    buttons = [
        IStoreOSButton(hass, config_entry, fetcher, "reboot", "reboot"),
        IStoreOSButton(hass, config_entry, fetcher, "reconnect", "ifdown wan && ifup wan"),
    ]
    async_add_entities(buttons, True)


class IStoreOSButton(ButtonEntity):
    def __init__(self, hass, config_entry, fetcher, key, command):
        self._hass = hass
        self._config_entry = config_entry
        self._fetcher = fetcher
        self._key = key
        self._command = command
        self._attr_translation_key = key
        self._attr_has_entity_name = True
        self._attr_unique_id = f"istoreos_button_{key}"

    async def async_press(self):
        await self._fetcher.rpc_exec(self._command)

    @property
    def device_info(self):
        version = self._hass.data[DOMAIN][self._config_entry.entry_id].get("firmware_version", "未知版本")
        return {
            "identifiers": {(DOMAIN, "router")},
            "name": "iStoreOS 路由器",
            "manufacturer": "iStoreOS",
            "model": f"iStoreOS {version}",
            "sw_version": version,
        }
