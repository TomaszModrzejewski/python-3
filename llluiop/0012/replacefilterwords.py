#!/usr/bin/env python

import os



def Words(path):
    f = open(path)
    return [word.strip('\n') for word in f]


if __name__ == '__main__':
    filteredwords = Words('filtered_words.txt')

    while True:
        input = raw_input("input your line:")

        for word in filteredwords:
            if word in input:
                input = input.replace(word, ''.join(['*' for _ in range(len(word))]))

        input = raw_input("input your line:")
