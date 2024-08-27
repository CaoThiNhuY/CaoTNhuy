# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:23:49 2024

@author: Admin
"""

#Nhap ngay, thang, nam xuat theo dinh dang
ngay=int(input("Nhap ngay:"))
thang=int(input("Nhap thang:"))
nam=int(input("Nhap nam:"))
#aa/bb/cccc
print(f"{ngay}/{thang}/{nam}")
#aa/bb/cc
print(f"{ngay}/{thang}/{nam%100}")
#cccc/bb/aa
print(f"{nam}/{thang}/{ngay}")