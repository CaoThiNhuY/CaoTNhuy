# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:10:05 2024

@author: Admin
"""

h=int(input("Nhap gio (1):"))
p=int(input("Nhap phut (1):"))
s=int(input("Nhap giay (1):"))

h2=int(input("Nhap gio (2):"))
p2=int(input("Nhap phut (2):"))
s2=int(input("Nhap giay (2):"))
#tính ra tổng hiệu 2 giờ theo hướng đổi ra giờ
t1=h+p/60+s/3600
print("t1=",t1)
t2=h2+p2/60+s2/3600
print("t2=",t2)
print(f"{t1:.2f} + {t2:.2f} = {t1+t2:.2f}")
print(f"{t1:.2f} - {t2:.2f}= {t1-t2:.2f}")
#tính ra tổng hiệu 2 giờ và cho ra kết quả theo định dạng giờ,phút,giây
from datetime import timedelta
tg1=timedelta(hours=h,minutes=p,seconds=s)
tg2=timedelta(hours=h2,minutes=p2,seconds=s2)
print("Tong 2 gio la:",tg1)
print("Hieu 2 gio la:",tg2)