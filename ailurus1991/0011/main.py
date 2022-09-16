#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jinyang'


def readFile(filePath):
    file = open(filePath, 'r')
    return [word.strip('\n') for word in file]

def check(testWord):
    realWords = readFile('filtered_words.txt')
    for i in realWords:
        if i == testWord:
            print 'Freedom'
            return
    else:
        print 'Human Rights'
        return

if __name__ == '__main__':
    check('sss')