# -*- coding:utf-8 -*-
#第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）

import random, string

forSelect = f"{string.ascii_letters}0123456789"

def generate(count, length):
    # count = 200
    # length = 20

    for _ in range(count):
        Re = "".join(random.choice(forSelect) for _ in range(length))
        print(Re)

if __name__ == "__main__":
    generate(200, 20)
