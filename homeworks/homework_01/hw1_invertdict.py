#!/usr/bin/env python
# coding: utf-8


def getvalues(v):
    res = []
    if type(v) in [list, tuple, set]:
        for i in v:
            if type(v) in [list, tuple, set]:
                for j in getvalues(i):
                    res.append(j)
            else:
                res.append(i)
    else:
        res = [v]
    return res
    
def invert_dict(source_dict):
    res = {}
    if ( type(source_dict) is not dict ):
        return res
    for k, v in source_dict.items():
        values = getvalues(v)
        for v in values :
            if v in res:
                if ( type (res[v]) is not list ):
                    x = res[v]
                    res[v] = [x]
                    res[v].append(k)
                else:
                    res[v].append(k)
            else:
                res[v] = k
    return res
