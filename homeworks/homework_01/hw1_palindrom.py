#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    back = input_string[::-1]
    if back == input_string:
        return True
    return False
    raise NotImplementedError
