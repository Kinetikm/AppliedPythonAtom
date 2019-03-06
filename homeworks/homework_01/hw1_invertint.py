#!/usr/bin/env python
# coding: utf-8
import math


def reverse(number):
    if number == 0:
        return 0
    num_1 = int(number)

    if (num_1 < 0):
        minus = True
    else:
        minus = False

    unsign_num = int(math.fabs(num_1))

    strNum = str(unsign_num)

    str1 = strNum.strip('0')

    str2 = str1[::-1]
    if minus:
        str3 = "-" + str2
        str4 = int(str3)
    else:
        str4 = int(str2)
    return str4
