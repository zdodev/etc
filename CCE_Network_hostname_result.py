#-*- coding: utf-8 -*-

import win32com.client
import os
import time

# Word 보고서 읽기
def read_word(wordfile):
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    word.Documents.Open(wordfile)
    doc = word.ActiveDocument

    time.sleep(4)
    content = []
    table = doc.Tables(4)
    content.append(table.Cell(Row = 2, Column = 1).Range.Text[:-2])

    time.sleep(1)
    table = doc.Tables(5)
    for i in range(2, 61):
        """
        출력 테스트
        print table.Cell(Row = i, Column = 2).Range.Text[:-2]
        """
        content.append(table.Cell(Row = i, Column = 4).Range.Text[:-2])
    word.Quit()

    return content
    
# 시작

os.chdir('C:\\Users\\finss\\Desktop\\NETWORK_20170620')
pwd = os.getcwd()
file_list = os.listdir()

"""
excel2 = win32com.client.Dispatch('Excel.Application')
excel2.Visible = True
wb2 = excel2.Workbooks.Add()
ws2 = wb2.Worksheets("Sheet1")
"""
list_total = []

for i in range(1, 54):
    list1 = []
    excel1 = win32com.client.Dispatch('Excel.Application')
    excel1.Visible = False
    print(file_list[i - 1])
    wb1 = excel1.Workbooks.Open(pwd + '\\' + file_list[i - 1])
    ws1 = wb1.ActiveSheet

    list1.append(file_list[i - 1])
    for j in range(2, 38):
        list1.append(ws1.Cells(j, 4).Value)

    list_total.append(list1)
    excel1.Quit()
    del excel1

excel2 = win32com.client.Dispatch('Excel.Application')
excel2.Visible = True
wb2 = excel2.Workbooks.Add()
ws2 = wb2.Worksheets("Sheet1")

for i in range(1, 54):
    for j in range(2, 38):
        ws2.Cells(j - 1, i).Value = list_total[i - 1][j - 2]

