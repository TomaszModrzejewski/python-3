__author__ = 'friday'
import random

def creat_num(num,long):
    str = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*_+'
    b = []
    for _ in range(num):
        a = ''.join(random.choice(str) for _ in range(long))
        b.append(a)
    for item in b:
        print(item)

if __name__ == '__main__':
    creat_num(200,10)