#!/usr/bin/env python
# coding: utf-8

high = ['(', '*', '/', ')']
low = ['+', '-']
check = [')', '+', '-', '*', '/', '']


def advanced_calculator(input_string):
    '''
    if input_string in check or input_string.isalpha():
        return None
    if input_string[0] in check:
        return int(input_string.replace(input_string[0], ''))
    if input_string.isdigit():
        return int(input_string)
    if len(input_string) < 3:
        return None
    for el in high:
        if el in input_string:
            input_string = input_string.replace(el, ' ' + el + ' ')
    for el in low:
        if el in input_string:
            input_string = input_string.replace(el, ' ' + el + ' ')
    input_string = input_string.replace('  ', ' ')
    input_string = input_string.strip()
    input_list = input_string.split(' ')
    result = []
    operation = []
    for i in range(len(input_list)):
        if input_list[i] in high:
            if input_list[i] != ')':
                operation.append(input_list[i])
            else:
                n = len(operation) - 1
                while operation[n] != '(':
                    result.append(operation.pop())
                    n -= 1
                operation.pop()
        elif input_list[i] in low:
            if len(operation) != 0:
                if operation[len(operation) - 1] in low:
                    result.append(operation.pop())
                    operation.append(input_list[i])
                    continue
                elif operation[len(operation) - 1] in high\
                 and operation[len(operation) - 1] != '(':
                    result.append(operation.pop(len(operation) - 1))
                operation.append(input_list[i])
            else:
                operation.append(input_list[i])
        elif input_list[i].isdigit():
            if input_list[i].find('.') != (-1):
                result.append(float(input_list[i]))
            else:
                result.append(int(input_list[i]))
        else:
            return None
    result.append(operation.pop())
    i = 2
    while i < len(result):
        if result[i] == '+':
            result[i] = result[i - 1] + result[i - 2]
            result.pop(i - 1)
            result.pop(i - 2)
            i -= 2
        elif result[i] == '-':
            result[i] = result[i - 2] - result[i - 1]
            result.pop(i - 1)
            result.pop(i - 2)
            i -= 2
        elif result[i] == '*':
            result[i] = result[i - 1] * result[i - 2]
            result.pop(i - 1)
            result.pop(i - 2)
            i -= 2
        elif result[i] == '/':
            if result[i - 2] != 0:
                result[i] = result[i - 2] / result[i - 1]
                result.pop(i - 1)
                result.pop(i - 2)
                i -= 2
            else:
                return None
        i += 1
    return result[i - 1]
print(advanced_calculator('*+4'))'''
    raise NotImplementedError
