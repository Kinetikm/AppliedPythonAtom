#!/usr/bin/env python
# coding: utf-8


def is_left_br(st, index):
    return (st[index] == "{") or (st[index] == "(") or (st[index] == "[")


def is_right_br(st, index):
    return (st[index] == "}") or (st[index] == ")") or (st[index] == "]")


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    index = 0
    st = input_string
    if st is "":
        return True
    else:
        if is_right_br(st, 0):
            return False
        else:
            while (index < len(st)) and (is_left_br(st, index)):
                index = index + 1
            if index != len(st):
                s = st[index-1] + st[index]
                if s == "[]" or s == "{}" or s == "()":
                    if index == (len(st)-1):
                        new_string = st[:index-1]
                    else:
                        new_string = st[:index-1] + st[index+1:]
                    return is_bracket_correct(new_string)
                else:
                    return False
            else:
                return False
    raise NotImplementedError
