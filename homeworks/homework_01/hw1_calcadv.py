#!/usr/bin/env python
# coding: utf-8

ops = set("*/+-")
low_priority = set("+-")
high_priority = set("*/")
brackets = set("()")

def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    input_string = to_polish(input_string)
    parts = input_string.split(' ')
    stack = list()
    for part in parts:
        if not (part in ops):
            stack.append(float(part))
        elif len(stack)>1:
            b = stack.pop(-1)
            a = stack.pop(-1)
            if part=='+':
                stack.append(a+b)
            elif part=='-':
                stack.append(a-b)
            elif part=='*':
                stack.append(a*b)
            elif part=='/' and b!=0:
                stack.append(a/b)
            else:
                return None
    if len(stack)==1:
        return stack[0]
    else:
        return None

def to_polish(infix_string):
    parts = infix_string.split(' ')
    stack = list()
    res=''
    opstack = list()
    for part in parts:
        if not part in ops and not part in brackets:
            res+=part+' '
        elif part == '(':
            stack.append(part)
        elif (part==')'):
            lastPart=stack.pop()
            while lastPart!='(' and len(stack)>0:
                res+=lastPart+' '
                lastPart=stack.pop()
            if lastPart!='(':
                return None
        elif part in ops:
            while (part in low_priority) and len(stack)>0 and (stack[-1] in high_priority):
                res+=stack.pop()+" "
            stack.append(part)
    while len(stack)>0:
        lastPart=stack.pop()
        if lastPart!='(':
            res+=lastPart+" "
        else:
            return None
    return res.strip()