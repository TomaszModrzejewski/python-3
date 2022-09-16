#coding=utf-8
import json, xlwt, os
f = open(f"{os.path.split(os.path.realpath(__file__))[0]}/city.txt")
dict = json.loads(f.read().decode("GBK"))
xls = xlwt.Workbook()
sheet = xls.add_sheet("city")
col = 0
for i in range(len(dict.keys())):
	row = i
	sheet.write(row, col, dict.keys()[i])
	sheet.write(row, col+1, dict[dict.keys()[i]])
xls.save(f"{os.path.split(os.path.realpath(__file__))[0]}/city.xls")