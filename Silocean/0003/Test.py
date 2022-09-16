# -*-coding:utf-8-*-
__author__ = 'Tracy'
import redis, uuid

r = redis.StrictRedis(host='localhost', port=6379)
for i in range(200):
    r.set(f'key_id{str(i)}', uuid.uuid1())

for i in range(200):
    print(r.get(f"key_id{str(i)}"))