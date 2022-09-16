# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-21
# Python 3.4

"""

第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge

"""


def filter_words(words):
    with open('filtered_words.txt', 'r') as file_object:
        filtered_words = [line.strip('\n') for line in file_object]
    filtered = any(filtered_word in words for filtered_word in filtered_words)
    if filtered:
        print('Freedom')
    else:
        print('Human Rights')

if __name__ == '__main__':
    while True:
        input_words = input('Input some words:')
        filter_words(input_words)

