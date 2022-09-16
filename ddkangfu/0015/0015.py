# coding=utf-8

import json
import os

import xlwt

"""
0015: 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
    {
        "1" : "上海",
        "2" : "北京",
        "3" : "成都"
    }
请将上述内容写到 city.xls 文件中，如下图所示：

![student.xls](http://i.imgur.com/nPDlpme.jpg)
"""


def load_json_file(file_name):
    f = file(file_name)
    return json.load(f)


def save_as_xls(file_name, data):
    excel = xlwt.Workbook()

    file_names = os.path.splitext(os.path.basename(file_name))
    table = excel.add_sheet(file_names[0])

    for row, (k, v) in enumerate(data.items()):
        table.write(row, 0, k)
        table.write(row, 1, v)
    excel.save(file_name)


if __name__ == '__main__':
    if data := load_json_file("city.txt"):
        save_as_xls('city.xls', data)
