# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:44:32 2024

@author: ny
"""
h= int(input("Nhap gio (0-23): "))
m= int(input("Nhap phut (0-59): "))
s= int(input("Nhap giay (0-59): "))
if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
    print("Gio, phut, giay ban nhap la hop le.")
else:
    print("Gio, phut, giay ban nhap khong hop le.")
    