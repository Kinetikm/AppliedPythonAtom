#!/usr/bin/env python
# coding: utf-8


def simpl(lst):
    ans = list()
    qu = list()
    qu.append(lst)
    while len(qu) > 0:
        nxt = qu[-1]
        qu.pop()
        if type(nxt) in [type(int(1)), type(float(1.0)),
                         type(''), type(Ellipsis)]:
            ans.append(nxt)
        else:
            for i in nxt:
                qu.append(i)
    return ans


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    ans = {}
    for key in source_dict:
        for i in simpl(source_dict[key]):
            ans[i] = []
    for key in source_dict:
        for i in simpl(source_dict[key]):
            ans[i].append(key)
    for key in ans:
        try:
            if len(ans[key]) == 1:
                ans[key] = ans[key][0]
        except KeyError:
            continue
    return ans
