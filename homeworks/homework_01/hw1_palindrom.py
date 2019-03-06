#!/usr/bin/env python
# coding: utf-8

# input_string = 'пkfЦёчгl гчёЦfkп'
def check_palindrom(input_string):
    '''
    Метод проверяющий строку на то, является ли
    она палиндромом.
    :param input_string: строка
    :return: True, если строка являестя палиндромом
    False иначе
    '''
    print(input_string)
    a = input_string
    a2 = ''
    # print(a1)
    for j in a:
        a2 = a2 + j
    s = ''
    # print('111', a2)
    for i in reversed(range(len(a2))):
        s += a2[i]
    print(a2, s)
    if a2 == s:
        return True
    else:
        return False

# print(check_palindrom(input_string))