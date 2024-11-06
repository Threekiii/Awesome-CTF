# -*- coding: utf-8 -*-
# @Author  : Threekiii
# @Time    : 2022/8/30 15:54
# @Function: 二维码绘制（方法2）

import cv2
# import cv2 as cv
import numpy as np

f = open("qrcode.txt",encoding = "utf-8")

blank_image = np.zeros((330,330,3), np.uint8)

a = f.read()

aa = 0

for i in a:
    x = aa//330
    y = aa%330
    if i == '0':
        blank_image[x, y, 1] = 0
    else:
        blank_image[x, y, 0] = 255
        blank_image[x, y, 1] = 255
        blank_image[x, y, 2] = 255
    aa += 1

cv2.imwrite('flag.png',blank_image)
cv2.imshow('canvas',blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()