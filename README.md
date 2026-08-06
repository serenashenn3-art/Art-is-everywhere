# Art is everywhere / 行走的艺术

> **EN:** Turn your pet into the protagonist of a timeless masterpiece. This AI Skill fuses uploaded pet photos with 200 world‑famous paintings across five centuries of art history, producing side‑by‑side comparison artworks (original vs. pet fusion) with accurate metadata (title, artist, year, movement).
>
> **中文：** 名画中的萌宠，行走的艺术。将您的爱宠融入跨越五百年的艺术史，让每一只毛孩子都成为传世名作的主角。本 AI Skill 将用户上传的宠物照片与 200 幅世界经典名画无缝融合，生成"原画 vs 成图"左右对比图，并附带准确的名画信息（名称、作者、时间、流派）。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skill Version](https://img.shields.io/badge/version-4.0-blue.svg)](https://github.com/serenashenn3-art/Art-is-everywhere)
[![Paintings](https://img.shields.io/badge/paintings-200-green.svg)](https://github.com/serenashenn3-art/Art-is-everywhere)
[![Platform](https://img.shields.io/badge/platform-Trae%20%7C%20Kimi%20%7C%20Codex%20%7C%20Claude-orange.svg)](https://github.com/serenashenn3-art/Art-is-everywhere)

[English](#english) · [中文](#中文)

---

# English

## 🎨 Overview

**Art is everywhere** (formerly *行走的艺术 / Walking Art*) is an AI Skill that fuses a user‑uploaded pet photo with one of 100 classic paintings, generating a "pet as the protagonist of a masterpiece" artwork. Each output is presented as a **side‑by‑side comparison** (original reference on the left, pet fusion on the right) with an accurate info panel (title, artist, year, movement).

### ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🎲 **Random Mode** | Smart match from the 100‑painting library, weighted by pet type |
| 🎨 **Pick a Painting** | Browse 16 art movements and choose your favorite |
| 📊 **100 Masterpieces** | From Renaissance to contemporary, 16 major styles |
| 🖼️ **Side‑by‑side Output** | Original reference + pet fusion, museum‑catalogue style |
| 📋 **Accurate Metadata** | Title, artist, year, movement — traceable and verifiable |
| 📥 **One‑click Download** | Comparison image + standalone artwork, PNG format |
| 🔧 **Cross‑platform** | Trae / Kimi Work / Codex / Claude / generic agents |

---

## 🖼️ Showcase

### Case 1: *Las Meninas* × Gray Tabby‑and‑White Cat

> 17th‑century Spanish court — the Infanta becomes a feline.

![Las Meninas × Gray Tabby Cat](output/comparison/20260805_las-meninas_comparison.png)

| Field | Info |
|-------|------|
| 🎨 **Painting** | *Las Meninas* |
| 👤 **Artist** | Diego Velázquez |
| 📅 **Year** | 1656 |
| 🎭 **Movement** | Spanish Baroque (Golden Age) |
| 📍 **Location** | Museo Nacional del Prado, Madrid, Spain |
| 📐 **Size** | 318 × 276 cm |
| 🐱 **Fusion** | The gray tabby‑and‑white cat replaces Infanta Margaret Theresa, seated in the court with maids of honor on both sides; Velázquez's self‑portrait on the left (with the red cross of Santiago); the royal couple reflected in the rear mirror |

---

### Case 2: *The Starry Night* × Gray Tabby‑and‑White Cat

> Van Gogh's swirling sky — a kitten on the hillside gazing at the stars.

![The Starry Night × Gray Tabby Cat](output/comparison/20260806_starry-night_comparison.png)

| Field | Info |
|-------|------|
| 🎨 **Painting** | *The Starry Night* (*De sterrennacht*) |
| 👤 **Artist** | Vincent Willem van Gogh (1853–1890) |
| 📅 **Year** | June 1889 |
| 🎭 **Movement** | Post‑Impressionism |
| 📍 **Location** | Museum of Modern Art, New York, USA |
| 📐 **Size** | 73.7 × 92.1 cm |
| 🐱 **Fusion** | A gray tabby‑and‑white cat sits on the foreground hill, gazing up at the swirling sky, replacing the cypress on the left. The tabby stripes are rendered in Van Gogh's impasto brushwork, blending into the rhythm of the swirling sky. The cypress moves to the right; the village and church spire remain in the valley |

---

### Case 3: *Girl with a Pearl Earring* × Gray Tabby‑and‑White Cat

> Dutch Golden Age — the cat becomes the "Mona Lisa of the North."

![Girl with a Pearl Earring × Gray Tabby Cat](output/comparison/20260806_pearl-earring_comparison.png)

| Field | Info |
|-------|------|
| 🎨 **Painting** | *Girl with a Pearl Earring* (*Meisje met de parel*) |
| 👤 **Artist** | Johannes Vermeer (1632–1675) |
| 📅 **Year** | c. 1665 |
| 🎭 **Movement** | Dutch Golden Age (Tronie portrait) |
| 📍 **Location** | Mauritshuis, The Hague, Netherlands |
| 📐 **Size** | 44.5 × 39 cm |
| 🐱 **Fusion** | The gray tabby‑and‑white cat turns in three‑quarter view toward the viewer, replicating the girl's pose. The cat wears a blue‑and‑gold mini turban, with the signature teardrop pearl earring hanging from its left ear. Soft light from the left; the white chest fur gleams like the girl's white collar. Dark background with Vermeer‑style sfumato faithfully restored |

---

### More Styles at a Glance

| Movement | Representative Works | Best Pets |
|----------|---------------------|-----------|
| 🌅 Impressionism | *Water Lilies*, *Impression, Sunrise* | Active cats / dogs |
| 🖼️ Modern Art | *The Persistence of Memory*, *Guernica* | Pets with personality |
| 🎴 Eastern Art | *The Great Wave off Kanagawa*, *Along the River During Qingming* | Birds, rabbits, small pets |
| 🏰 Northern Renaissance | *The Garden of Earthly Delights*, *The Tower of Babel* | Multi‑pet households |
| 🗽 Romanticism | *Liberty Leading the People*, *Wanderer above the Sea of Fog* | Heroic large dogs |
| 💋 Symbolism | *The Kiss* (Klimt), *The Card Players* | Elegant, calm cats |

> 💡 **Upload your pet's photo** — we'll match the best masterpiece for your fur baby!

---

## 🚀 Quick Start

### Option 1: Trae Skill (native)

```bash
# Place the skill folder into Trae's skills directory
cp -r xing-zou-de-yi-shu/ .trae/skills/
```

Upload a pet photo in a Trae conversation — the Skill activates automatically.

### Option 2: System Prompt (Kimi / Claude / Codex)

1. Copy the contents of `SKILL.md` into your system prompt / custom instructions
2. Ensure the `resources/` and `scripts/` folders are on an accessible path
3. Upload a pet photo — the AI follows the Skill instructions

### Option 3: Standalone Comparison Script

```bash
# Clone the repo
git clone https://github.com/serenashenn3-art/Art-is-everywhere.git

# Install dependencies
pip install Pillow

# Compose a side-by-side comparison
python3 scripts/compose_comparison.py \
  original.png \
  pet_fusion.png \
  comparison_output.png \
  '{"title_zh":"Las Meninas","title_original":"Las Meninas","author_cn":"Velazquez","author":"Velazquez","year":"1656","style":"Spanish Baroque","style_tag":"Baroque"}'
```

---

## 📋 Workflow

```
User uploads pet photo
      │
      ▼
  Identify pet info (type / breed / color)
      │
      ▼
┌──────────────────────────┐
│  🎲 Random   🎨 Pick    │
└──────┬───────────────┬───┘
       ▼               ▼
  Random painting   Browse 16 styles
       │               │
       ▼               ▼
  Generate original reference + pet fusion
       │
       ▼
  Compose side-by-side comparison (with info panel)
       │
       ▼
  Show comparison + metadata + download link
```

---

## 📁 Project Structure

```
xing-zou-de-yi-shu/
├── SKILL.md                              # Skill main instruction file (core)
├── README.md                             # This file (bilingual EN/ZH)
├── LICENSE                               # MIT License
├── .gitignore
├── resources/
│   ├── paintings-database-v3.md          # 200-painting database (16 styles)
│   ├── paintings-database.md             # Legacy database (22 paintings)
│   └── prompt-templates.md               # Prompt templates
├── scripts/
│   └── compose_comparison.py             # Side-by-side comparison script
├── examples/
│   ├── input-example.md                  # Input example
│   └── output-example.md                 # Output example
└── output/                               # Generated results (gitignored)
    ├── reference/                        # Original reference images
    ├── generated-art/                    # Pet fusion artworks
    └── comparison/                       # Comparison composites
```

---

## 🎴 100 Masterpieces · 16 Movements

| # | Movement | Count | Representative Works |
|---|----------|-------|---------------------|
| 1 | 🎨 Renaissance | 10 | *Mona Lisa*, *Creation of Adam*, *Primavera* |
| 2 | 🏛️ Baroque | 8 | *Las Meninas*, *The Night Watch*, *Girl with a Pearl Earring* |
| 3 | 🧡 Dutch Golden Age | 6 | *The Milkmaid*, *The Little Street* |
| 4 | 🌅 Impressionism | 8 | *The Starry Night*, *Water Lilies*, *Impression, Sunrise* |
| 5 | 🌀 Post‑Impressionism | 4 | *The Scream*, *Moulin Rouge* |
| 6 | 🖼️ Modern Art | 8 | *The Two Fridas*, *Guernica*, *The Dream* |
| 7 | 🎴 Eastern Art | 6 | *The Great Wave off Kanagawa*, *Along the River During Qingming* |
| 8 | 🏰 Northern Renaissance | 5 | *The Last Supper*, *The Garden of Earthly Delights*, *The Tower of Babel* |
| 9 | 🗽 Romanticism & Neoclassicism | 8 | *Liberty Leading the People*, *Death of Marat* |
| 10 | 🌾 Realism | 4 | *The Gleaners*, *A Burial at Ornans* |
| 11 | 💋 Symbolism & Secession | 5 | *The Kiss* (Klimt), *The Card Players* |
| 12 | 🔮 Surrealism (extended) | 4 | *The Son of Man*, *Soft Construction with Boiled Beans* |
| 13 | 🔶 Abstract & Contemporary | 6 | *Composition VIII*, *Balloon Dog* |
| 14 | 🏮 Chinese Art (extended) | 6 | *Travelers among Mountains and Streams*, *A Thousand Li of Rivers and Mountains* |
| 15 | ⛩️ Japanese Art (extended) | 4 | *Plum Estate, Kameido*, *Sudden Shower over Shin-Ōhashi* |
| 16 | 🎭 More Classics | 8 | *The Last Judgment*, *Sistine Madonna* |

---

## 🐾 Pet Matching Guide

| Pet Type | Top 5 Matches |
|----------|---------------|
| 🐱 Cat | #11 Las Meninas · #37 The Two Fridas · #20 El Greco · #19 Chubby Boy · #13 Girl with a Pearl Earring |
| 🐕 Dog | #12 The Night Watch · #29 A Sunday on La Grande Jatte · #25 The Starry Night · #27 Water Lilies · #33 The Scream |
| 🐇 Rabbit / Small Pet | #3 Primavera · #26 Sunflowers · #27 Water Lilies · #13 Girl with a Pearl Earring · #1 Mona Lisa |
| 🦜 Bird | #25 The Starry Night · #47 The Great Wave · #46 Dwelling in the Fuchun Mountains · #48 Fine Wind, Clear Morning · #3 Primavera |

---

## 🔧 Technical Details

### Comparison Composition Script

`scripts/compose_comparison.py` uses Python Pillow to compose the side‑by‑side image:

- **Canvas size**: 2400 × 1900 px
- **Left**: original reference (label "ORIGINAL MASTERPIECE")
- **Right**: pet fusion (label "PET FUSION ARTWORK")
- **Bottom**: painting info bar (title, style, year, artist)
- **Font**: auto‑detects CJK fonts (Noto Sans CJK / WQY / DejaVu fallback)

### Dependencies

- Python 3.8+
- Pillow (PIL)
- CJK font (optional, Noto Sans CJK recommended)

---

## 🌐 Cross‑platform Compatibility

| Platform | Status | Deployment |
|----------|--------|------------|
| **Trae** | ✅ Fully compatible | Drop into `.trae/skills/` |
| **Kimi Work** | ✅ Compatible | SKILL.md as system prompt |
| **Codex (OpenAI)** | ✅ Compatible | SKILL.md as custom instructions |
| **Claude** | ✅ Compatible | SKILL.md as system prompt |
| **Generic AI Agent** | ✅ Compatible | Standard Markdown instruction format |

---

## 📝 License

[MIT License](LICENSE) — free to use, modify, and distribute.

---

## 🙏 Acknowledgements

- The 100‑painting database is compiled from public‑domain art‑history sources.
- All painting metadata (artist, year, location) comes from official museum open data.
- Generated artworks are for entertainment and personal use only and do not represent the originals.

---

# 中文

## 🎨 项目简介

**行走的艺术**（英文名 *Art is everywhere*）是一个 AI Skill，将用户上传的宠物照片与 200 幅世界经典名画无缝融合，生成"宠物成为名画主角"的艺术作品。每幅作品都以**左右对比图**形式呈现（原画参考 vs 成图），并附带准确的名画信息（名称、作者、时间、流派）。

### ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🎲 **随机生成** | 系统从200幅名画库中智能匹配随机选取 |
| 🎨 **选择名画** | 按16种风格分类浏览，自选心仪名画 |
| 📊 **200幅名画库** | 覆盖文艺复兴到当代，16大艺术风格 |
| 🖼️ **左右对比输出** | 原画参考 + 宠物融合，博物馆画册风格 |
| 📋 **准确信息标签** | 名称、作者、时间、流派，可追溯可复核 |
| 📥 **一键下载** | 对比图 + 单独成图，PNG格式 |
| 🔧 **跨平台兼容** | Trae / Kimi Work / Codex / Claude / 通用 Agent |

---

## 🖼️ 效果展示

### 🎯 案例一：《宫娥》× 灰虎斑加白猫

> 17 世纪西班牙宫廷 · 小公主变身喵星人

![《宫娥》× 灰虎斑猫](output/comparison/20260805_las-meninas_comparison.png)

| 字段 | 信息 |
|------|------|
| 🎨 **画作** | 《宫娥》 *Las Meninas* |
| 👤 **作者** | 迭戈·罗德里格斯·德·席尔瓦·委拉斯开兹（Diego Velázquez） |
| 📅 **创作时间** | 1656 年 |
| 🎭 **流派** | 西班牙巴洛克绘画（黄金时代） |
| 📍 **现藏地点** | 西班牙马德里 · 普拉多国家博物馆 |
| 📐 **原作尺寸** | 318 × 276 cm |
| 🐱 **融合说明** | 灰虎斑加白猫替换小公主玛格丽特·特蕾莎，端坐宫廷，两侧宫女服侍，左侧为委拉斯开兹自画像（胸口红十字勋章），后墙镜中反射王室夫妇 |

---

### 🎯 案例二：《星月夜》× 灰虎斑加白猫

> 梵高的旋涡星空 · 猫咪坐在山坡仰望星河

![《星月夜》× 灰虎斑猫](output/comparison/20260806_starry-night_comparison.png)

| 字段 | 信息 |
|------|------|
| 🎨 **画作** | 《星月夜》 *The Starry Night* (*De sterrennacht*) |
| 👤 **作者** | 文森特·威廉·梵高（Vincent Willem van Gogh, 1853-1890） |
| 📅 **创作时间** | 1889 年 6 月 |
| 🎭 **流派** | 后印象派 |
| 📍 **现藏地点** | 美国纽约 · 现代艺术博物馆 |
| 📐 **原作尺寸** | 73.7 × 92.1 cm |
| 🐱 **融合说明** | 灰虎斑加白猫坐在前景山坡上，仰头凝望旋涡星空，取代了原画左侧的柏树位置。猫毛的虎斑条纹以梵高式厚涂笔触绘制，与旋涡天空的节奏融为一体。柏树移至右侧，村庄与教堂尖塔保留在山谷中 |

---

### 🎯 案例三：《戴珍珠耳环的少女》× 灰虎斑加白猫

> 荷兰黄金时代 · 猫咪化身"北方蒙娜丽莎"

![《戴珍珠耳环的少女》× 灰虎斑猫](output/comparison/20260806_pearl-earring_comparison.png)

| 字段 | 信息 |
|------|------|
| 🎨 **画作** | 《戴珍珠耳环的少女》 *Girl with a Pearl Earring* (*Meisje met de parel*) |
| 👤 **作者** | 约翰内斯·维米尔（Johannes Vermeer, 1632-1675） |
| 📅 **创作时间** | 约 1665 年 |
| 🎭 **流派** | 荷兰黄金时代（Tronie 风格肖像） |
| 📍 **现藏地点** | 荷兰海牙 · 莫瑞泰斯皇家美术馆 |
| 📐 **原作尺寸** | 44.5 × 39 cm |
| 🐱 **融合说明** | 灰虎斑加白猫以四分之三侧面回头凝视观众，完美复刻原画少女的姿态。猫咪头戴蓝金色迷你头巾，左耳处悬挂标志性的水滴形珍珠耳环。柔和光线从左侧照射，白色胸毛如少女的白色衣领般明亮。深色背景与维米尔式晕涂法完美还原 |

---

### 🎴 更多名画风格预览（按流派）

| 风格 | 代表作品 | 适合宠物 |
|------|---------|---------|
| 🌅 **印象派** | 《睡莲》《日出·印象》《蒙马特街道》 | 活跃外向的猫/狗 |
| 🖼️ **现代艺术** | 《记忆的永恒》《格尔尼卡》《梦》 | 有个性的奇异宠物 |
| 🎴 **东方艺术** | 《千里江山图》《神奈川冲浪里》 | 鸟类、兔子、小型宠物 |
| 🏰 **北方文艺复兴** | 《人间乐园》《巴别塔》 | 群宠、多宠物合璧 |
| 🗽 **浪漫主义** | 《自由引导人民》《雾海上的漫游者》 | 英勇气质的大型犬 |
| 💋 **象征主义** | 《吻》（克里姆特）《玩牌者》 | 优雅沉静的猫 |

> 💡 **欢迎上传您的宠物照片**，我们会根据毛孩子的气质为您匹配最适合的名画！

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
git clone https://github.com/serenashenn3-art/Art-is-everywhere.git

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
├── README.md                             # 项目说明（本文件，中英双语）
├── LICENSE                               # MIT 许可证
├── .gitignore
├── resources/
│   ├── paintings-database-v3.md          # 200幅名画数据库（16大风格）
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

## 🎴 200幅名画库 · 16大风格

| 编号 | 风格 | 数量 | 编号范围 | 代表作品 |
|------|------|------|---------|---------|
| 1 | 🎨 文艺复兴 | 20 | #1-20 | 蒙娜丽莎、创造亚当、春、最后的审判、西斯廷圣母 |
| 2 | 🏛️ 巴洛克 | 16 | #21-36 | 宫娥、夜巡、戴珍珠耳环、圣马太蒙召、基督下葬 |
| 3 | 🧡 荷兰黄金时代 | 12 | #37-48 | 倒牛奶的女仆、小街、下十字架(维登版) |
| 4 | 🌅 印象派 | 16 | #49-64 | 星月夜、睡莲、日出·印象、吻(克里姆特)、玩牌者 |
| 5 | 🌀 后印象派 | 10 | #65-74 | 呐喊、红磨坊、拥抱(席勒)、女人三阶段 |
| 6 | 🖼️ 现代艺术 | 14 | #75-88 | 两个弗里达、格尔尼卡、人类之子、哈里昆的嘉年华 |
| 7 | 🎴 东方艺术 | 12 | #89-100 | 神奈川冲浪里、清明上河图、墨竹图 |
| 8 | 🏰 北方文艺复兴 | 11 | #101-111 | 最后的晚餐、雅典学院、人间乐园、四使徒 |
| 9 | 🗽 浪漫主义与新古典 | 16 | #112-127 | 自由引导人民、马拉之死、土耳其浴女、奴隶船 |
| 10 | 🌾 现实主义 | 9 | #128-136 | 拾穗者、奥南的葬礼、晚钟、画室、草地上的午餐 |
| 11 | 💋 象征主义与分离派 | 10 | #137-146 | 独角兽、死之岛、独眼巨人、拥抱 |
| 12 | 🔮 超现实主义扩展 | 9 | #147-155 | 西里伯斯大象、戈尔孔达、天鹅倒影大象 |
| 13 | 🔶 抽象与当代 | 10 | #156-165 | 秋之韵律(波洛克)、十字架之站、溺水的女孩、无题骷髅 |
| 14 | 🏮 中国艺术扩展 | 12 | #166-177 | 溪山行旅图、千里江山图、奔马图、竹石图 |
| 15 | ⛩️ 日本艺术扩展 | 9 | #178-186 | 龟户梅屋铺、妇人相学十体、相马旧王城、回首的美人 |
| 16 | 🎭 更多经典补充 | 14 | #187-200 | 哀悼基督(乔托版)、圣三位一体、众神之宴 |

---

## 🐾 宠物适配推荐

| 宠物类型 | TOP 8 推荐 |
|---------|-----------|
| 🐱 猫咪 | #21宫娥 · #75两个弗里达 · #38埃尔格列柯 · #37胖男孩 · #23戴珍珠耳环 · #147人类之子 · #1蒙娜丽莎 · #145拥抱 |
| 🐕 狗狗 | #22夜巡 · #53大碗岛 · #49星月夜 · #51睡莲 · #65呐喊 · #119干草车 · #118雾海漫游者 · #105阿尔诺芬尼 |
| 🐇 兔/小宠 | #3春 · #50向日葵 · #51睡莲 · #23戴珍珠耳环 · #1蒙娜丽莎 · #103人间乐园 · #169千里江山图 · #170五牛图 |
| 🦜 鸟类 | #49星月夜 · #91神奈川冲浪 · #90富春山居 · #92凯风快晴 · #3春 · #142独角兽 · #93大桥骤雨 · #178龟户梅屋铺 |

---

## 🔧 技术细节

### 对比图合成脚本

`scripts/compose_comparison.py` 使用 Python Pillow 库合成左右对比图：

- **画布尺寸**：2400 × 1900 px
- **左侧**：原画参考图（标签「原 作 名 画」/ "ORIGINAL MASTERPIECE"）
- **右侧**：宠物融合图（标签「萌 宠 合 成」/ "PET FUSION ARTWORK"）
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

- 200幅名画数据基于公共领域艺术史资料整理
- 所有名画信息（作者、时间、藏地）均来自博物馆官方公开数据
- 生成的艺术作品仅供娱乐和个人使用，不代表原作

---

> 🐾 **Art is everywhere / 行走的艺术** · Every fur baby is a born artist · 每只毛孩子都是天生的艺术家 · v3.0
