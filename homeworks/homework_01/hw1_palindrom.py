#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    if type(input_string)==str:
        strBuf = input_string[::-1]
        if strBuf == input_string:
            return True
    return False
