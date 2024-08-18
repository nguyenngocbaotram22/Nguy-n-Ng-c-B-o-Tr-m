# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:21:05 2024

@author: Admin
"""

distance=float(input("nhap do dai den truongm"))
if distance>1200:
    print("thoi nho ban cho")
elif distance<300:
    print("di bo tot")
elif distance>=300 and distance<=1200:
    print("thoi nho ban cho")
else:
    print("khong biet nua")