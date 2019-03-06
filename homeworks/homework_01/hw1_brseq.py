#!/usr/bin/env python
# coding: utf-8

# input_string = '[]}{)]{}{)(]{(]{[([]{{})}}))(([])([])[(}}['

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

    L = []
    R = []
    val = True
    for i in range(len(q)):
        if q[0] not in skobki.keys():
            val = False
            # print(1)
            break
        if q[i] in skobki.keys():
            L.append(q[i])
        else:
            R.append(q[i])
        # print(L, R)
        if len(R) != 0:
            if len(L) == 0:
                val = False
            else:
                if skobki.get(L[-1]) == R[0]:
                    L.pop()
                    R.pop()
                if len(R) != 0:
                    break

    if val is True and len(L) == 0 and len(R) == 0:
        return True
    else:
        return False
    # raise NotImplementedError

# print(is_bracket_correct(input_string))