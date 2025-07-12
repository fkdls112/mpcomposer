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
