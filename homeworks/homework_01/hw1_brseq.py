#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    br1 = '([{'
    br2 = ')]}'
    pairs = []
    for symbol in input_string:
        if symbol in br1:
            pairs.append(br1.index(symbol))
        elif symbol in br2:
            if pairs and pairs[-1] == br2.index(symbol):
                pairs.pop()
            else:
                return False
    return not pairs
