# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:06:05 2024

@author: Admin
"""

a=input("Thoi gian gio, phut, giay:")
b=a.split(":")
hh,mm,ss=map(int, b)
tong_giay=hh*60*60 +mm*60 + ss
print("tong giay la:", tong_giay)