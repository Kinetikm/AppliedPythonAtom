#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict,NewDict=None):
    if source_dict == "":
        return {}
    BufDict = {}
    ForBuf = list()
    if NewDict is None:
        NewDict = {}
    for key, value in source_dict.items():
        if type(value) != int and type(value) != float and type(value) != str and (value!=Ellipsis):
            for iter in value:
                BufDict.update({key: iter})
                NewDict = invert_dict({key: iter}, NewDict)
        else:
            if  value not in NewDict:
                NewDict.update({value: key})
            else:
                if type(NewDict[value]) == list:
                    NewDict[value].append(key)
                else:
                    ForBuf = list()
                    BUFFER = NewDict[value]
                    ForBuf.append(BUFFER)
                    ForBuf.append(key)
                    NewDict.update({value: ForBuf})
    return NewDict
