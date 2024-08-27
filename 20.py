# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:58:14 2024

@author: ny
"""

a=int(input("Nhap so nguyen a="))
b=int(input("Nhap so nguyen b="))
c=int(input("Nhap so nguyen c="))
#ví dụ a là GTLN
GTLN=a
if b>GTLN:
    GTLN=b
if c>GTLN:
    GTLN=c
print("GTLN (",a,",",b,",",c,")=",GTLN)