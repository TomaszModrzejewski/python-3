#!/usr/bin.env python

import os


def main():
    f = open('code.cpp')
    blanks = 0
    comments = 0
    for line in f:
        if len(line.split()) == 0:
            blanks += 1
        elif line.startswith("//"):
            comments += 1
        elif line.startswith("/*"):
            comments += 1

    f = open('code.cpp')
    f = open('code.cpp')
    f = open('code.cpp')


if __name__ == '__main__':
    main()