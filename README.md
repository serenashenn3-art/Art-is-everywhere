# 行走的艺术

> **名画中的萌宠，行走的艺术。** 将您的爱宠融入跨越五百年的艺术史，让每一只毛孩子都成为传世名作的主角。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skill Version](https://img.shields.io/badge/version-3.0-blue.svg)](https://github.com/walking-art-team/xing-zou-de-yi-shu)
[![Paintings](https://img.shields.io/badge/paintings-100-green.svg)](https://github.com/walking-art-team/xing-zou-de-yi-shu)
[![Platform](https://img.shields.io/badge/platform-Trae%20%7C%20Kimi%20%7C%20Codex%20%7C%20Claude-orange.svg)](https://github.com/walking-art-team/xing-zou-de-yi-shu)

---

## 🎨 项目简介

**行走的艺术** 是一个 AI Skill，将用户上传的宠物照片与 100 幅世界经典名画进行无缝融合，生成"宠物成为名画主角"的艺术作品。每幅作品都以左右对比图形式呈现（原画 vs 成图），并附带准确的名画信息（名称、作者、时间、流派）。

### ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🎲 **随机生成** | 系统从100幅名画库中智能匹配随机选取 |
| 🎨 **选择名画** | 按16种风格分类浏览，自选心仪名画 |
| 📊 **100幅名画库** | 覆盖文艺复兴到当代，16大艺术风格 |
| 🖼️ **左右对比输出** | 原画参考 + 宠物融合，博物馆画册风格 |
| 📋 **准确信息标签** | 名称、作者、时间、流派，可追溯可复核 |
| 📥 **一键下载** | 对比图 + 单独成图，PNG格式 |
| 🔧 **跨平台兼容** | Trae / Kimi Work / Codex / Claude / 通用 Agent |

---

## 🖼️ 效果展示

### 作品一：《宫娥》× 灰虎斑猫

![《宫娥》× 灰虎斑猫](output/comparison/20260805_las-meninas_comparison.png)

| 项目 | 内容 |
|------|------|
| 画作 | 《宫娥》*Las Meninas* |
| 作者 | 迭戈·委拉斯开兹（1656） |
| 流派 | 西班牙巴洛克 |
| 藏地 | 马德里·普拉多博物馆 |

### 作品二：《两个弗里达》× 灰虎斑猫

![《两个弗里达》× 灰虎斑猫](output/comparison/20260805_two-fridas_comparison.png)

| 项目 | 内容 |
|------|------|
| 画作 | 《两个弗里达》*Las Dos Fridas* |
| 作者 | 弗里达·卡罗（1939） |
| 流派 | 墨西哥超现实主义 |
| 藏地 | 墨西哥城·现代艺术博物馆 |

---

## 🚀 快速开始

### 方式一：Trae Skill（原生）

```bash
# 将 skill 文件夹放入 Trae 的 skills 目录
cp -r xing-zou-de-yi-shu/ .trae/skills/
```

在 Trae 对话中上传宠物照片，Skill 自动激活。

### 方式二：系统提示词（Kimi / Claude / Codex）

1. 将 `SKILL.md` 内容复制到系统提示词 / Custom Instructions
2. 确保 `resources/` 和 `scripts/` 目录在可访问路径
3. 上传宠物照片，AI 按 Skill 指令执行

### 方式三：独立运行对比图合成

```bash
# 克隆仓库
git clone https://github.com/walking-art-team/xing-zou-de-yi-shu.git

# 安装依赖
pip install Pillow

# 合成对比图
python3 scripts/compose_comparison.py \
  original.png \
  pet_fusion.png \
  comparison_output.png \
  '{"title_zh":"宫娥","title_original":"Las Meninas","author_cn":"委拉斯开兹","author":"Velazquez","year":"1656年","style":"西班牙巴洛克","style_tag":"巴洛克"}'
```

---

## 📋 使用流程

```
用户上传宠物照片
      │
      ▼
  识别宠物信息（类型/品种/毛色）
      │
      ▼
┌──────────────────────────┐
│  🎲 随机生成  │  🎨 选择名画  │
└──────┬───────────────┬───┘
       │               │
       ▼               ▼
  随机选取名画     浏览16种风格
       │           选择具体画作
       │               │
       ▼               ▼
  生成原画参考 + 宠物融合图
       │
       ▼
  合成左右对比图（含信息标签）
       │
       ▼
  展示对比图 + 作品信息 + 下载链接
```

---

## 📁 项目结构

```
xing-zou-de-yi-shu/
├── SKILL.md                              # Skill 主指令文件（核心）
├── README.md                             # 项目说明（本文件）
├── LICENSE                               # MIT 许可证
├── .gitignore
├── resources/
│   ├── paintings-database-v2.md          # 100幅名画数据库（16大风格）
│   ├── paintings-database.md             # 旧版名画数据库（22幅）
│   └── prompt-templates.md               # 提示词模板（6幅专用+通用）
├── scripts/
│   └── compose_comparison.py             # 左右对比图合成脚本
├── examples/
│   ├── input-example.md                  # 输入示例
│   └── output-example.md                 # 输出示例
└── output/                               # 生成结果（gitignore）
    ├── reference/                        # 原画参考图
    ├── generated-art/                    # 宠物融合成图
    └── comparison/                       # 对比合成图
```

---

## 🎴 100幅名画库 · 16大风格

| 编号 | 风格 | 数量 | 代表作品 |
|------|------|------|---------|
| 1 | 🎨 文艺复兴 | 10 | 蒙娜丽莎、创造亚当、春 |
| 2 | 🏛️ 巴洛克 | 8 | 宫娥、夜巡、戴珍珠耳环的少女 |
| 3 | 🧡 荷兰黄金时代 | 6 | 倒牛奶的女仆、小街 |
| 4 | 🌅 印象派 | 8 | 星月夜、睡莲、日出·印象 |
| 5 | 🌀 后印象派 | 4 | 呐喊、红磨坊 |
| 6 | 🖼️ 现代艺术 | 8 | 两个弗里达、格尔尼卡、梦 |
| 7 | 🎴 东方艺术 | 6 | 神奈川冲浪里、清明上河图 |
| 8 | 🏰 北方文艺复兴 | 5 | 最后的晚餐、人间乐园、巴别塔 |
| 9 | 🗽 浪漫主义与新古典 | 8 | 自由引导人民、马拉之死 |
| 10 | 🌾 现实主义 | 4 | 拾穗者、奥南的葬礼 |
| 11 | 💋 象征主义与分离派 | 5 | 吻（克里姆特）、玩牌者 |
| 12 | 🔮 超现实主义扩展 | 4 | 人类之子、内战的预兆 |
| 13 | 🔶 抽象与当代 | 6 | 构图VIII、气球狗 |
| 14 | 🏮 中国艺术扩展 | 6 | 溪山行旅图、千里江山图 |
| 15 | ⛩️ 日本艺术扩展 | 4 | 龟户梅屋铺、山下白雨 |
| 16 | 🎭 更多经典补充 | 8 | 最后的审判、西斯廷圣母 |

---

## 🐾 宠物适配推荐

| 宠物类型 | TOP 5 推荐 |
|---------|-----------|
| 🐱 猫咪 | #11宫娥 · #37两个弗里达 · #20格列柯 · #19胖男孩 · #13戴珍珠耳环 |
| 🐕 狗狗 | #12夜巡 · #29大碗岛 · #25星月夜 · #27睡莲 · #33呐喊 |
| 🐇 兔/小宠 | #3春 · #26向日葵 · #27睡莲 · #13戴珍珠耳环 · #1蒙娜丽莎 |
| 🦜 鸟类 | #25星月夜 · #47神奈川冲浪 · #46富春山居 · #48凯风快晴 · #3春 |

---

## 🔧 技术细节

### 对比图合成脚本

`scripts/compose_comparison.py` 使用 Python Pillow 库合成左右对比图：

- **画布尺寸**：2400 × 1900 px
- **左侧**：原画参考图（标签「原 作 名 画」）
- **右侧**：宠物融合图（标签「萌 宠 合 成」）
- **底部**：名画信息栏（名称、风格、时间、作者）
- **字体**：自动检测中文字体（Noto Sans CJK / WQY / DejaVu 回退）

### 依赖

- Python 3.8+
- Pillow (PIL)
- 中文字体（可选，推荐 Noto Sans CJK）

---

## 🌐 跨平台兼容

| 平台 | 状态 | 部署方式 |
|------|------|---------|
| **Trae** | ✅ 完全兼容 | 放入 `.trae/skills/` 目录 |
| **Kimi Work** | ✅ 兼容 | SKILL.md 作为系统提示词 |
| **Codex (OpenAI)** | ✅ 兼容 | SKILL.md 作为 custom instructions |
| **Claude** | ✅ 兼容 | SKILL.md 作为 system prompt |
| **通用 AI Agent** | ✅ 兼容 | 标准 Markdown 指令格式 |

---

## 📝 License

[MIT License](LICENSE) - 可自由使用、修改、分发。

---

## 🙏 致谢

- 100幅名画数据基于公共领域艺术史资料整理
- 所有名画信息（作者、时间、藏地）均来自博物馆官方公开数据
- 生成的艺术作品仅供娱乐和个人使用，不代表原作

---

> 🐾 **行走的艺术** · 每只毛孩子都是天生的艺术家 · v3.0
