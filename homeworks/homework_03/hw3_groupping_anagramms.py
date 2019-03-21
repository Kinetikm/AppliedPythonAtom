#!/usr/bin/env python
# coding: utf-8


def groupping_anagramms(words):
    dict = {}
    for i in words:
        x = ''.join(sorted(i.lower()))
        if x in dict.keys():
            dict[x].append(i)
        else:
            dict[x] = [i]
    return list(dict.values())