#!/usr/bin/env python
# coding: utf-8

from com.handler import treeset
from collections import OrderedDict
import operator


def reverse_dict_to_ordered(inputDict: dict) -> OrderedDict:
    inversedDict = dict()
    for pair in inputDict.items():
        if pair[1] not in inversedDict:
            inversedDict[pair[1]] = treeset.TreeSet()
        inversedDict[pair[1]].add(pair[0])
    resultDict = OrderedDict(sorted(inversedDict.items(), key=operator.itemgetter(0)))
    return resultDict
