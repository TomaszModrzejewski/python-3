import random
import string

words = string.ascii_letters + string.digits

def get_coupon(digit):
    return ''.join(random.choice(words) for _ in range(digit))

def two_hundred_coupons():
#    conpons = set()
    digit = 10
    for i in range(200):
        data = '%03d' % i                    ##数字编码放在最前面，保证验证码唯一性
        data += get_coupon(digit)
#        conpons.add(data)
        print(data)

two_hundred_coupons()
