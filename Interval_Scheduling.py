#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/10/19 5:43 PM
# @Author  : Siqi Liang
# @Contact : zszxlsq@gmail.com
# @File    : Interval_Scheduling.py
# @Software: PyCharm
import numpy as np


class Scheduling_Problem():
    def __init__(self, N, starts, ends):
        self.N = N
        self.Rstarts = starts
        self.Rends = ends
        self.Astart = []
        self.Aend = []

    def solve(self):
        while len(self.Rstarts) != 0:
            first_finish_end = min(self.Rends)
            self.Aend.append(first_finish_end)
            Ridx = self.Rends.index(first_finish_end)
            first_finish_start = self.Rstarts[Ridx]
            self.Astart.append(first_finish_start)
            self.delete_overlap(first_finish_start, first_finish_end)
        idx_order = np.argsort(self.Astart)
        self.Astart.sort()
        self.Aend = np.array(self.Aend)[idx_order].tolist()

    def result(self):
        for i in range(len(self.Astart)):
            print('Event %d -- starts at %.3f, ends at %.3f' % (i + 1, self.Astart[i], self.Aend[i]))

    def delete_overlap(self, start, end):
        new_start = []
        new_end = []
        for i in range(len(self.Rstarts)):
            if end <= self.Rstarts[i] or start >= self.Rends[i]:
                new_start.append(self.Rstarts[i])
                new_end.append(self.Rends[i])
        self.Rends = new_end
        self.Rstarts = new_start
