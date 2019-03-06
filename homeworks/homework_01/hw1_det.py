#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(l_of_l):
    n = len(l_of_l)
    for list_hor in l_of_l:
        if len(list_hor) != n:
            return None
    if n < 2:
        return None
    if n > 2:
        i = 1
        t = 0
        sum = 0
        while t <= n-1:
            d = {}
            t1 = 1
            while t1 <= n-1:
                m = 0
                d[t1] = []
                while m <= n-1:
                    if m != t:
                        d[t1].append(l_of_l[t1][m])
                    m += 1
                t1 += 1
                l_of_l1 = [d[x] for x in d]
            sum = sum+i*(l_of_l[0][t])*(calculate_determinant(l_of_l1))
            i = i*(-1)
            t += 1
        return sum
    else:
        return l_of_l[0][0]*l_of_l[1][1]-l_of_l[0][1]*l_of_l[1][0]


# a = [[1, 2, 6, 8], [4, 6, 7, 5], [7, 1, 8, 9], [2, 1, 8, 5]]
# print(calculate_determinant(a))
# a = [[1, 2, 6], [4, 6, 7], [7, 1, 8], [2, 1, 8]]
# print(calculate_determinant(a))
# a = [[1, 2], [4, 6]]
# print(calculate_determinant(a))
