# -*- coding:utf-8 -*-
from xlwt import Workbook
import json

file = open('city.txt','rb')
text = file.read().decode('gbk')
js = json.loads(text)
book = Workbook()
sheet = book.add_sheet('city')
js2 = sorted(js)
colnum = 0
for rownum, i in enumerate(js2):
    sheet.write(rownum,colnum,unicode(i))
    sheet.write(rownum,colnum+1,unicode(js[i]))
book.save('city.xls')