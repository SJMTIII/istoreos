import aiohttp
import re
import logging

_LOGGER = logging.getLogger(__name__)

def parse_uptime(uptime_str: str):
    match = re.search(r"up\s+(\d+)\s+days?,\s+(\d+):(\d+)", uptime_str)
    if match:
        return map(int, match.groups())
    match = re.search(r"up\s+(\d+):(\d+)", uptime_str)
    if match:
        return 0, *map(int, match.groups())
    return 0, 0, 0

class DataFetcher:
    def __init__(self, host, username, password):
        self._host = host
        self._username = username
        self._password = password
        self._session = aiohttp.ClientSession()
        self._token = None

    async def login(self):
        url = f"http://{self._host}/cgi-bin/luci/rpc/auth"
        payload = {"id": 1, "method": "login", "params": [self._username, self._password]}
        async with self._session.post(url, json=payload) as resp:
            data = await resp.json()
            self._token = data.get("result")
            _LOGGER.debug("Got token: %s", self._token)

    async def rpc_exec(self, command):
        if not self._token:
            await self.login()
        url = f"http://{self._host}/cgi-bin/luci/rpc/sys?auth={self._token}"
        payload = {"id": 1, "method": "exec", "params": [command]}
        async with self._session.post(url, json=payload) as resp:
            return await resp.json()

    async def get_firmware_version(self):
        try:
            data = await self.rpc_exec("cat /etc/os-release")
            text = data.get("result", "")
            match = re.search(r'VERSION="(.+?)"', text)
            return match.group(1) if match else "未知版本"
        except Exception as e:
            _LOGGER.warning("获取固件版本失败: %s", e)
            return "未知版本"

    async def fetch_status(self):
        result = {}

        # Uptime & Load
        uptime_data = await self.rpc_exec("uptime")
        uptime_str = uptime_data.get("result", "")
        result["uptime_raw"] = uptime_str.strip()

        load_match = re.search(r"load average: ([0-9.]+), ([0-9.]+), ([0-9.]+)", uptime_str)
        if load_match:
            load1, load5, load15 = map(float, load_match.groups())
            result.update({
                "load_1min": load1,
                "load_5min": load5,
                "load_15min": load15,
                "load_summary": f"{load1} / {load5} / {load15}"
            })

        days, hours, minutes = parse_uptime(uptime_str)
        result.update({
            "uptime_days": days,
            "uptime_hours": hours,
            "uptime_minutes": minutes,
            "uptime_human": f"{days} 天 {hours} 小时" if days else f"{hours} 小时 {minutes} 分钟"
        })

        # Memory
        mem_data = await self.rpc_exec("free")
        mem_str = mem_data.get("result", "")
        mem_match = re.search(r"Mem:\s+(\d+)\s+(\d+)\s+(\d+)\s+\d+\s+(\d+)\s+(\d+)", mem_str)
        if mem_match:
            total, used, free, buff_cache, available = map(int, mem_match.groups())
            used_percent = round(used / total * 100, 2)
            result.update({
                "mem_total": total,
                "mem_used": used,
                "mem_free": free,
                "mem_available": available,
                "mem_used_percent": used_percent,
                "mem_used_mb": round(used / 1024, 1),
                "mem_total_mb": round(total / 1024, 1),
                "mem_free_mb": round(free / 1024, 1),
                "mem_available_mb": round(available / 1024, 1),
                "mem_summary": f"{round(used / 1024, 1)} MB / {round(total / 1024, 1)} MB ({used_percent}%)"
            })

        # Online devices
        arp_data = await self.rpc_exec("cat /proc/net/arp")
        arp_str = arp_data.get("result", "")
        result["online_devices"] = sum(
            1 for line in arp_str.splitlines()
            if "br-lan" in line and "0x2" in line
        )

        # WAN IP
        wan_ip = None
        wan_data = await self.rpc_exec("ubus call network.interface.wan status")
        wan_str = wan_data.get("result", "")
        match = re.search(r'"address":\s*"([\d\.]+)"', wan_str)
        if match:
            wan_ip = match.group(1)
        else:
            ipify = await self.rpc_exec("curl -s https://api.ipify.org")
            wan_ip = ipify.get("result", "").strip()
        result["wan_ip"] = wan_ip

        # Connections
        conn_data = await self.rpc_exec("cat /proc/sys/net/netfilter/nf_conntrack_count")
        conn_str = conn_data.get("result", "").strip()
        result["connections"] = int(conn_str) if conn_str.isdigit() else None

        return result

    async def close(self):
        await self._session.close()
