# mpcomposer
# MoviePilot Docker Compose 配置生成工具

## 📌 概述
一个基于Python的图形界面工具，用于快速生成MoviePilot的Docker Compose配置文件。通过直观的界面简化配置过程，减少手动编辑YAML文件的错误。

<img width="2031" height="1877" alt="image" src="https://github.com/user-attachments/assets/3821f938-af5b-4973-a2d7-0ce065963944" />


## ✨ 主要功能

### 🌐 网络配置
| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| 网络模式 | Host或Bridge模式 | Host |
| NGINX端口 | Web访问端口 | 3000 |
| 应用端口 | 应用程序端口 | 3001 |
| API端口 | 新增API端口 | 3002 |

### 💾 存储卷映射
```plaintext
存储位置路径1 (本地) → [容器内路径]
存储位置路径2 (本地) → [容器内路径]
配置目录 (本地) → /config (固定)
Core目录 (本地) → /moviepilot/.cache/ms-playwright (固定)
qBittorrent种子目录 (可选) → /BT_backup (固定)

## 📌 这样吧
<img width="1901" height="1705" alt="image" src="https://github.com/user-attachments/assets/923fef14-264a-4af5-9c4b-545565ce50d0" />
<img width="1905" height="1045" alt="image" src="https://github.com/user-attachments/assets/08c65c98-8e13-46ea-88d7-96d5ac804685" />
<img width="1977" height="1079" alt="image" src="https://github.com/user-attachments/assets/7fa1a1cf-2320-4f15-ad3d-fed9c30d9294" />
<img width="979" height="545" alt="image" src="https://github.com/user-attachments/assets/ff97caf2-8132-4c52-a17b-7cb0d9d0f8ec" />


