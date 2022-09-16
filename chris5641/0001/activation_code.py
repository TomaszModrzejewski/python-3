# -*- coding: utf-8 -*-
"""
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import random

__author__ = 'Chris5641'


def get_code():
    with open('ActivationCode.txt', 'w') as f:
        char_seq = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for _ in range(200):
            code = ''.join(random.choice(char_seq) for _ in range(9))
            f.write(code+'\n')


if __name__ == '__main__':
    get_code()

