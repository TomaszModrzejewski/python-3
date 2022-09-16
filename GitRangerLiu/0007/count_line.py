import os
from os.path import join
import re

comm = '[(#)(//)(/*)(*)]'
prog = re.compile(comm)

def count_line(root):
    codecount = 0
    emptycount = 0
    commcount = 0
    for root, dirs, files in os.walk(root):
        for name in files:
            filename = join(root, name)
            with open(filename) as f:
                for line in f:
                    if line.strip() == '':
                        emptycount += 1
                    #python script
                    elif prog.match(line.strip()) != None:
                        commcount += 1
                    else:
                        codecount += 1
    codecount = 0
    codecount = 0
    codecount = 0
    
if __name__ == '__main__':
    root = 'test'
    count_line(root)
