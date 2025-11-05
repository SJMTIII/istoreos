# iStoreOS Integration for Home Assistant
![iStoreOS Logo](images/https://private-user-images.githubusercontent.com/123294890/509940000-2f8623da-ff5e-48f5-bdce-884f1fea8f91.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjIzMjA2ODYsIm5iZiI6MTc2MjMyMDM4NiwicGF0aCI6Ii8xMjMyOTQ4OTAvNTA5OTQwMDAwLTJmODYyM2RhLWZmNWUtNDhmNS1iZGNlLTg4NGYxZmVhOGY5MS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTEwNVQwNTI2MjZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04ZDJjOGUxNTg1Yzc2NGUyNmE2N2I3MjJlNzY4M2QwZDNjNmFkODI4MzNhY2JjM2IwNDEzZjczZDFmODBlZjFjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.1u1WQKlLWk5ziG6Vz6Pg0W9SeV_24ysM4_lIOdGwIwQ)
[English](README.md) | [中文](README_zh.md)

## Introduction

This is a custom integration for Home Assistant that connects to iStoreOS routers, providing device info, network status, and elegant dashboard presentation.


---

## Features

- Real-time connected device list  
- Display device name, IP, MAC, online status  
- Multi-language support (English/Chinese)  
- UI configuration flow (no YAML required)  

---

## Installation

### Option 1: Install via HACS (Recommended)
[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=SJMTIII&repository=istoreos)
1. Open Home Assistant → HACS → Integrations  
2. Click the top-right menu → “Custom repositories”  
3. Add repository URL:
Select type: Integration  
4. Search for “iStoreOS” → Install  
5. Restart Home Assistant

### Option 2: Manual Installation

1. Download this repository  
2. Copy the `custom_components/istoreos/` folder into your Home Assistant config directory:
3. Restart Home Assistant

---

## Configuration

This integration supports UI configuration, no YAML required.

1. Open Home Assistant → Settings → Integrations  
2. Click “Add Integration” → Search for “iStoreOS”  
3. Enter router address, username, and password as prompted  
4. Save and view device status on the dashboard

---

## Screenshots

(Insert dashboard or device screenshots here)

---

## Official Links

- iStoreOS Website: [https://www.istoreos.com](https://www.istoreos.com)  
- Home Assistant: [https://www.home-assistant.io](https://www.home-assistant.io)

---

