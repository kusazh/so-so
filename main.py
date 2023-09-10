from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('MisekiBitmap.ttf', size=16)

image = Image.new('RGB', (320, 288), (219, 248, 199))
draw = ImageDraw.Draw(image)
draw.fontmode= "1"
keywords = []
text = '''
[奥坎剃刀]生锈了
你将它掷入[狄拉克之海]
那[波动方程式]有够[单调]

在[宇宙微波背景]下
我们看向[怪兽的月光]
亦无法从[事件视界][逃逸]

远方传出的微小[红移]
闭上眼感受它的[弦]
是[点灯夫群]正向我们而来
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
