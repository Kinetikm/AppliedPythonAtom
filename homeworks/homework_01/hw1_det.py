#!/usr/bin/env python
# coding: utf-8


import copy
def minor( A, i, j ):  #minor
    M = copy.deepcopy(A) 
    del M[ i ]
    for i in range( len( A[0] ) - 1 ):
        del M[ i ] [ j ]
    return M   
    
def calculate_determinant(list_of_lists):
    A = list_of_lists
    for stroka in A:
        if len(stroka)!=len(A):
            return None
    m = len( A )
    n = len( A[0] )
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    kf = 1 #znak
    d = 0
    for j in range( n ):
        d += A[0][j]*kf*calculate_determinant( minor( A, 0, j ) ) 
        kf *= -1
    return d 
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    raise NotImplementedError