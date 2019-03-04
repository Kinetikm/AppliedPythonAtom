#!/usr/bin/env python
# coding: utf-8

# CHET NE VZLETELO

def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
#     new_dict = {}
#
#     if not source_dict:
#         return source_dict
#     for k, v in source_dict.items():
#         if isinstance(v, (list, tuple, set)):
#             for v2 in get1List(v):
#                 helper(k, v2, new_dict)
#         else:
#             helper(k, v, new_dict)
#
#     return new_dict
#
#
# def helper(k, v, dict):
#     if v in dict.keys():
#         if isinstance(dict[v], list):
#             dict[v].append(k)
#         else:
#             tmp = dict[v]
#             dict[v] = [tmp, k]
#     else:
#         dict[v] = k
#
# def get1List(lst):
#     tmp = []
#     tmp.append(findList(lst))
#     return tmp
#
# def findList(lst):
#     tmp = []
#     if not lst:
#         return
#     if isinstance(lst, (list, tuple, set)):
#         for i in lst:
#             findList(i)
#     else:
#         tmp.append(lst)
#     return tmp

    raise NotImplementedError
