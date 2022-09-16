# -*- coding: utf-8 -*-
'''
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，
则变成「**是个好城市」。
'''
import string

def filter_word():
    with open('filtered_words.txt', 'rb') as f:
        words = [line.strip() for line in f]
    while(True):
        text = raw_input('>')
        for word in words:
            if word in text:
                text = string.replace(text, word, gen_asterisk(word))

#Each Chinese character is replace by one asterisk, and each English character
#by one asterisk.
def gen_asterisk(word):
    return len(word) * '*' if word.isalnum() else '*' * (len(word) / 2)
    
if __name__ == '__main__':
    filter_word()
