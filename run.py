#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MoviePilot Docker Compose 配置生成工具 v3.1
基于 MoviePilot v2.11.0 app/core/config.py 环境变量定义
所有配置项严格对应官方源码，无虚构变量
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime

# ═══════════════════════════════════════════════
# 配置定义：所有字段严格来自 MoviePilot config.py
# ═══════════════════════════════════════════════

CONFIG_SECTIONS = [
    {
        "title": "🌐 基本设置",
        "vars": [
            ("NGINX_PORT", "Web端口", "3000", "前端访问端口"),
            ("PORT", "API端口", "3001", "后端API端口"),
            ("TZ", "时区", "Asia/Shanghai", "容器时区"),
            ("SUPERUSER", "管理员用户名", "admin", "WebUI登录账号"),
            ("API_TOKEN", "API密钥", "moviepilot", "API认证令牌，建议修改"),
            ("APP_DOMAIN", "外网域名", "", "如 https://movie.yourdomain.com"),
            ("WALLPAPER", "登录页海报", "tmdb", "tmdb / bing"),
            ("MOVIEPILOT_AUTO_UPDATE", "自动更新", "release", "release / beta / dev"),
            ("PROXY_HOST", "网络代理", "", "格式 IP:PORT，如 192.168.1.1:7890"),
        ]
    },
    {
        "title": "🎬 媒体相关",
        "vars": [
            ("TMDB_API_KEY", "TMDB API Key", "", "https://www.themoviedb.org 申请"),
            ("SEARCH_SOURCE", "搜索来源", "themoviedb,douban,bangumi", "多个用逗号分隔"),
            ("RECOGNIZE_SOURCE", "识别来源", "themoviedb", "themoviedb / douban"),
            ("SCRAP_SOURCE", "刮削来源", "themoviedb", "themoviedb / douban"),
            ("AUTH_SITE", "认证站点", "", "iyuu / ptp / hdb"),
        ]
    },
    {
        "title": "📁 下载路径 (v2.11新增)",
        "vars": [
            ("DOWNLOAD_PATH", "通用下载路径", "", "统一下载目录"),
            ("DOWNLOAD_MOVIE_PATH", "电影下载路径", "", "单独设置电影路径"),
            ("DOWNLOAD_TV_PATH", "电视剧下载路径", "", "单独设置电视剧路径"),
            ("DOWNLOAD_ANIME_PATH", "动漫下载路径", "", "单独设置动漫路径"),
            ("DOWNLOAD_CATEGORY", "按类别分目录", "false", "true / false"),
        ]
    },
    {
        "title": "📚 媒体库配置 (v2.11新增)",
        "vars": [
            ("LIBRARY_PATH", "媒体库根目录", "", "媒体库所在路径"),
            ("LIBRARY_MOVIE_NAME", "电影库名称", "电影", ""),
            ("LIBRARY_TV_NAME", "电视剧库名称", "电视剧", ""),
            ("LIBRARY_ANIME_NAME", "动漫库名称", "", "可选"),
            ("LIBRARY_CATEGORY", "媒体库分类", "true", "true / false"),
        ]
    },
    {
        "title": "⬇️ 下载器配置",
        "vars": [
            ("DOWNLOADER", "下载器", "qbittorrent", "qbittorrent / transmission"),
            ("DOWNLOADER_MONITOR", "监控下载器", "true", "true / false"),
            ("QB_HOST", "qBittorrent地址", "", "IP:PORT"),
            ("QB_USER", "qBittorrent用户名", "", ""),
            ("QB_PASSWORD", "qBittorrent密码", "", ""),
            ("TORRENT_TAG", "种子标签", "MOVIEPILOT", ""),
            ("TR_HOST", "Transmission地址", "", "IP:PORT (可选)"),
            ("TR_USER", "Transmission用户名", "", "可选"),
            ("TR_PASSWORD", "Transmission密码", "", "可选"),
        ]
    },
    {
        "title": "🖥️ 媒体服务器",
        "vars": [
            ("MEDIASERVER", "媒体服务器", "emby", "emby / jellyfin / plex"),
            ("EMBY_HOST", "Emby地址", "", "IP:PORT"),
            ("EMBY_API_KEY", "Emby API Key", "", ""),
            ("JELLYFIN_HOST", "Jellyfin地址", "", "IP:PORT (可选)"),
            ("JELLYFIN_API_KEY", "Jellyfin API Key", "", "可选"),
            ("PLEX_HOST", "Plex地址", "", "IP:PORT (可选)"),
            ("PLEX_TOKEN", "Plex Token", "", "可选"),
        ]
    },
    {
        "title": "📢 通知渠道",
        "vars": [
            ("MESSAGER", "通知方式", "webpush", "webpush / telegram / wechat / slack"),
            ("WECHAT_CORPID", "企业微信CorpID", "", "可选"),
            ("WECHAT_APP_SECRET", "企业微信Secret", "", "可选"),
            ("WECHAT_APP_ID", "企业微信AgentID", "", "可选"),
            ("TELEGRAM_TOKEN", "Telegram Bot Token", "", "可选"),
            ("TELEGRAM_CHAT_ID", "Telegram Chat ID", "", "可选"),
        ]
    },
    {
        "title": "☁️ CookieCloud",
        "vars": [
            ("COOKIECLOUD_HOST", "CookieCloud地址", "https://movie-pilot.org/cookiecloud", ""),
            ("COOKIECLOUD_KEY", "用户KEY", "", ""),
            ("COOKIECLOUD_PASSWORD", "加密密码", "", "端对端加密"),
            ("COOKIECLOUD_INTERVAL", "同步间隔(分钟)", "1440", "默认24小时"),
        ]
    },
    {
        "title": "🔧 高级选项",
        "vars": [
            ("BIG_MEMORY_MODE", "大内存模式", "false", "true / false"),
            ("GITHUB_TOKEN", "GitHub Token", "", "ghp_xxxx 提高API限流"),
            ("GITHUB_PROXY", "GitHub代理", "", "如 https://mirror.ghproxy.com/"),
            ("AUTO_UPDATE_RESOURCE", "自动更新站点资源", "false", "true / false"),
            ("TRANSFER_TYPE", "转移方式", "copy", "copy / move / link / softlink"),
            ("DOWNLOAD_SUBTITLE", "下载字幕", "true", "true / false"),
            ("SUBSCRIBE_MODE", "订阅模式", "spider", "spider / rss"),
            ("SCRAP_FOLLOW_TMDB", "跟随TMDB变更", "true", "true / false"),
        ]
    },
]

