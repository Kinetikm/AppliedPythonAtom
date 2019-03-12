#!/usr/bin/env python
# coding: utf-8


def printLine(titles, distances, line):
    stringToPrint = "|"
    for title in titles:
        if "Оценка" not in title:
            stringToPrint = "".join([stringToPrint,
                                     " " * 2,
                                     str(line[title]),
                                     " " * (2 +
                                            distances[title] -
                                            len(str(line[title]))),
                                     "|"])
        else:
            stringToPrint = "".join([stringToPrint,
                                     " " * (2 +
                                            distances[title] -
                                            len(str(line[title]))),
                                     str(line[title]),
                                     " " * 2,
                                     "|"])
    print(stringToPrint)
