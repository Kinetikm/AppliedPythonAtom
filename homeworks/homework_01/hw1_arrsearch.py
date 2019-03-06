#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    MyDict = {}
    for j in range(len(input_list)):
        k = input_list[j]
        if MyDict.get(n-input_list[j]):
            return [MyDict.get(n-input_list[j]), j]
        if k not in MyDict:
            MyDict.update({k: j})
    return None
