from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('MisekiBitmap.ttf', size=16)

image = Image.open('wiki.png').resize((320, 288), resample=0)
draw = ImageDraw.Draw(image)
draw.fontmode= "1"
keywords = []
text = '''





[点灯夫群]

在群论中，点灯夫群（英语：Lamplightergroup）是两个群 我/2我 和 我 的圈积
(我/2我) s Z。
'''
i = 0
for line in text.splitlines():
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
        if current > 310:
            i += 1
            current = 16
        text_width = draw.textlength(ch, font)
        draw.text((current, 16 * i), ch, font=font, fill=fill)
        # if i == 6:
        #     current += text_width - 1
        # else:
        current += text_width
    i += 1
image = image.resize((160, 144), resample=0)
image.save(f'so-so/assets/backgrounds/{"-".join(keywords)}-{len(text)}.png')
