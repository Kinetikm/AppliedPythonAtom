#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json


def r_json(filename, encoding):
    data = []
    with open(filename, encoding=encoding) as file:
        try:
            blank = json.load(file)
            data.append(list(blank[0].keys()))
            for x in blank:
                if list(x.keys()) != blank[0]:
                    raise KeyError
                data.append(list(x.values()))
        except json.JSONDecodeError:
            raise ValueError
    return data
