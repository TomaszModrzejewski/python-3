#!/usr/bin/env python

import os



def Words(path):
    f = open(path)
    return [word.strip('\n') for word in f]


if __name__ == '__main__':
    filteredwords = Words('filtered_words.txt')

    while(True):
        input = raw_input("input your line:").split()

        if set(input).intersection(filteredwords):
                print 'Freedom'
        else:
            print 'Human Rights'


