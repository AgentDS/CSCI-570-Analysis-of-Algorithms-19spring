#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/13/19 12:53 AM
# @Author  : Siqi Liang
# @Contact : zszxlsq@gmail.com
# @File    : Gale_Shapley_main.py
# @Software: PyCharm
import Gale_Shapley as gs
import numpy as np
from random import shuffle

if __name__ == '__main__':
    N = 3
    # man_favor_list = []
    # woman_favor_list = []
    # for m in range(N):
    #     favor = [i for i in range(N)]
    #     shuffle(favor)
    #     man_favor_list.append(favor)
    #
    # for w in range(N):
    #     favor = [i for i in range(N)]
    #     shuffle(favor)
    #     woman_favor_list.append(favor)

    man_favor_list = [[1, 2, 0], [1, 2, 0], [0, 1, 2]]
    woman_favor_list = [[2, 0, 1], [2, 1, 0], [2, 0, 1]]

    man = gs.ManGroup(N, man_favor_list)
    woman = gs.WomanGroup(N, woman_favor_list)

    gs_prob = gs.BestMatch(man, woman)
    gs_prob.solve_match()
    gs_prob.out()
