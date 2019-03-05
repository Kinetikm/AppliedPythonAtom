#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    br_list = list()
    for i in input_string:
        if i == '(' or i == '[' or i == '{':
            br_list.append(i)
        if i == ')':
            if len(br_list) != 0:
                if br_list[len(br_list) - 1] == '(':
                    br_list.pop()
                else:
                    return False
            else:
                return False
        if i == ']':
            if len(br_list) != 0:
                if br_list[len(br_list) - 1] == '[':
                    br_list.pop()
                else:
                    return False
            else:
                return False
        if i == '}':
            if len(br_list) != 0:
                if br_list[len(br_list) - 1] == '{':
                    br_list.pop()
                else:
                    return False
            else:
                return False
    if len(br_list) == 0:
        return True
    else:
        return False

    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
