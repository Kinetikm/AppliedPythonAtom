#!/usr/bin/env python
# coding: utf-8


import copy
def RemoveS(matr, i, j):
    del matr[i]
    for count in range(len(matr)):
        del matr[count][j]

def calculate_determinant(list_of_lists):
    k=0
    if list_of_lists == [[]]:
        return None
    prinf("----------------------------------------->", len(list_of_lists))
    if len(list_of_lists) > 2:
        for count in range(len(list_of_lists)):
            matr2_0=copy.deepcopy(list_of_lists)
            RemoveS(matr2_0, count, 0)
            k=k+((-1)**(count+2)) * list_of_lists[count][0] * \
              calculate_determinant(matr2_0)
        return k
    elif len(list_of_lists) == 2:
        return list_of_lists[0][0] * list_of_lists[1][1]-\
               list_of_lists[0][1] * list_of_lists[1][0]
    elif len(list_of_lists) == 1:
        return list_of_lists[0][0]
    else:
        return None

# print(calculate_determinant([[]]))
b=[[2, 4, 1, 244],[3, 7, 8, 234], [1, 2, 5, 127], [4, 1, 87, 95]]
# print(calculate_determinant(b))
print(calculate_determinant([[]]))
# def Determinant(matr):
#     k=0
#     if len(matr) > 2:
#         for count in range(len(matr)):
#             matr2_0=copy.deepcopy(matr)
#             RemoveS(matr2_0, count, 0)
#             k=k+((-1)**(count+2))*matr[count][0] * \
#               Determinant(matr2_0)
#         return k
#     else:
#         return matr[0][0] * matr[1][1]-\
#                matr[0][1] * matr[1][0]