#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(text):
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')
    return not text
    raise NotImplementedError
