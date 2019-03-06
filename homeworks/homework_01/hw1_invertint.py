#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    number = int(number)
    if number < 0:
        number = abs(number)
        neg_option = True
    else:
        neg_option = False
    reversed_number = 0
    while number > 0:
        reminder = number % 10
        reversed_number = (reversed_number * 10) + reminder
        number = number // 10
    if neg_option is True:
        reversed_number = -reversed_number
    return reversed_number


# print(reverse(input('Input int number: ')))
