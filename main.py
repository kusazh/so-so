from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('MisekiBitmap.ttf', size=16)

image = Image.new('RGB', (320, 288), (219, 248, 199))
draw = ImageDraw.Draw(image)
draw.fontmode= "1"
keywords = []
text = '''
讲师挥舞概念大旗
试图指导生活
演员搬弄概念游戏
试图模糊生活定义

概念吃掉概念
戏剧继续上演
叛乱者引爆对立
对立打破第一面墙壁

警察肃清街道
学者沉默不语
诗人乞讨卖艺
难民偷窃我的硬币


'''
for i, line in enumerate(text.splitlines()):
    current = 16
    fill = (7, 24, 33)
    is_keyword, keyword = False, ''
    for ch in line:
        if ch == '[':
            fill = (48, 104, 80)
            is_keyword = True
            continue
        elif ch == ']':
            fill = (7, 24, 33)
            is_keyword = False
            keywords.append(keyword)
            keyword = ''
            continue
        if is_keyword:
            keyword += ch
        text_width = draw.textlength(ch, font)
        draw.text((current, 16 * i), ch, font=font, fill=fill)
        # if i == 6:
        #     current += text_width - 1
        # else:
        current += text_width
image = image.resize((160, 144), resample=0)
image.save(f'so-so/assets/backgrounds/{"-".join(keywords)}-{len(text)}.png')
