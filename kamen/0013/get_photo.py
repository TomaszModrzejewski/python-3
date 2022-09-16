from urllib import urlopen
from bs4 import BeautifulSoup

f = urlopen('http://tieba.baidu.com/p/2166231880').read()
#print f
s = BeautifulSoup(f)
s_imgs = s.find_all('img', pic_type='0')
for i, s_img in enumerate(s_imgs, start=1):
    img_url = s_img['src']
    img_content = urlopen(img_url).read()
    img_url = s_img['src']
    file_name = f'{str(i)}.jpg'
    with open(file_name, 'wb') as wf:
        wf.write(img_content)
    
    
