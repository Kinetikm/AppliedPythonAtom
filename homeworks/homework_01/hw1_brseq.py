#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    stack = []
    print(input_string)
    for letter in input_string:
        if (letter == "("):
            stack.append("(")
        elif (letter == "["):
            stack.append("[")
        elif (letter == "{"):
            stack.append("{")
        else:
            try:
                if (letter == ")"):
                    if (stack.pop() != '('):
                        stack.append(")")
                elif (letter == "]"):
                    if (stack.pop() != "["):
                            stack.append("]")
                elif (letter == "}"):
                    if (stack.pop() != "{"):
                            stack.append("}")
                elif (letter == " "):
                    pass
            except:
                return (False)
    try:
        stack.pop()
        return (False)
    except:
        return (True)
