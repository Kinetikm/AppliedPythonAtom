#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def make_table(data):

    columns = len(data[0])
    count_spaces = []
    for col in range(columns):
        spaces = 0
        for row in data:
            spaces = max(spaces, len(str(row[col])))
        count_spaces.append(spaces)
    for row in data:
        for x, y in enumerate(row):
            try:
                count_spaces[x]
            except Exception:
                raise Exception
    print("-" * (5 * columns + sum(count_spaces) + 1))
    column_names = data.pop(0)
    for x, y in enumerate(column_names):
        print("|  {:^{width}}  ".format(y, width=count_spaces[x]), end='')
    print("|")
    for row in data:
        for x, y in enumerate(row):
            if x != len(row) - 1:
                s = "|  {:<{width}}  "
            else:
                s = "|  {:>{width}}  "
            print(s.format(y, width=count_spaces[x]), end='')
        print("|")
    print("-" * (5 * columns + sum(count_spaces) + 1))
