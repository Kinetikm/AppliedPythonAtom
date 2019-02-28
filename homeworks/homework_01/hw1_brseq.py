#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    """
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    """
    counters = {'(': 0, '[': 0, '{': 0}
    open_brackets = list(counters.keys())
    close_brackets = [')', ']', '}']
    brackets_cl_op = {')': '(', ']': '[', '}': '{'}
    brackets_list = open_brackets + close_brackets
    brackets_mapping = {
        '(': open_brackets + [')'],
        '[': open_brackets + [']'],
        '{': open_brackets + ['}'],
    }

    brackets = []
    for bracket in input_string:
        if bracket in brackets_list:  # скобка допустима
            if bracket in open_brackets:  # скобка открывающая
                brackets.append(bracket)
                counters[bracket] += 1
            else:  # скобка закрывающая
                if not brackets:
                    # если первой идёт закрывающаяся скобка
                    return False
                if bracket not in brackets_mapping[brackets[-1]]:
                    # скобка не может следовать после последней открывающейся
                    return False
                brackets.pop(-1)
                counters[brackets_cl_op[bracket]] -= 1
        else:  # не входит в список допустимых скобок
            return False

    return not bool(sum(counters.values()))


def is_bracket_correct_internet(input_string):
    """
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    """
    while '()' in input_string or '[]' in input_string or '{}' in input_string:
        input_string = input_string.replace('()', '')
        input_string = input_string.replace('[]', '')
        input_string = input_string.replace('{}', '')

    # Возвращаем True, если input_string с пустой строкой
    return not input_string