# Docker层面的可选变量（非MoviePilot env vars）
DOCKER_EXTRA = [
    ("PUID", "用户ID", "1000", "Docker安全上下文"),
    ("PGID", "用户组ID", "1000", "Docker安全上下文"),
    ("UMASK", "文件掩码", "022", "Docker安全上下文"),
]


# ═══════════════════════════════════════════════
# GUI 主程序
# ═══════════════════════════════════════════════

class MoviePilotComposer:
    """MoviePilot Compose 配置生成器"""

    def __init__(self, root):
        self.root = root
        self.root.title("MoviePilot Compose 配置生成工具 v3.1")
        self.root.geometry("900x700")
        self.root.minsize(700, 600)

        # 存储所有输入框的变量
        self.entries = {}
        self.section_frames = {}  # 存储每个分组的折叠内容Frame
        self.section_expanded = {}  # 记录折叠状态

        self.build_ui()

    def build_ui(self):
        """构建界面"""
        # 顶栏
        top_bar = ttk.Frame(self.root)
        top_bar.pack(fill=tk.X, padx=10, pady=(10, 0))

        ttk.Label(top_bar, text="MoviePilot Docker Compose 配置生成工具 v3.0",
                  font=("Microsoft YaHei", 13, "bold")).pack(side=tk.LEFT)

        # 网络模式选择
        net_frame = ttk.Frame(top_bar)
        net_frame.pack(side=tk.RIGHT)
        ttk.Label(net_frame, text="网络模式:").pack(side=tk.LEFT, padx=(0, 5))
        self.network_mode = tk.StringVar(value="host")
        ttk.Combobox(net_frame, textvariable=self.network_mode,
                     values=["host", "bridge"], state="readonly", width=8).pack(side=tk.LEFT)

        # 画布滚动区域
        canvas_frame = ttk.Frame(self.root)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.canvas = tk.Canvas(canvas_frame, highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)

        self.scroll_frame = ttk.Frame(self.canvas)
        self.scroll_frame.bind("<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw", tags="inner")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 鼠标滚轮支持
        self.canvas.bind("<Enter>", self._bind_mousewheel)
        self.canvas.bind("<Leave>", self._unbind_mousewheel)

        # 创建所有配置分组
        for i, section in enumerate(CONFIG_SECTIONS):
            self._create_section(i, section)

        # Docker额外选项
        self._create_section(len(CONFIG_SECTIONS), {
            "title": "🐳 Docker安全上下文 (可选)",
            "vars": DOCKER_EXTRA
        })

        # 存储卷映射
        self._create_volumes_section()

        # 底部按钮栏
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(fill=tk.X, padx=10, pady=(5, 10))

        ttk.Button(btn_frame, text="🔄 恢复默认值", command=self._reset_defaults,
                   width=15).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text="⚙️ 生成 Compose 文件", command=self.generate_compose,
                   width=20).pack(side=tk.LEFT, padx=5)
        self.save_btn = ttk.Button(btn_frame, text="💾 保存到文件", command=self.save_compose,
                                    state=tk.DISABLED, width=15)
        self.save_btn.pack(side=tk.LEFT, padx=5)

        # 结果显示区
        result_frame = ttk.LabelFrame(self.root, text="生成的 docker-compose.yml", padding=5)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        self.result_text = tk.Text(result_frame, wrap=tk.NONE, height=12,
                                    font=("Consolas", 10))
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

        # 水平滚动条
        h_scroll = ttk.Scrollbar(result_frame, orient="horizontal", command=self.result_text.xview)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.result_text.config(xscrollcommand=h_scroll.set)

    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _create_section(self, index, section):
        """创建手风琴式分组"""
        # 标题栏
        header_frame = ttk.Frame(self.scroll_frame)
        header_frame.pack(fill=tk.X, pady=(3, 0))

        title = section["title"].split(" (")[0]  # 去除括号中的额外信息

        # 点击展开/折叠
        self.section_expanded[index] = tk.BooleanVar(value=True)

        header_btn = ttk.Label(header_frame, text=f"▼ {section['title']}",
                               font=("Microsoft YaHei", 10, "bold"),
                               cursor="hand2", padding=(5, 3))
        header_btn.pack(fill=tk.X)

        # 内容区域
        content_frame = ttk.LabelFrame(self.scroll_frame, padding=8)
        content_frame.pack(fill=tk.X, padx=2, pady=(0, 2))
        self.section_frames[index] = content_frame

        # 点击事件
        def toggle_section(idx=index, btn=header_btn, frame=content_frame):
            if self.section_expanded[idx].get():
                frame.pack_forget()
                btn.config(text=f"▶ {section['title']}")
                self.section_expanded[idx].set(False)
            else:
                frame.pack(fill=tk.X, padx=2, pady=(0, 2),
                          before=self.scroll_frame.winfo_children()[
                              list(self.scroll_frame.winfo_children()).index(header_frame) + 1
                          ])
                btn.config(text=f"▼ {section['title']}")
                self.section_expanded[idx].set(True)
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        header_btn.bind("<Button-1>", lambda e, i=index: toggle_section(i))

        # 创建输入字段
        vars_list = section["vars"]
        cols = 2 if len(vars_list) > 4 else 1

        for j, (name, label, default, hint) in enumerate(vars_list):
            row = j // cols
            col = (j % cols) * 2

            inner = ttk.Frame(content_frame)
            inner.grid(row=row, column=col, columnspan=2, sticky="ew", padx=3, pady=1)

            ttk.Label(inner, text=f"{label}:", width=18, anchor="e").pack(side=tk.LEFT, padx=(0, 3))
            entry = ttk.Entry(inner)
            entry.insert(0, default)
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            if hint:
                ttk.Label(inner, text=f" {hint}", foreground="gray",
                         font=("Microsoft YaHei", 8)).pack(side=tk.LEFT)

            self.entries[name] = entry

        # 列权重
        if cols == 2:
            content_frame.columnconfigure(0, weight=1)
            content_frame.columnconfigure(2, weight=1)

    def _create_volumes_section(self):
        """创建存储卷映射分组"""
        index = len(CONFIG_SECTIONS) + 1
        section_title = "💾 存储卷映射"

        header_frame = ttk.Frame(self.scroll_frame)
        header_frame.pack(fill=tk.X, pady=(3, 0))

        self.section_expanded[index] = tk.BooleanVar(value=True)
        header_btn = ttk.Label(header_frame, text=f"▼ {section_title}",
                               font=("Microsoft YaHei", 10, "bold"),
                               cursor="hand2", padding=(5, 3))
        header_btn.pack(fill=tk.X)

        content_frame = ttk.LabelFrame(self.scroll_frame, padding=8)
        content_frame.pack(fill=tk.X, padx=2, pady=(0, 2))
        self.section_frames[index] = content_frame

        # 点击折叠
        def toggle(idx=index, btn=header_btn, frame=content_frame):
            if self.section_expanded[idx].get():
                frame.pack_forget()
                btn.config(text=f"▶ {section_title}")
                self.section_expanded[idx].set(False)
            else:
                frame.pack(fill=tk.X, padx=2, pady=(0, 2))
                btn.config(text=f"▼ {section_title}")
                self.section_expanded[idx].set(True)
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        header_btn.bind("<Button-1>", lambda e: toggle())

        # 卷映射字段
        vol_config = [
            ("CONFIG_DIR", "配置目录", "/mnt/user/docker/moviepilot/config", "→ /config"),
            ("MEDIA_DIR", "媒体目录", "/mnt/user/media", "→ /media"),
            ("DOWNLOAD_DIR", "下载目录", "/mnt/user/downloads", "→ /downloads"),
            ("BT_BACKUP_DIR", "BT备份目录(可选)", "", "→ /BT_backup"),
        ]

        for j, (name, label, default, hint) in enumerate(vol_config):
            inner = ttk.Frame(content_frame)
            inner.grid(row=j, column=0, sticky="ew", padx=3, pady=1)

            ttk.Label(inner, text=f"{label}:", width=18, anchor="e").pack(side=tk.LEFT, padx=(0, 3))
            entry = ttk.Entry(inner)
            entry.insert(0, default)
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            ttk.Label(inner, text=hint, foreground="gray",
                     font=("Microsoft YaHei", 8)).pack(side=tk.LEFT)
            self.entries[name] = entry

    def _reset_defaults(self):
        """恢复所有默认值"""
        for section in CONFIG_SECTIONS:
            for name, _, default, _ in section["vars"]:
                if name in self.entries:
                    self.entries[name].delete(0, tk.END)
                    self.entries[name].insert(0, default)
        for name, _, default, _ in DOCKER_EXTRA:
            if name in self.entries:
                self.entries[name].delete(0, tk.END)
                self.entries[name].insert(0, default)
        # 恢复卷映射默认值
        defaults_vol = {
            "CONFIG_DIR": "/mnt/user/docker/moviepilot/config",
            "MEDIA_DIR": "/mnt/user/media",
            "DOWNLOAD_DIR": "/mnt/user/downloads",
            "BT_BACKUP_DIR": "",
        }
        for name, val in defaults_vol.items():
            if name in self.entries:
                self.entries[name].delete(0, tk.END)
                self.entries[name].insert(0, val)
        self.network_mode.set("host")

    def generate_compose(self):
        """生成 docker-compose.yml"""
        network_mode = self.network_mode.get()
        nginx_port = self.entries.get("NGINX_PORT", None)
        nginx_port = nginx_port.get() if nginx_port else "3000"
        port = self.entries.get("PORT", None)
        port = port.get() if port else "3001"

        # 收集环境变量
        env_lines = []
        for section in CONFIG_SECTIONS:
            for name, label, default, hint in section["vars"]:
                val = self.entries.get(name, None)
                val = val.get().strip() if val else ""
                if val:
                    env_lines.append(f"            - '{name}={val}'")

        # Docker额外变量
        for name, _, default, _ in DOCKER_EXTRA:
            val = self.entries.get(name, None)
            val = val.get().strip() if val else ""
            if val:
                env_lines.append(f"            - '{name}={val}'")

        # 卷映射
        volumes = ["            - '/var/run/docker.sock:/var/run/docker.sock:ro'"]
        config_dir = self.entries.get("CONFIG_DIR")
        config_dir = config_dir.get().strip() if config_dir else ""
        if config_dir:
            volumes.append(f"            - '{config_dir}:/config'")

        media_dir = self.entries.get("MEDIA_DIR")
        media_dir = media_dir.get().strip() if media_dir else ""
        if media_dir:
            volumes.append(f"            - '{media_dir}:/media'")

        download_dir = self.entries.get("DOWNLOAD_DIR")
        download_dir = download_dir.get().strip() if download_dir else ""
        if download_dir:
            volumes.append(f"            - '{download_dir}:/downloads'")

        bt_dir = self.entries.get("BT_BACKUP_DIR")
        bt_dir = bt_dir.get().strip() if bt_dir else ""
        if bt_dir:
            volumes.append(f"            - '{bt_dir}:/BT_backup'")

        # 构建 Compose 内容
        compose = f"""# ============================================
# MoviePilot v2.11.0 Docker Compose 配置
# 生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
# 生成工具: mpcomposer v3.1
# ============================================

services:

    moviepilot:
        image: jxxghp/moviepilot-v2:2.11.0
        container_name: moviepilot-v2
        hostname: moviepilot-v2
        network_mode: {network_mode}
        restart: always
        stdin_open: true
        tty: true
"""

        # 非 host 模式添加端口映射
        if network_mode != "host":
            compose += f"""        ports:
            - '{nginx_port}:{nginx_port}'  # Web端口
            - '{port}:{port}'    # API端口
"""

        # 卷映射
        compose += "        volumes:\n"
        compose += "\n".join(volumes) + "\n"

        # 环境变量
        if env_lines:
            compose += "\n        environment:\n"
            compose += "\n".join(env_lines) + "\n"

        # 显示结果
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, compose)
        self.save_btn.config(state=tk.NORMAL)

    def save_compose(self):
        """保存 compose 文件"""
        content = self.result_text.get(1.0, tk.END)
        file_path = filedialog.asksaveasfilename(
            defaultextension=".yml",
            filetypes=[("YAML files", "*.yml"), ("All files", "*.*")],
            initialfile="docker-compose.yml"
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                messagebox.showinfo("保存成功", f"文件已保存到:\n{file_path}")
            except Exception as e:
                messagebox.showerror("保存失败", f"保存文件时出错:\n{str(e)}")


# ═══════════════════════════════════════════════
# 入口
# ═══════════════════════════════════════════════

if __name__ == "__main__":
    root = tk.Tk()
    app = MoviePilotComposer(root)
    root.mainloop()
