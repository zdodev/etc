import win32com.client
import time

# Word 보고서 읽기
def read_word(wordfile):
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    print ("Oepn Word:", wordfile)
    word.Documents.Open(wordfile)
    doc = word.ActiveDocument

    time.sleep(4)
    content = []
    table = doc.Tables(4)
    content.append(table.Cell(Row = 2, Column = 1).Range.Text[:-2])
    content.append(table.Cell(Row = 2, Column = 2).Range.Text[:-2])

    word.Quit()

    return content
    
# 시작
excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = False
wb = excel.Workbooks.Open('C:\\Users\\finss\\Desktop\\test\\list.xlsx')
ws = wb.ActiveSheet

path = ws.Cells(1, 2).Value

list1 = []
print ("load word file list...")
for i in range(1, 360):
    filename = ws.Cells(i, 1).Value
    full_path = path + filename
    list1.append(full_path)

excel.Quit()

time.sleep(3)

excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")

for count in range(349, 360):
    print ((count + 1), "번째. 진행 중")
    output_con = read_word(list1[count])
    for i in range(2):
        ws.Cells(count + 1, i + 1).Value = output_con[i]
    

"""
for i in range(1, 3):
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    word.Documents.Open(list1[i - 1])
    doc = word.ActiveDocument
    table = doc.Tables(5)
    print table.Cell(Row = 2, Column = 2).Range.Text
""" 
    
"""
excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")

for row in range(2, 61):
    content = table.Cell(Row = row, Column = 2).Range.Text
    ws.Cells(row - 1, 1).Value = content[:-2]
    print "%-50s" % content[:-2], row
    value = table.Cell(Row = row, Column = 4).Range.Text
    ws.Cells(row - 1, 2).Value = value[:-2]
    print value[:-2], row

word.Quit()
"""
"""
str1 = str(table.Cell(Row = 4, Column = 2).Range.Text.encode('utf-8'))
str1 = str1[:-2].decode('utf-8')
list1 = []
list2 = []

for r in range(2,61):
    str1 = str(table.Cell(Row = r, Column = 2).Range.Text.encode('utf-8'))
    str1 = str1[:-2].decode('utf-8')
    list1.append(str1)
    str2 = str(table.Cell(Row = r, Column = 4).Range.Text.encode('utf-8'))
    str2 = str2[:-2].decode('utf-8')
    list2.append(str2)
    #print "%-50s" % (str1), " | ", str2

excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")

for i in list1:
    print i.encode('utf-8')

for r in range(59):
    ws.Cells(r + 1, 1).Value = list1[r]
    ws.Cells(r + 1, 2).Value = list2[r]

word.Quit()
"""

