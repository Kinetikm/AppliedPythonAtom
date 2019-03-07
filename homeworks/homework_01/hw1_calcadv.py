#!/usr/bin/env python
# coding: utf-8

import re


def advanced_calculator(input_string):
    try:
        s = re.findall("[0-9]", input_string)
        if len(s) == 0 or "**" in input_string:
            return None

        for ss in input_string:
            if "," in ss or "[" in ss or "]" in ss or ss.isalpha():
                return None
        return eval(input_string)
    except (SyntaxError, TypeError):
        return None

    raise NotImplementedError
