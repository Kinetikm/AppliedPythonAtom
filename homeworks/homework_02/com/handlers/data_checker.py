#!/usr/bin/env python
# coding: utf-8


def checkData(data):
    validKeys = sorted(["Название", "Ссылка", "Теги", "Оценка"])
    for element in data:
        if sorted(element.keys()) != validKeys:
            raise SyntaxError
    return True
