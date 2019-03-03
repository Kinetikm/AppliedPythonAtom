#!/usr/bin/env python
# coding: utf-8

input_string1 = input()


def check_palindrom(input_string):
    if input_string[::-1] == input_string:
        return True
    else:
        return False


print(check_palindrom(input_string1))

#    '''
#    Метод проверяющий строку на то, является ли
#    она палиндромом.
#    :param input_string: строка
#    :return: True, если строка являестя палиндромом
#    False иначе
#    '''
