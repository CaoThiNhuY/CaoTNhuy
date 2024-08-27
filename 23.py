# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:59:46 2024

@author: Admin
"""

import math
a=float(input("Nhap a="))
b=float(input("Nhap b="))
c=float(input("Nhap c="))
if a==0:
    if b==0:
        if c!=0:
            print("Phuong trinh vo nghiem")
        if c==0:
            print("Phuong trinh co vo so nghiem")
    if b!=0:
        x=-c/b
        print("Phuong trinh co nghiem x=",x)
else:
    delta=b**2 - 4*a*c
    if delta<0:
        print("Phuong trinh vo nghiem")
    if delta==0:
        x1=x2=-b/2*a
        print("Phuong trinh co nghiem kep x1=","x2=",x1)
    if delta>0:
        x1=(-b-(math.sqrt(delta)**2))/2*a
        x2=(-b+(math.sqrt(delta)**2))/2*a
        print("Phuong trinh co 2 nghiem phan biet x1=",x1)
        print("x2=",x2)