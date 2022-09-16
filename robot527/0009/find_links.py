#! usr/bin/python3
"""
第 0009 题：一个HTML文件，找出里面的链接。
"""


import re, urllib.request
url = input('Enter the URL which you wish to extract > ')
if url == '':
    url = "https://adblockplus.org/zh_CN/acceptable-ads"

print(f'We will extract links from {url} :')


with urllib.request.urlopen(url) as response:
    content = response.read()
    try:
        content = content.decode('utf-8')
    except UnicodeDecodeError:
        content = content.decode('gbk')
    link_list = re.findall('''(?<=href=)["'](.[^"']+)["']''', content)
    for i, item in enumerate(link_list, start=1):
        print('%d:' % i, item)
