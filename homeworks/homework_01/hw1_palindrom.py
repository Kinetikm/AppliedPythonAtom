#!/usr/bin/env python
# coding: utf-8

def check_palindrom(input_string):
    input_string = input_string.lower()
    if input_string != input_string[::-1]:
        return False
    else:
        return True