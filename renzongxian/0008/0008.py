# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-20
# Python 3.4

"""

第 0008 题：一个HTML文件，找出里面的正文。

"""

import urllib.request
import re


def get_body(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>')
    return r.findall(html_content.decode('GBK').encode('utf-8'))


if __name__ == '__main__':
    body = get_body('http://tech.163.com/14/1219/01/ADPT7MTE000915BF.html')
    with open('result.txt', 'w') as file_object:
        for l in body:
            file_object.write(l + '\n')

