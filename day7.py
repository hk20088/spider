#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='Leon Hu'

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 生成随机字母（在ASCII编码中，A的编码是65，Z的编码是90. z的编码是122， 这里生成A-Z的随机字母）
def rndChar():
    return chr(random.randint(65,90))

# 生成随机数字
def rndCou():
    return str(random.randint(0,9))

# 随机颜色1
def rndColor1():
    return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

# 随机颜色2
def rndColor2():
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))


def createCode():
    width = 60 * 4
    height = 60
    # 创建白色图片（RGB值域从0到255，其中0为黑色，255为白色）
    img = Image.new('RGB', (width, height), (255, 255, 255))

    # 创建font对象（如果出现 OSError: cannot open resource 异常，说明pillow没有定位到字体文件，修改正确的字体文件的路径即可）
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)

    # 创建Draw对象，用于向白色背景图片上绘图
    draw = ImageDraw.Draw(img)

    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor1())

    # 输出文字
    str = ''
    for t in range(4):
        conts = [rndChar(),rndCou()]
        con = random.choice(conts)
        draw.text((60 * t + 10, 10), con, font=font, fill=rndColor2())
        str = str+con

    # 打印验证码
    print(str)
    # 模糊图片
    img = img.filter(ImageFilter.BLUR)
    # 保存图片
    img.save('code.jpg', 'jpeg')




if __name__ == '__main__':
    print(createCode())

