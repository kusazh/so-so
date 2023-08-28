from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('MisekiBitmap.ttf', size=16)

image = Image.new('RGB', (320, 288), (219, 248, 199))
draw = ImageDraw.Draw(image)
draw.fontmode= "1"
keywords = []
for i, line in enumerate('''
将眼睛眯起来
就能变得敏锐
我知道这是科学
我知道这是寓言

话已经被说满了
只好缩减
我知道这是诗歌
我知道这是方笺

我们都被困在孤岛上
所以才造[船]
我知道这是人类
我知道还有其他人
'''.splitlines()):
    current = 14
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
            continue
        if is_keyword:
            keyword += ch
        text_width = draw.textlength(ch, font)
        draw.text((current, 14 * i), ch, font=font, fill=fill)
        current += text_width - 2
image = image.resize((160, 144), resample=0)
image.save(f'asserts/{"-".join(keywords)}.png')
