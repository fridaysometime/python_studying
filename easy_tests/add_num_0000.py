
#第 0000 题：**将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
# 类似于图中效果
from PIL import Image,ImageFont,ImageDraw

def add_num(img):
    im=Image.open(img)
    w,h=im.size
    font=ImageFont.truetype("C:\Windows\Fonts\Calibri.ttf",30)
    fillcolor="#ff0000"
    draw=ImageDraw.Draw(im)
    draw.text((w-34,0),'10',font=font,fill=fillcolor)
    im.save('2.jpg','jpeg')

if __name__=='__main__':
    add_num('1.jpg')
