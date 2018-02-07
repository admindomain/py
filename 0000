from PIL import Image,ImageDraw,ImageFont

im=Image.open('1.jpg')

w,h=im.size
draw=ImageDraw.Draw(im)
font=ImageFont.truetype('SIMYOU.TTF',size=w//8)
draw.text((w-w//8,0),chr(52),fill=(255,0,0),font=font)
im.save('qqtest.jpg')
