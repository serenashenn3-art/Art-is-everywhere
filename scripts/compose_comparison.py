#!/usr/bin/env python3
"""
行走的艺术 · 名画对比合成器
用法: python3 compose_comparison.py <原图路径> <成图路径> <输出路径> <名画配置JSON>

名画配置JSON格式:
{
  "title_zh": "宫娥",
  "title_original": "Las Meninas",
  "author": "Diego Velázquez",
  "author_cn": "迭戈·委拉斯开兹",
  "year": "1656年",
  "style": "西班牙巴洛克",
  "style_tag": "巴洛克"
}
"""

import sys
import json
from PIL import Image, ImageDraw, ImageFont
import os

HAS_CHINESE_FONT = False

def find_font():
    global HAS_CHINESE_FONT
    candidates = [
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.otf",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.otf",
        "/usr/share/fonts/truetype/arphic/uming.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            if 'cjk' in path.lower() or 'wqy' in path.lower() or 'uming' in path.lower():
                HAS_CHINESE_FONT = True
            return path
    return None

def find_font_bold():
    candidates = [
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.otf",
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.otf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return find_font()

def draw_centered_text(draw, text, y, font, fill, width, x_start=0):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = x_start + (width - text_width) // 2
    draw.text((x, y), text, font=font, fill=fill)

def draw_multiline_text_centered(draw, text_lines, y_start, font, fill, line_height, x_start, block_width):
    for i, line in enumerate(text_lines):
        draw_centered_text(draw, line, y_start + i * line_height, font, fill, block_width, x_start)

def create_comparison(original_path, generated_path, output_path, painting_info):
    """
    创建左右对比图
    左: 原画参考 | 右: 宠物融合成品
    底部: 名画信息标签
    """
    font_path = find_font()
    bold_font_path = find_font_bold()

    # ---------- 画布尺寸 ----------
    canvas_width = 2400
    canvas_height = 1900
    padding = 60
    gap = 50

    # 计算图片区域
    image_area_width = (canvas_width - padding * 2 - gap) // 2
    image_area_height = 1400

    # ---------- 创建画布 ----------
    canvas = Image.new('RGB', (canvas_width, canvas_height), '#FAFAF8')
    draw = ImageDraw.Draw(canvas)

    # ---------- 顶部标题 ----------
    title_font_size = 56
    subtitle_font_size = 28
    label_font_size = 32
    info_title_font_size = 36
    info_content_font_size = 28
    info_small_font_size = 24

    if font_path:
        title_font = ImageFont.truetype(bold_font_path or font_path, title_font_size)
        subtitle_font = ImageFont.truetype(bold_font_path or font_path, subtitle_font_size)
        label_font = ImageFont.truetype(bold_font_path or font_path, label_font_size)
        info_title_font = ImageFont.truetype(bold_font_path or font_path, info_title_font_size)
        info_content_font = ImageFont.truetype(font_path, info_content_font_size)
        info_small_font = ImageFont.truetype(font_path, info_small_font_size)
    else:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        info_title_font = ImageFont.load_default()
        info_content_font = ImageFont.load_default()
        info_small_font = ImageFont.load_default()

    # ---------- 文本变量（根据字体可用性）----------
    if HAS_CHINESE_FONT:
        left_label_text = "原 作 名 画"
        right_label_text = "萌 宠 合 成"
        title_text = "行 走 的 艺 术"
        info_title = f"《{painting_info.get('title_zh', '')}》  ·  {painting_info.get('title_original', '')}"
        style_label = f"风格: {painting_info.get('style', '')}  |  创作时间: {painting_info.get('year', '')}  |  作者: {painting_info.get('author_cn', painting_info.get('author', ''))}"
        credit = "行走的艺术 · Masterpiece Pet Gallery · Powered by AI"
    else:
        left_label_text = "ORIGINAL MASTERPIECE"
        right_label_text = "PET FUSION ARTWORK"
        title_text = "Masterpiece Pet Gallery · Walking Art"
        info_title = f'"{painting_info.get("title_original", "")}"  ·  {painting_info.get("title_zh", "")}'
        style_label = f"Style: {painting_info.get('style', '')}  |  Year: {painting_info.get('year', '')}  |  Artist: {painting_info.get('author', '')}"
        credit = "Masterpiece Pet Gallery · Powered by AI"

    # 标题
    y_title = 30
    draw_centered_text(draw, title_text, y_title, title_font, '#1a1a1a', canvas_width)

    # 分隔线
    y_line1 = y_title + title_font_size + 20
    draw.line([(padding, y_line1), (canvas_width - padding, y_line1)], fill='#d0d0d0', width=2)

    # ---------- 加载并放置图片 ----------
    try:
        original_img = Image.open(original_path).convert('RGB')
    except Exception as e:
        print(f"ERROR loading original: {e}")
        original_img = Image.new('RGB', (800, 1000), '#888888')
        draw_err = ImageDraw.Draw(original_img)
        draw_err.text((100, 450), "[原图加载失败]", fill='white')

    try:
        generated_img = Image.open(generated_path).convert('RGB')
    except Exception as e:
        print(f"ERROR loading generated: {e}")
        generated_img = Image.new('RGB', (800, 1000), '#888888')
        draw_err = ImageDraw.Draw(generated_img)
        draw_err.text((100, 450), "[成图加载失败]", fill='white')

    # 统一尺寸并保持比例
    def fit_image(img, target_width, target_height):
        w, h = img.size
        ratio = min(target_width / w, target_height / h)
        new_w = int(w * ratio)
        new_h = int(h * ratio)
        return img.resize((new_w, new_h), Image.LANCZOS)

    # 左图 - 原画
    left_img = fit_image(original_img, image_area_width, image_area_height)
    left_x = padding + (image_area_width - left_img.size[0]) // 2
    left_y = y_line1 + 40
    canvas.paste(left_img, (left_x, left_y))

    # 右图 - 成图
    right_img = fit_image(generated_img, image_area_width, image_area_height)
    right_x = padding + image_area_width + gap + (image_area_width - right_img.size[0]) // 2
    right_y = y_line1 + 40
    canvas.paste(right_img, (right_x, right_y))

    # 图片边框
    border_color = '#2c2c2c'
    border_width = 3
    # 左边框
    draw.rectangle([left_x - border_width, left_y - border_width,
                    left_x + left_img.size[0] + border_width, left_y + left_img.size[1] + border_width],
                   outline=border_color, width=border_width)
    # 右边框
    draw.rectangle([right_x - border_width, right_y - border_width,
                    right_x + right_img.size[0] + border_width, right_y + right_img.size[1] + border_width],
                   outline=border_color, width=border_width)

    # ---------- 图片下方标签 ----------
    label_y = max(left_y + left_img.size[1], right_y + right_img.size[1]) + 20

    # 左标签
    draw_centered_text(draw, left_label_text, label_y, label_font, '#555555', image_area_width, padding)

    # 右标签
    draw_centered_text(draw, right_label_text, label_y, label_font, '#2c5f8d', image_area_width, padding + image_area_width + gap)

    # ---------- 底部信息区 ----------
    info_y = label_y + label_font_size + 40

    # 信息区背景
    info_height = 260
    info_rect = [padding - 10, info_y - 15, canvas_width - padding + 10, info_y + info_height]
    draw.rectangle(info_rect, fill='#FFFFFF', outline='#e0e0e0', width=2)

    # 信息 - 标题行
    draw_centered_text(draw, info_title, info_y + 10, info_title_font, '#1a1a1a', canvas_width)

    # 信息 - 标签
    draw_centered_text(draw, style_label, info_y + 65, info_content_font, '#555555', canvas_width)

    # 信息 - 分割线
    info_y_line = info_y + 110
    draw.line([(padding, info_y_line), (canvas_width - padding, info_y_line)], fill='#e8e8e8', width=1)

    # 信息 - 署名行
    draw_centered_text(draw, credit, info_y + 130, info_small_font, '#999999', canvas_width)

    # ---------- 保存 ----------
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    canvas.save(output_path, 'PNG', quality=100)
    print(f"✅ 对比图已保存: {output_path}")
    print(f"   尺寸: {canvas_width}×{canvas_height}")
    return output_path


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print(__doc__)
        sys.exit(1)

    original_path = sys.argv[1]
    generated_path = sys.argv[2]
    output_path = sys.argv[3]
    painting_info = json.loads(sys.argv[4])

    create_comparison(original_path, generated_path, output_path, painting_info)
