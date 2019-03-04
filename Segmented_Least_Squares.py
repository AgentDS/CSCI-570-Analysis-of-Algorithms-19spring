#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/4/19 12:38 AM
# @Author  : Siqi Liang
# @Contact : zszxlsq@gmail.com
# @File    : Segmented_Least_Squares.py
# @Software: PyCharm
import numpy as np


def generate_data_set(a, b, x):
    s = len(a)
    n = x.shape[0]
    group_x = []
    first = 0
    last = np.floor(n / 4)
    for i in range(s):
        if i != s - 1:
            group_x.append(x[first:last])
        else:
            group_x.append(x[first::])
        first = last + 1
        last += np.floor(n / 4)
    group_y = []
    for i in range(s):
        y = group_x[i] * a[i] + b[i]
        group_y.append(y)
