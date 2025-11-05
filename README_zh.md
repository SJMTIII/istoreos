# iStoreOS 集成 for Home Assistant

## 简介

这是一个适用于 Home Assistant 的 iStoreOS 自定义集成，支持从 iStoreOS 路由器获取设备信息、网络状态等数据，并以优雅的方式展示在仪表盘中。

---

## 功能特点

- 实时获取连接设备列表  
- 展示设备名称、IP、MAC、在线状态等  
- 支持中文界面  
- 支持 UI 配置流程（无需 YAML）  
- 图标与品牌展示已提交至 Home Assistant 官方品牌库

---

## 安装方式

### 方法一：通过 HACS 安装（推荐）

1. 打开 Home Assistant → HACS → Integrations  
2. 点击右上角菜单 → “自定义仓库”  
3. 添加仓库地址：
类型选择：Integration  
4. 搜索 “iStoreOS” → 安装  
5. 重启 Home Assistant

### 方法二：手动安装

1. 下载本仓库代码  
2. 将 `custom_components/istoreos/` 文件夹复制到你的 Home Assistant 配置目录下：
3. 重启 Home Assistant

---

## 配置方式

集成支持 UI 配置，无需手动编辑 YAML。

1. 打开 Home Assistant → 设置 → 集成  
2. 点击右下角 “添加集成” → 搜索 “iStoreOS”  
3. 按提示输入路由器地址、账号密码等信息  
4. 保存后即可在仪表盘中查看设备状态

---

## 截图示例

（你可以在这里插入仪表盘截图或设备展示图）

---

## 官方链接

- iStoreOS 官网：[https://www.istoreos.com](https://www.istoreos.com)  
- Home Assistant：[https://www.home-assistant.io](https://www.home-assistant.io)

---

