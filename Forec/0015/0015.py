# coding = utf-8
__author__ = 'Forec'
import xlwt
import re

book = xlwt.Workbook(encoding = 'utf-8', style_compression=0)
sheet = book.add_sheet('student',cell_overwrite_ok = True)
info = re.compile(r'\"(\d+)\" : \"(.*?)\"')
with open('city.txt',"r") as f:
    data = f.read()
for line, x in enumerate(info.findall(data)):
    for i in range(len(x)):
        sheet.write(line,i,x[i])
book.save('city.xls')