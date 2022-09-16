with open('a.txt', 'rb') as f:
    lines = f.readlines()
f = open('a.txt', 'rb')
f.close()

with open('a.txt', 'rb') as f:
    while true:
        line = f.readline()
        if not line:
            break
