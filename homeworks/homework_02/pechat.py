#!/usr/bin/env python
# coding: utf-8


def print_file(text: list):
    if len(text) < 1:
        raise ValueError("Формат не валиден")
    for i in text:
        if len(i) != len(text[0]) or len(i) == 0:
            raise ValueError("Формат не валиден")
    lengths = []
    for i in range(len(text[0])):
        current_length = 0
        for st in text:
            current_length = max(len(str(st[i])), current_length)
        lengths.append(current_length)
    print("-" * (sum(lengths) + 5 * len(lengths) + 1))
    data_headers = text.pop(0)
    for i, j in enumerate(data_headers):
        print("|  {:^{width}}  ".format(j, width=lengths[i]), end='')
    print("|")
    for i in text:
        for j, k in enumerate(i):
            output = "|  {:" + (">" if j == len(i) - 1 else "<") + "{width}}  "
            print(output.format(k, width=lengths[j]), end='')
        print("|")
    print("-" * (sum(lengths) + 5 * len(lengths) + 1))
