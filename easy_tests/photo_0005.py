from PIL import Image
import os

path='pics'
new_path='new_pics'
if not os.path.isdir(new_path):
    os.mkdir(new_path)
for i in os.listdir(path):
    i_path=os.path.join(path,i)
    im=Image.open(i_path)
    w,h=im.size
    print(w)
    print(h)
    if((1336/w) >= (640/h)):
        n=1336/w
    else:
        n=640/h
    im.thumbnail(w/n,h/n)
    im.save(new_path+i.split('.')[0]+'.jpg','jpeg')
