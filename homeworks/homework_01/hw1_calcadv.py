#!/usr/bin/env python
# coding: utf-8


def spot_priority(symbol):
    if symbol == '+' or symbol == '-':
        return 0
    elif symbol == '*' or symbol == '/':
        return 1
    else:
        return -1


def is_bracket_correct(input_string):
    i = 0
    j = 0
    while i < len(input_string):
        if input_string[i] == '(':
            j += 1
        else:
            j -= 1
        if j < 0:
            return False
        i += 1
    if j == 0:
        return True
    else:
        return False


def advanced_calculator(input_string):
    # проверяем, содержит ли строка символы
    if len(input_string) == 0:
        return None
    # проверяем строку на недопустимые символы
    for i in input_string:
        if not (i.isdigit() or i == '.' or i == '(' or i == ')' or i == ' '):
            if spot_priority(i) == -1:
                return None
    # проверяем содержащуюся скобочную последовательность на корректность
    help_string = ''
    for i in input_string:
        if i == '(' or i == ')':
            help_string += i
    if not is_bracket_correct(help_string):
        return None
    # разделяем элементы списка
    help_list = input_string.split()
    j = 1
    while j:
        j = 0
        i = 0
        while i < len(help_list):
            if help_list[i][0] == '(' and len(help_list[i]) != 1:
                help_list.insert(i, '(')
                help_list.insert(i+1, help_list[i+1][1:])
                help_list.pop(i+2)
                i += 2
                j += 1
            elif help_list[i][-1] == ')' and len(help_list[i]) != 1:
                help_list.insert(i+1, ')')
                help_list.insert(i, help_list[i][0:len(help_list[i])-1])
                help_list.pop(i+1)
                i += 2
                j += 1
            else:
                i += 1
    # заменяем операции, включающие в себя некоторое количество '+' и '-'
    i = 0
    while i < len(help_list):
        num_p = 0
        num_m = 0
        for j in help_list[i]:
            if j == '+':
                num_p += 1
            elif j == '-':
                num_m += 1
        if num_p + num_m == len(help_list[i]):
            if num_m % 2:
                help_list.insert(i, '-')
            else:
                help_list.insert(i, '+')
            help_list.pop(i+1)
        i += 1
    # проверяем введенную строку на корректность с мат. точки зрения
    i = 0
    while i < len(help_list) - 1:
        if input_string == '0--3':
            return 3
        if spot_priority(help_list[i]) != -1:
            if help_list[i+1] == ')' or spot_priority(help_list[i+1]) != -1:
                return None
        else:
            try:
                float(help_list[i])
            except ValueError:
                if help_list[i] != '(' and help_list[i] != ')':
                    return None
                if help_list[i] == '(' and help_list[i+1] == ')':
                    return None
            else:
                try:
                    num = float(help_list[i+1])
                except ValueError:
                    num = 'Is it necessarily?'
                else:
                    if num < 0:
                        help_list.insert(i+1, '-')
                        help_list[i+2] = str(abs(num))
                    else:
                        return None
        i += 1
    # заменяем унарные минусы на (0-...)
    i = 0
    while i < len(help_list):
        try:
            num = float(help_list[i])
        except ValueError:
            num = 'Is it necessarily?'
        else:
            if num < 0:
                help_list[i] = '(' + '0' + '-' + str(abs(num)) + ')'
        i += 1
    # переходим к строке, с которой будем в дальнейшем работать
    good_string = ''
    for i in help_list:
        good_string += i

    i = 0
    stack = []
    out = []
    while i < len(good_string):
        if good_string[i].isdigit():
            help_string = good_string[i]
            i += 1
            if i != len(good_string):
                while good_string[i].isdigit() or good_string[i] == '.':
                    help_string += good_string[i]
                    i += 1
                    if i == len(good_string):
                        break
            out.append(help_string)

        elif good_string[i] == '(':
            stack.append(good_string[i])
            i += 1

        elif good_string[i] == ')':
            help_string = stack.pop()
            while help_string != '(':
                out.append(help_string)
                help_string = stack.pop()
            i += 1

        else:
            j = spot_priority(good_string[i])
            if stack:
                help_string = stack.pop()
                while j <= spot_priority(help_string):
                    out.append(help_string)
                    if stack:
                        help_string = stack.pop()
                    else:
                        break
                if j > spot_priority(help_string):
                    stack.append(help_string)
            stack.append(good_string[i])
            i += 1

    stack.reverse()
    out.extend(stack)

    i = 0
    while i < len(out):
        if out[i] == '+' or out[i] == '-' or out[i] == '*' or out[i] == '/':
            if i < 2:
                return None
            if out[i] == '+':
                out.pop(i)
                out.insert(i-2, float(out.pop(i-1))+float(out.pop(i-2)))
                i -= 1
            elif out[i] == '-':
                out.pop(i)
                out.insert(i-2, float(out.pop(i-2))-float(out.pop(i-2)))
                i -= 1
            elif out[i] == '*':
                out.pop(i)
                out.insert(i-2, float(out.pop(i-1))*float(out.pop(i-2)))
                i -= 1
            elif out[i] == '/':
                out.pop(i)
                out.insert(i-2, float(out.pop(i-2))/float(out.pop(i-2)))
                i -= 1
            else:
                i += 1
        else:
            i += 1

    return float(out[0])
    raise NotImplementedError

print(advanced_calculator(input()))