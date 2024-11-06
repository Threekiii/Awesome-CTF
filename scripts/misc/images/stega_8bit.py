# -*- coding: utf-8 -*-
# @Author  : Threekiii
# @Time    : 2022/12/8 14:17
# @Function: 位深隐写提取脚本（后8bit隐写）

import png

img = png.Reader('image_48bit.png')
imginfo = img.read()
w, h, imgdata = imginfo[:3]
data = []
for linedata in imgdata:
    line = []
    for d in linedata:
        line.append(d%(2**8))
    data.append(line)
with open('flag.png', 'wb') as f:
    img2 = png.Writer(width=w, height=h, greyscale=False, bitdepth=8)
    img2.write(f, data)
