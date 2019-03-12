#!/usr/bin/env python
# coding: utf-8

from com.output.cols_distance import colsDistance
from com.output.line_printer import printLine
import sys


def createTable(data, titles):
    distances = colsDistance(titles, data)
    tableLen = len(distances) + 1
    for singleDist in distances.values():
        tableLen += singleDist + 4
    titleString = "|"
    for title in titles:
        titleString = "".join([titleString,
                               " " * (2 +
                                      (distances[title] - len(title) + 1) //
                                      2),
                               title,
                               " " * (2 +
                                      (distances[title] - len(title)) //
                                      2),
                               "|"])
    print('-' * tableLen, file=sys.stderr)
    print('-' * tableLen)
    print(titleString, file=sys.stderr)
    print(titleString)
    for line in data:
        printLine(titles, distances, line)
    print('-' * tableLen, file=sys.stderr)
    print('-' * tableLen)
