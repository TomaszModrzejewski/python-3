#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: key
# @Date:   2015-11-17 22:21:34
# @Last Modified by:   key
# @Last Modified time: 2015-11-18 21:13:01

'''
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
'''

import glob
from PIL import Image

def change_resolution(patterns):
    iphone_width = 750
    iphone_height = 1334
    pictures = []
    for pattern in patterns:
        pictures.extend(glob.glob(pattern))
    print(pictures)
    for picture in pictures:
        img = Image.open(picture)
        width = min(iphone_width, img.size[0])
        height = min(iphone_height, img.size[1])
        print(width,height)
        dist = img.resize((width,height),Image.ANTIALIAS)
        dist.save(f"ipone6_{picture}")

if __name__ == '__main__':
    change_resolution(("*.jpg","*.png"))
