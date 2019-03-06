#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    len1 = len(input_string)
    right = True
    for i in range(0, len1 // 2):
        if input_string[i] != input_string[len1 - i - 1]:
            right = False
            break
    return right
