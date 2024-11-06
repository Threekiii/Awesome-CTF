# -*- coding: utf-8 -*-
# @Author  : Threekiii
# @Time    : 2022/8/30 15:52
# @Function: 二维码绘制（方法1）

from PIL import Image

MAX = 330
pic = Image.new("RGB",(MAX,MAX))

s= ''
i = 0
for y in range(0,MAX):
    for x in range(0,MAX):
        print(s[i])
        if(s[i]=='1'):
            pic.putpixel([x,y],(0,0,0))
        else:
            pic.putpixel([x,y],(255,255,255))
        i=i+1
pic.show()
pic.save('flag.png')


