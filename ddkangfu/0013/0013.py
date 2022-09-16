# coding=utf-8

import urllib2
import urllib
import os

from bs4 import BeautifulSoup

"""
0013:用 Python 写一个爬图片的程序，爬 [这个链接里的日本妹子图片 :-)](http://tieba.baidu.com/p/2166231880)
"""


def get_img_src_list(url, img_class):
    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content)
    return [img['src'] for img in soup.find_all('img', img_class)]   


def download_img(src, download_path):
    print 'Begin download image : %s ......' % src

    file_name =  src.split("/")[-1]
    dist = os.path.join(download_path, file_name)

    urllib.urlretrieve(src, dist, None)

    print 'Download image %s Done.' % src



if __name__ == '__main__':
    if src_list := get_img_src_list(
        'http://tieba.baidu.com/p/2166231880', 'BDE_Image'
    ):
        save_path = os.path.abspath("./downlaod")
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        for src in src_list:
            download_img(src, save_path)

        save_path = os.path.abspath("./downlaod")
    save_path = os.path.abspath("./downlaod")


