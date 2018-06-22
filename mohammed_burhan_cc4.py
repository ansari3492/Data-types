# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:11:06 2018

@author: Lenovo
"""


str3=input("enter string: ").strip()
x=str3.find(" ")
print (str3[x:].strip(),str3[0:x].strip()) 