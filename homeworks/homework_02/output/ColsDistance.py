#!/usr/bin/env python
# coding: utf-8


def colsDistance(titles, data):
    distances = {}
    for title in titles:
        distances[title] = len(title)
    for line in data:
        for title in titles:
            if len(str(line[title])) > distances[title]:
                distances[title] = len(line[title])
    return distances
