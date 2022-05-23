#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Filename:jinxiaojian
# Create Time: 2022/5/15 上午 02:33
import openpyxl

class Excel:

    def __init__(self,filename,sheet_name):

        self.filename = filename
        self.sheet_name = sheet_name

    def open(self):
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheet_name]

    def read_data(self):
        self.open()
        res=list(self.sh.rows)
        title=[c.value for c in res[0]]
        cases_data=[]
        for row in res[1:]:
            data=[c.value for c in row]
            case= dict(zip(title,data))
            cases_data.append(case)
        return cases_data

    def write_data(self,row,column,value):
        self.open()
        self.sh.cell(row=row,column=column,value=value)
        self.wb.save(self.filename)