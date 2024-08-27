# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:11:52 2024

@author: NY
"""
h=int(input("Nhap gio:"))
p=int(input("Nhap phut:"))
s=int(input("Nhap giay:"))
#theo định dạng gio/phut/giay
print(f"{h}/{p}/{s}")
giay=h*3600+p*60+s
print("Tong giay la:",giay)
#theo ví dụ 1h8p8s
print(f"{h}h{p}p{s}s")
giay=h*3600+p*60+s
print("Tong giay la:",giay)