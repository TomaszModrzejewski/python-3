import random, string

with open('Promo_code.txt', 'wb') as f:
    for _ in range(200):
        chars = string.letters + string.digits
        s = [random.choice(chars) for _ in range(10)]
        f.write(''.join(s) + '\n')