#!/usr/bin/env python
# coding: utf-8


def spot_priority(symbol):
    if symbol == '+' or symbol == '-':
        return 0
    elif symbol == '*' or symbol == '/':
        return 1
    else:
        return -1


def advanced_calculator(input_string):
    if len(input_string) == 0:
        return None
    i = 0
    minus = 0
    stack = []
    out = []
    while i < len(input_string):
        if input_string[i].isdigit():
            Help = input_string[i]
            i += 1
            if i != len(input_string):
                while input_string[i].isdigit() or input_string[i] == '.':
                    Help += input_string[i]
                    i += 1
                    if i == len(input_string):
                        break
            if minus:
                out.append('-'+Help)
                minus = 0
            else:
                out.append(Help)

        elif input_string[i] == '(':
            stack.append(input_string[i])
            i += 1

        elif input_string[i] == ')':
            Help = stack.pop()
            while Help != '(':
                out.append(Help)
                Help = stack.pop()
            i += 1

        else:
            j = spot_priority(input_string[i])
            if j != -1:
                if input_string[i] == '-' and (i == 0 or input_string[i-1] == '('):
                    if input_string[i+1] == '(':
                        out.append('0')
                        stack.append('-')
                    else:
                        minus = 1
                else:
                    if stack:
                        Help = stack.pop()
                        while  j <= spot_priority(Help):
                            out.append(Help)
                            if stack:
                                Help = stack.pop()
                            else:
                                break
                        if j > spot_priority(Help):
                            stack.append(Help)
                    stack.append(input_string[i])
            else:
                return None
            i += 1

    stack.reverse()
    out.extend(stack)

    i = 0
    while i < len(out):
        if out[i] == '+':
            out.pop(i)
            out.insert(i-2, float(out.pop(i-1))+float(out.pop(i-2)))
            i -= 1
        elif out[i] == '-':
            out.pop(i)
            out.insert(i-2, float(out.pop(i-2))-float(out.pop(i-2)))
            i -= 1
        elif out[i] == '*':
            out.pop(i)
            out.insert(i-2, float(out.pop(i-1))*float(out.pop(i-2)))
            i -= 1
        elif out[i] == '/':
            out.pop(i)
            out.insert(i-2, float(out.pop(i-2))/float(out.pop(i-2)))
            i -= 1
        elif out[i] == '^':
            out.pop(i)
            out.insert(i-2, float(out.pop(i-2))**float(out.pop(i-2)))
            i -= 1
        else:
            i += 1

    return float(out[0])     
    raise NotImplementedError
