from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('MisekiBitmap.ttf', size=16)

image = Image.new('RGB', (320, 288), (219, 248, 199))
draw = ImageDraw.Draw(image)
draw.fontmode= "1"
keywords = []
text = '''
翘角的城市
解构折纸的方式
你寄居帝王之座
以冠冕乞讨

旧时代的尘嚣
革命的预兆
[话语]并列之间
篡改一道圣旨

门上的封纸
粘住紧张的街道
你以微服私访
寻找一味新药
'''
for i, line in enumerate(text.splitlines()):
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
