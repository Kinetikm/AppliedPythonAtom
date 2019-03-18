#!/usr/bin/env python
# coding: utf-8


def groupping_anagramms(words):
    for_anagramms = dict()
    for word in words:
        flag = False
        for key in for_anagramms.keys():
            if sorted(key.lower()) == sorted(word.lower()):
                for_anagramms[key].append(word)
                flag = True
                break
        if flag:
            continue
        for_anagramms[word] = [word]
    result = []
    for anagramms in for_anagramms.values():
        result.append(anagramms)
    return result
