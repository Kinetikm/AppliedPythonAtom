#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    a = ("[", "(", "{")
    b = ("]", ")", "}")
    last = [0]
    for i in input_string:
        head = last[len(last) - 1]
        if i in a:
            head = a.index(i)
            last.append(head)
        elif i in b:
            if input_string.index(i) == 0:
                return False
            if head != b.index(i):
                return False
            last.pop()
            continue
    if len(last) != 1:
        return False
    return True
    raise NotImplementedError
