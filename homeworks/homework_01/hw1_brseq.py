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

    a =list()
    open_brackets=set('([{')
    for ch in input_string:
        if(ch in open_brackets):
            a.append(ch)
        elif len(a)>0 and (ch == ']' and a[-1]=='[' or ch == ')' and a[-1]=='(' or ch == '}' and a[-1]=='{'):
            a.pop(-1);
        else:
            return False
    return True