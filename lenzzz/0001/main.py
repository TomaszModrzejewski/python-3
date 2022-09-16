from random import randint

def makeCode(length,number):
    code = []
    code_set = set(code)
    code_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    limit = len(code_map)
    while (len(code_set)<number):
        this_code = "".join(code_map[randint(0,limit-1)] for _ in range(length))
        code.append(this_code)
        code_set = set(code)

    return code_set


if __name__ == '__main__':
    for i in makeCode(30,200):
        print i