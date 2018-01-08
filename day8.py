#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='Leon Hu'

from PIL import Image
import pytesseract

# 这里利用 pytesseract 找到 tesseract引擎的执行命令，否则会报 WindowsError: [Error 2] 异常
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

# 打开图片
img = Image.open('f:/code.jpg')

# 将图片进行灰度处理，即转化成单色图片
img_grey = img.convert('L')

img_grey.save('f:/gre.jpg','jpeg')

# 图片降噪。其实就是对已处理的灰度图片中被认为可能形成验证码字符的像素进行阀值设定,
# 如果阀值等于 70,我就认为是形成验证码字符串的所需像素,然后将其添加进一个空table中,
# 最后通过img_grey.point将使用table拼成一个新验证码图片
# 注意，阀值需要需要自己的图片去设置。
threshold = 70
tab = []
for i in range(256):
    if i < threshold:
        tab.append(0)
    else:
        tab.append(1)

# 用tab生成图片
img_grey.point(tab, '1')
img_grey.save('f:/black.jpg','jpeg')

# 读取处理好的图片
img_finished = Image.open('f:/black.jpg')
strcode = pytesseract.image_to_string(img_finished)

print(strcode)

