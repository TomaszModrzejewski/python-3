# 第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
import random, string, time, math, uuid, redis

chars = string.ascii_letters + string.digits

def gen1():
    #key2 = ''.join(random.choice(chars) for i in range(10))
    return ''.join(random.sample(chars, 10))

def gen2():
    return math.modf(time.time())[0]

def gen3():
    return uuid.uuid4()

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    # r.set('name', 'will')
    # print(r.get('name'))
    for _ in range(200):
        r.sadd('code', gen1())
    r.save()
