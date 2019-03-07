#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    newdict={v:[i for i in source_dict.keys() if v in source_dict[i]] for k,v in source_dict.items() for v in v}
    #print(newdict)
    return newdict