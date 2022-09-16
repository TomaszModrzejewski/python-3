import string
import random
def coupon_creator(digit):
    return ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for _ in range(digit)
    )
    
def two_hundred_coupons():
    data=''
    count=1
    digit=12
    for count in range(200):
        count+=1
        data += f'coupon no.{count}  {coupon_creator(digit)}' + '\n'

    return data


with open('coupondata.txt','w') as coupondata:
    coupondata.write(two_hundred_coupons())