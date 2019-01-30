# -*- coding: UTF-8 -*-
import xlrd
def read_excel(path):
    workbook = xlrd.open_workbook(path)
    sheet0=workbook.sheet_by_index(0);
    listUrl=[]
    listpwd=[]
    rownum=sheet0.nrows
    for index in range(rownum):
        listUrl.append(sheet0.cell(index,0).value.encode('utf-8'))
        listpwd.append(sheet0.cell(index,1).value.encode('utf-8'))
    return listUrl,listpwd
if __name__ == '__main__':
    path=r'C:\filetmp\demo.xlsx'
    listUrl,listpwd=read_excel(path)
    print listUrl
    print listpwd
