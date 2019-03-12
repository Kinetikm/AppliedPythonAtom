#!/usr/bin/env python
# coding: utf-8


def checkData(titles, data):
    validKeys = sorted(titles)
    for element in data:
        if sorted(element.keys()) != validKeys:
            raise SyntaxError
    return True
