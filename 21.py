# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:26:49 2024

@author: ny
"""

so=int(input("Nhap so bat ki:"))
cac_so={0:"Khong",1:"Mot",2:"Hai",3:"Ba",4:"Bon",5:"Nam",6:"Sau",7:"Bay",8:"Tam",9:"Chin"}
if 0<= so <= 9:
    print(cac_so[so]) #in ra chuỗi tương ứng với số nguyên so đã nhập.
else:
    print("Khong doc duoc")