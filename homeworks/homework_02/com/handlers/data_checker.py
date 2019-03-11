#!/usr/bin/env python
# coding: utf-8


def checkData(data):
    validKeys = sorted(["Название", "Ссылка", "Теги", "Оценка"])
    if len(data) == 0:
        raise SyntaxError
    for element in data:
        if sorted(element.keys()) != validKeys:
            raise SyntaxError
    return True
