# -*-coding:utf-8-*-
__author__ = 'Tracy'

import uuid

with open('keys.txt', 'w') as f:
    for _ in range(200):
        f.write(str(uuid.uuid1())+"\n")

