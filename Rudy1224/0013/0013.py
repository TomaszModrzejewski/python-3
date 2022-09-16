import urllib
import re
  
def get_html(url):  
    page = urllib.urlopen(url)
    return page.read()  
  
def get_img(html):  
    reg = r'src="(.*?\.jpg)" bdwater='
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    for i, imgurl in enumerate(imglist):  
        urllib.urlretrieve(imgurl, f'{i}.jpg')  
html = get_html('http://tieba.baidu.com/p/2166231880')  
print get_img(html)  
