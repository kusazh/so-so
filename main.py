from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('MisekiBitmap.ttf', size=16)

image = Image.new('RGB', (320, 288), (219, 248, 199))
draw = ImageDraw.Draw(image)
draw.fontmode= "1"
keywords = []
text = '''　　　　　　　　　　　像恐龙奔跑一样
我已经很久没有[奔跑]　　留下辞世之句
上一次是白垩纪末
历史蚀刻脚印
留下被篡改的意义

我已经很久没有哭
上一次是今天早晨
睡眠可以将情绪消除
同时，理由被分泌

那么生存是什么
我一直都有在呼吸
是引起风暴
还是杀死远方蝴蝶

我已经很久没有死
上一次是在大阪
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
