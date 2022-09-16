#!/usr/bin/python
#coding:utf-8
# Author: cijianzy
# Created Time: 2015年06月14日 星期日 17时43分18秒

from uuid import uuid4
def get_key(num):
    return [str(uuid4()) for _ in range(num)] 
print get_key(200)

