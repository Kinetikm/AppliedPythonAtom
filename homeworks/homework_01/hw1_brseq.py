# !/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    result = True

    if input_string == '':
        return True
    if input_string[0] == ')' or input_string == ']' or input_string == '}' \
            or len(input_string) % 2 == 1:
        return False

    if input_string[len(input_string) - 1] == '(' or input_string[len(input_string) - 1] == '[' \
            or input_string[len(input_string) - 1] == '{':
        return False

    def one(st):
        kr = 1
        kv = 0
        fi = 0
        for symb in st:
            if symb == '[':
                kv += 1
            elif symb == '{':
                fi += 1
            elif symb == '(':
                kr += 1
            elif symb == ')':
                kr -= 1
            elif symb == ']':
                kv -= 1
            elif symb == '}':
                fi -= 1
            if kv < 0 or fi < 0:
                return False
            if kr == 0:
                return kv == 0 and fi == 0
        return kv == 0 and fi == 0 and kr == 0

    def two(st):
        kr = 0
        kv = 1
        fi = 0
        for symb in st:
            if symb == '[':
                kv += 1
            elif symb == '{':
                fi += 1
            elif symb == '(':
                kr += 1
            elif symb == ']':
                kv -= 1
            elif symb == ')':
                kr -= 1
            elif symb == '}':
                fi -= 1
            if kr < 0 or fi < 0:
                return False
            if kv == 0:
                return kr == 0 and fi == 0
        return kv == 0 and fi == 0 and kr == 0

    def three(st):
        kr = 0
        kv = 0
        fi = 1
        for symb in st:
            if symb == '[':
                kv += 1
            elif symb == '{':
                fi += 1
            elif symb == '(':
                kr += 1
            elif symb == ')':
                kr -= 1
            elif symb == ']':
                kv -= 1
            elif symb == '}':
                fi -= 1
            if kv < 0 or kr < 0:
                return False
            if fi == 0:
                return kr == 0 and fi == 0
        return kv == 0 and fi == 0 and kr == 0

    for i in range(len(input_string)):
        if input_string[i] == '(':
            result = one(input_string[i + 1:])
        elif input_string[i] == '[':
            result = two(input_string[i + 1:])
        elif input_string[i] == '{':
            result = three(input_string[i + 1:])
        if not result:
            return result
    return result
