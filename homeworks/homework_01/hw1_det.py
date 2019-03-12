#!/usr/bin/env python
# coding: utf-8

import copy


def calculate_determinant(list_of_lists):
    print(list_of_lists)

    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    mx = list_of_lists
    if len(mx) == 0:
        return None
    size = len(mx)
    for list in mx:
        if len(list) != size:
            return None

    def recur(arg):
        res = 0
        mtx = copy.deepcopy(arg)
        if len(mtx) == 1:
            return mtx[0][0]
        if len(mtx) == 2:
            return (mtx[0][0]*mtx[1][1] - mtx[1][0] * mtx[0][1])
        item = mtx.pop(0)
        for i in range(0, len(arg)):
            cpmtx = copy.deepcopy(mtx)
            for k in range(0, len(mtx)):
                cpmtx[k].pop(i)
            res += (-1)**(i) * item[i] * recur(cpmtx)
        return res
    return recur(mx)
