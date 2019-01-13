#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/13/19 12:15 PM
# @Author  : Siqi Liang
# @Contact : zszxlsq@gmail.com
# @File    : nnn.py
# @Software: PyCharm
import numpy as np

l1 = [1, 2, 3, 4]
l2 = ['2', '4', 'a']
l3 = [1.1111111111, 1, 2]
print(all(type(item) == int or type(item) == float for item in l1))
print(all(type(item) == int or type(item) == float for item in l2))
print(all(type(item) == int or type(item) == float for item in l3))
