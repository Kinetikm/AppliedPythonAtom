#!/usr/bin/env python
# coding: utf-8


def convertToJSON(data):
    jsonData = []
    numberToKey = {}
    if len(data) > 0:
        i = 0
        for title in data[0]:
            numberToKey[i] = title
            i += 1
    else:
        raise SyntaxError
    isTitleString = True
    for line in data:
        if isTitleString:
            isTitleString = False
            continue
        if len(line) != len(numberToKey):
            raise SyntaxError
        oneLineData = {}
        i = 0
        for value in line:
            oneLineData[numberToKey[i]] = value
            i += 1
        jsonData.append(oneLineData)
    return jsonData
