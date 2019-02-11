#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/10/19 5:44 PM
# @Author  : Siqi Liang
# @Contact : zszxlsq@gmail.com
# @File    : Interval_scheduling_main.py
# @Software: PyCharm
from Interval_Scheduling import *
from numpy import random

if __name__ == '__main__':
    random.seed(0)
    N = 10
    starts = random.rand(N) * 10
    interval = random.rand(N) * 20
    ends = starts + interval
    prob = Scheduling_Problem(N, starts.tolist(), ends.tolist())
    prob.solve()
    prob.result()
