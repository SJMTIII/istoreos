from homeassistant.components.sensor import SensorEntity
from . import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    fetcher = hass.data[DOMAIN][config_entry.entry_id]["fetcher"]

    sensors = [
        # CPU
        IStoreOSSensor(hass, config_entry, fetcher, "load_1min", "load"),
        IStoreOSSensor(hass, config_entry, fetcher, "load_5min", "load"),
        IStoreOSSensor(hass, config_entry, fetcher, "load_15min", "load"),
        IStoreOSSensor(hass, config_entry, fetcher, "load_summary", None),

        # 内存
        IStoreOSSensor(hass, config_entry, fetcher, "mem_used_percent", "%"),
        IStoreOSSensor(hass, config_entry, fetcher, "mem_used_mb", "MB"),
        IStoreOSSensor(hass, config_entry, fetcher, "mem_total_mb", "MB"),
        IStoreOSSensor(hass, config_entry, fetcher, "mem_available_mb", "MB"),
        IStoreOSSensor(hass, config_entry, fetcher, "mem_free_mb", "MB"),
        IStoreOSSensor(hass, config_entry, fetcher, "mem_summary", None),

        # 网络
        IStoreOSSensor(hass, config_entry, fetcher, "wan_ip", None),
        IStoreOSSensor(hass, config_entry, fetcher, "connections", "connections"),

        # 其他
        IStoreOSSensor(hass, config_entry, fetcher, "online_devices", "devices"),
        IStoreOSSensor(hass, config_entry, fetcher, "uptime_human", None),
    ]
    async_add_entities(sensors, True)


class IStoreOSSensor(SensorEntity):
    def __init__(self, hass, config_entry, fetcher, key, unit):
        self._hass = hass
        self._config_entry = config_entry
        self._fetcher = fetcher
        self._key = key
        self._attr_translation_key = key
        self._attr_has_entity_name = True
        self._attr_native_unit_of_measurement = unit
        self._attr_unique_id = f"istoreos_{key}"
        self._state = None

        self._attr_icon = {
            "load_1min": "mdi:chip",
            "load_5min": "mdi:chip",
            "load_15min": "mdi:chip",
            "load_summary": "mdi:chip",
            "mem_used_percent": "mdi:memory",
            "mem_used_mb": "mdi:memory",
            "mem_total_mb": "mdi:memory",
            "mem_available_mb": "mdi:memory",
            "mem_free_mb": "mdi:memory",
            "mem_summary": "mdi:memory",
            "wan_ip": "mdi:ip-network",
            "connections": "mdi:connection",
            "online_devices": "mdi:lan-connect",
            "uptime_human": "mdi:clock-outline",
        }.get(key, "mdi:router-network")

    async def async_update(self):
        data = await self._fetcher.fetch_status()
        self._state = data.get(self._key)

    @property
    def native_value(self):
        return self._state

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
