#!/usr/bin/env python
# coding: utf-8

import com.handler.treeset
from collections import OrderedDict
import operator


def reverse_dict_to_ordered(inputDict: dict):
    inversedDict = dict()
    for pair in inputDict.items():
        if pair[1] not in inversedDict:
            inversedDict[pair[1]] = treeset()
        inversedDict[pair[1]].insert(pair[0])
    resultDict = OrderedDict(sorted(inversedDict.items(), key=operator.itemgetter(0)))
    return resultDict