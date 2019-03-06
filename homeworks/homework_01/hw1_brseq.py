#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    b = input_string
    skobki = {'[': ']', '{': '}', '(': ')'}
    q = []
    for j in b:
        q.append(j)

    l = []
    r = []
    val = True
    for i in range(len(q)):
        if q[0] not in skobki.keys():
            val = False
            # print(1)
            break
        if q[i] in skobki.keys():
            l.append(q[i])
        else:
            r.append(q[i])
        # print(l, r)
        if len(r) != 0:
            if len(l) == 0:
                val = False
            else:
                if skobki.get(l[-1]) == r[0]:
                    l.pop()
                    r.pop()
                if len(r) != 0:
                    break

    if val is True and len(l) == 0 and len(r) == 0:
        return True
    else:
        return False
