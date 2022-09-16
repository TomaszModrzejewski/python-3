import random, string


def gen_charint(filename, width = 4, num = 200):
    with open(filename, 'wb') as f:
        charint = string.digits + string.letters
        for _ in range(num):
            verify = [random.choice(charint) for _ in range(width)]
            verify = ''.join(verify) + '\n'
            f.write(verify)

if __name__ == '__main__':

    filename = 'result.txt'
    width = 4
    num = 200
    gen_charint(filename, width, num)

    
