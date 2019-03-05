#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    s = input_string
    if len(s) % 2 == 0:
        for i in range(len(s) // 2):
            s1 = s.replace("()", "")
            s2 = s1.replace("[]", "")
            s = s2.replace("{}", "")
        if s == "":
            return True
        else:
            return False
    else:
        return False

    raise NotImplementedError
