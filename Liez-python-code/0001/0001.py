
# coding = utf-8
__author__= 'liez'

import random

def make_number(num, length):
    str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    a = []
    i = 0
    while i < num:
        numstr = ''.join(random.choice(str) for _ in range(length))
        if numstr not in a: #如果没重复
            a.append(numstr)
            i += 1
            print(numstr)

make_number(20,10)
