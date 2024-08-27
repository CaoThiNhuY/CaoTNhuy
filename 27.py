# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:44:53 2024

@author: ny
"""
import math
hinh = input("Nhap hinh (v - hinh vuong, n - hinh chu nhat, t - hinh tron): ")
if hinh=="v":
    canh=float(input("Nhap canh cua hinh vuong;"))
    S_vuong=canh*canh
    P_vuong=4*canh
    print(f"Chu vi: P={P_vuong}")
    print(f"Dien tich: S={S_vuong} ")
elif hinh=="n":
    a=float(input("Nhap chieu dai: "))
    b=float(input("Nhap chieu rong:"))
    s_cn=a*b
    p_cn=(a+b)*2
    print("Chu vi: S=",s_cn)
    print("Dien tich: P=",p_cn)
elif hinh=="t":
    R=float(input("Nhap ban kinh R="))
    C=2*math.pi*R
    S_tron=R**2*math.pi
    print("Chu vi: C=",C)
    print("Dien tich: S=",S_tron)
else:
    print("Khong xac dinh")