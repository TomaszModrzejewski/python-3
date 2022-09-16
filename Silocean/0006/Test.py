# -*-coding:utf-8-*-
__author__ = 'Tracy'
import os,re

path = 'diaries'
files = os.listdir(path)

def get_key_word(words):
    dic = {}
    max = 0
    marked_key = ''
    for word in words:
        dic[word] = 1 if dic.has_key(word) is False else dic[word] + 1
    for key in dic:
        if dic[key] > max:
            max = dic[key]
            marked_key = key
    print(marked_key, max)


for f in files:
    with open(os.path.join(path, f)) as diary:
        words = re.findall("[a-zA-Z]+'*-*[a-zA-Z]*",diary.read())
        get_key_word(words)