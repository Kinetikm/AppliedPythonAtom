#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string: str):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
#    if not isinstance(input_string, str):
#        raise TypeError("")
    string_list = list(input_string)
    print(string_list)
    openList = ["[", "{", "("]
    closeList = ["]", "}", ")"]

    stack = []
    for i in string_list:
        if i in openList:
            stack.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
