#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    if type(source_dict) == dict:
        import copy
        d = copy.deepcopy(source_dict)
        lst = []

        def unpack(smth):
            l = list(smth)
            for s in l:
                if isinstance(s, (list, set, tuple)):
                    unpack(s)
                else:
                    lst.append(s)
            return lst

        M = []
        for key in d.keys():
            lst = []
            if isinstance(d[key], (list, set, tuple)):
                for value in unpack(d[key]):
                    M.append([key, value])
            else:
                M.append([key, d[key]])
        N = []
        bank = set()
        for i in range(len(M)):
            index = 0
            ll = []
            for j in range(len(M) - 1, i - 1, -1):
                if M[i][1] == M[j][1] and i != j:
                    ll.append(M[j][0])
                    bank.add(M[j][1])
                    index += 1
                elif i == j and index > 0:
                    ll.append(M[j][0])
                    N.append([ll, M[i][1]])
                elif i == j and index == 0 and M[j][1] not in bank:
                    N.append([M[i][0], M[i][1]])
        P = {}
        for i in range(len(N)):
            P.setdefault(N[i][1], N[i][0])
        return P
    else:
        return source_dict
    raise NotImplementedError
