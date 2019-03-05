#!/usr/bin/env python
# coding: utf-8


def Polin(string):
    if type(string)==str:
        strBuf = string[::-1]
        if strBuf == string:
            return True
    return False
