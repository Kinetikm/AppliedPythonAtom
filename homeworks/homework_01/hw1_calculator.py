﻿#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if y == 0 and operator == "divide":
        return None
    if operator == "divide":
        return x / y
    if operator == "mult":
        return x * y
    if operator == "plus":
        return x + y
    if operator == "minus":
        return x - y
    return None
