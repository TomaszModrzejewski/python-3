# -*- coding:utf-8 -*-
from xml.dom import minidom
from xlrd import open_workbook
import re

axls = open_workbook('city.xls')
sheet1 = axls.sheet_by_name('city')
jdict = {
    str(sheet1.cell(i, 0).value): str(sheet1.cell(i, 1).value).decode('gbk')
    for i in range(3)
}

s = str(jdict)
s = re.sub('{','{\n\t ',s)
s = re.sub('}','\n}',s)
s = re.sub(',',',\n\t',s)
from xml.dom import minidom
doc = minidom.Document()
root = doc.createElement('root')
doc.appendChild(root)
students = doc.createElement('citys')
comment = doc.createComment(u'\n\t城市信息\n')
students.appendChild(comment)
students_text = doc.createTextNode(s.decode('unicode_escape'))
students.appendChild(students_text)
root.appendChild(students)
with open("city.xml", "wb") as f:
    f.write(doc.toprettyxml(indent = "", newl = "\n", encoding = "utf-8"))