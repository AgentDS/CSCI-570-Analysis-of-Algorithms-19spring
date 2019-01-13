#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/13/19 12:52 AM
# @Author  : Siqi Liang
# @Contact : zszxlsq@gmail.com
# @File    : Gale_Shapley.py
# @Software: PyCharm

import numpy as np


class ManGroup(object):
    def __init__(self, N, favor_list):
        self.N = N
        self.favor_list = favor_list  # list in list


class WomanGroup(object):
    def __init__(self, N, favor_list):
        self.N = N
        self.favor_list = favor_list  # list in list


class BestMatch(object):
    def __init__(self, man, woman):
        self.man = man
        self.woman = woman
        self.N = man.N
        self.man_engage_flag = np.zeros(man.N, dtype=int)
        self.woman_engage_flag = np.zeros(man.N, dtype=int)
        self.dating_flag = np.zeros(shape=(man.N, man.N), dtype=int)
        self.man_dating = np.ones(self.N, dtype=int) * (-1)
        self.woman_dating = np.ones(self.N, dtype=int) * (-1)

    def exist_free_man(self):
        for i in range(self.N):
            if self.man_dating[i] == -1:
                if np.sum(self.dating_flag[:, i]) < self.N:
                    return True
            else:
                continue
        return False

    def find_free_man(self):
        for i in range(self.N):
            if self.man_engage_flag[i] == 0:
                return i
            else:
                continue
        return -1

    def find_prefer_woman(self, man_id):
        prefer_list = self.man.favor_list[man_id]
        for i in range(self.N):
            w = prefer_list[i]
            if self.dating_flag[w, man_id] == 0:
                return w
            else:
                continue
        return -1

    def prefer_m_(self, w, m, m_):
        w_prefer = self.woman.favor_list[w]
        idx_m = w_prefer.index(m)
        idx_m_ = w_prefer.index(m_)
        if idx_m_ < idx_m:
            return True
        else:
            return False

    def solve_match(self):
        N = self.N
        while self.exist_free_man():
            m = self.find_free_man()
            w = self.find_prefer_woman(m)
            if self.woman_engage_flag[w] == 0:
                self.dating_flag[w, m] = 1
                self.man_dating[m] = w
                self.woman_dating[w] = m
                self.man_engage_flag[m] = 1
                self.woman_engage_flag[w] = 1
            else:
                m_ = self.woman_dating[w]
                self.dating_flag[w, m] = 1
                if self.prefer_m_(w, m, m_):
                    self.man_engage_flag[m] = 0
                else:
                    self.woman_dating[w] = m
                    self.man_dating[m] = w
                    self.man_dating[m_] = -1
                    self.man_engage_flag[m_] = 0
                    self.man_engage_flag[m] = 1
                    self.woman_engage_flag[w] = 1

        print('Problem solved.')

    def out(self):
        print('Prefer list::')
        for i in range(self.N):
            print('man', i, end=': ')
            print(self.man.favor_list[i])

        for i in range(self.N):
            print('woman', i, end=': ')
            print(self.woman.favor_list[i])

        print('Man --- Woman')
        for i in range(self.N):
            print(' ', i, end='')
            print(end=' --- ')
            print(self.man_dating[i])
