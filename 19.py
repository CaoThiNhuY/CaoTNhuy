# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:48:36 2024

@author: nhuy
"""

a=int(input("Nhap so nguyen a="))
b=int(input("Nhap so nguyen b="))
c=int(input("Nhap so nguyen c="))
d=int(input("Nhap so nguyen d="))
#Ví dụ cho a là GTNN
GTNN=a
if b<GTNN:
    GTNN=b
if c<GTNN:
    GTNN=c
if d<GTNN:
    GTNN=d
print("GTNN(",a,",",b,",",c,",",d,")=",GTNN)