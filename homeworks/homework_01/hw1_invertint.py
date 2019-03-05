#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    s1 = str(number)
    s2 = s1[::-1]
    count = 0

    if number == 0:
        return 0
    if number < 0:
        return int("-" + s2[0:len(s2) - 1])
    elif s2[0] == "0":
        while s2[count] == "0":
            count += 1
        return int(s2[count:])
    else:
        return int(s2)
    raise NotImplementedError
