#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
        try:
                x=float(x)
                y=float(y)
                if operator == 'plus':
                    return x+y
                if operator == 'minus':
                    return x-y
                if operator == 'mult':
                    return x*y
                if operator == 'divide':
                    return x/y
        except ZeroDivisionError:
            return None
        except TypeError:
            return None
        except ValueError:
            return None
