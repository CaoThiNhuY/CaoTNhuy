# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:15:00 2024

@author: Admin
"""

# Nhập ba số nguyên từ người dùng
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))

# Tìm số lớn nhất và nhỏ nhất
max_so = max(a, b, c)
min_so = min(a, b, c)

# In kết quả
print("Số lớn nhất là:", max_so)
print("Số nhỏ nhất là:", min_so)