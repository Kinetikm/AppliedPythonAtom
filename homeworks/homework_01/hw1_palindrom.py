#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    compare_string = input_string[::-1].lower()
    input_string = input_string.lower()
    input_string.replace(" ", "")
    compare_string.replace(" ", "")
    if input_string == compare_string:
        return True
    else:
        return False
