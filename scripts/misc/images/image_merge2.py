# -*- coding: utf-8 -*-
# @Author  : Threekiii
# @Time    : 2023/5/19 19:24
# @Function: 图片拼接（方法2），例如将 1000 张图片拼接为 1 张图片

from PIL import Image
 
def join(png1, png2, flag='horizontal'):
  """
  :param png1: path
  :param png2: path
  :param flag: horizontal or vertical
  :return:
  """
  img1, img2 = Image.open(png1), Image.open(png2)
  size1, size2 = img1.size, img2.size
  if flag == 'horizontal':
    joint = Image.new('RGB', (size1[0]+size2[0], size1[1]))
    loc1, loc2 = (0, 0), (size1[0], 0)
    print(loc1, loc2)
    joint.paste(img1, loc1)
    joint.paste(img2, loc2)
    joint.save('horizontal.png')
  elif flag == 'vertical':
    joint = Image.new('RGB', (size1[0], size1[1]+size2[1]))
    loc1, loc2 = (0, 0), (0, size1[1])
    joint.paste(img1, loc1)
    joint.paste(img2, loc2)
    joint.save('vertical.png')
 
if __name__ == '__main__':
  try:
    num = 1000
    png = 'first_slice.png'
    for n in range(0,num):
      filename = "./" + str(n) + ".png"
      join(png, filename)
  except Exception as e:
    print(e)