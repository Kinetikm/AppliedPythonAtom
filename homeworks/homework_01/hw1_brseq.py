#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    a=[]
    if type(input_string)==str:
        for i in range(len(input_string)):
            if string[i] == "{" or input_string[i] == "[" or input_string[i] == "(":
                a.append(string[i])
            else:
                if len(a) == 0 and i != len(string)-1:
                    return None
                if a[-1] == "[":
                    if input_string[i] == "]":
                        del a[-1]
                    else:
                        return None
                elif a[-1] == "(":
                    if input_string[i] == ")":
                        del a[-1]
                    else:
                        return None
                elif a[-1] == "{":
                    if input_string[i] == "}":
                        del a[-1]
                    else:
                        return None
        if len(a) == 0:
            return True
