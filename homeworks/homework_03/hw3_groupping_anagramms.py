#!/usr/bin/env python
# coding: utf-8


def groupping_anagramms(words):
    res_dict = dict()

    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if res_dict.get(sorted_word) is None:
            res_dict[sorted_word] = [word]
        else:
            res_dict[sorted_word].append(word)

    return list(res_dict.values())

