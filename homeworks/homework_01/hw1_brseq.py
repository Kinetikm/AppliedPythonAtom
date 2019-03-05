#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    a = []
    if type(input_string) == str:
        for i in range(len(input_string)):
            if input_string[i] == "{" or input_string[i] == "[" or \
                    input_string[i] == "(":
                a.append(input_string[i])
            else:
                print(len(a))
                if len(a) == 0:
                    return False
                if a[len(a)-1] == "[":
                    if input_string[i] == "]":
                        del a[len(a)-1]
                    else:
                        return False
                elif a[len(a)-1] == "(":
                    if input_string[i] == ")":
                        del a[len(a)-1]
                    else:
                        return False
                elif a[len(a)-1] == "{":
                    if input_string[i] == "}":
                        del a[len(a)-1]
                    else:
                        return False
        if len(a) == 0:
            return True
