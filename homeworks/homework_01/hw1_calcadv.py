#!/usr/bin/env python
# coding: utf-8

from enum import Enum
from collections import deque


class Token(Enum):
    NUMBER = 1
    CONCAT = 2
    SUBTRACT = 3
    MULTIPLY = 4
    DIVISION = 5
    PAREN_LEFT = 6
    PAREN_RIGHT = 7
    SPACE = 8


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    input_string = input_string.rstrip(' \t\n\r\v\f')
    revPolandNotation = deque()
    operationsStack = []
    operations = {
        ')': Token.PAREN_RIGHT,
        '(': Token.PAREN_LEFT,
        '*': Token.MULTIPLY,
        '+': Token.CONCAT,
        '-': Token.SUBTRACT,
        '/': Token.DIVISION,
        ' ': Token.SPACE
    }
    priority = {
        Token.CONCAT: 2,
        Token.SUBTRACT: 2,
        Token.MULTIPLY: 3,
        Token.DIVISION: 3,
        Token.PAREN_LEFT: 1,
        Token.PAREN_RIGHT: 4
    }
    number = ""
    currToken = Token.SPACE
    lastElement = Token.SPACE
    try:
        for chr in input_string:
            if chr not in operations.keys() and \
                    not chr.isdigit() and \
                    not chr == '.':
                return None
            if chr.isdigit() or chr == '.':
                if lastElement == Token.PAREN_RIGHT:
                    operationsStack.append(Token.MULTIPLY)
                number += chr
                currToken = Token.NUMBER
            else:
                if currToken == Token.NUMBER:
                    revPolandNotation.append(float(number))
                    number = ""
                if operations[chr] == Token.PAREN_LEFT and \
                   lastElement == Token.PAREN_RIGHT:
                    operationsStack.append(Token.MULTIPLY)
                if currToken != Token.SPACE:
                    lastElement = currToken
                currToken = operations[chr]
                if currToken == Token.SPACE:
                    continue
                if currToken != Token.PAREN_LEFT and \
                   currToken != Token.PAREN_RIGHT:
                    if (currToken == Token.CONCAT or
                        currToken == Token.SUBTRACT) and \
                            lastElement == Token.SPACE:
                        revPolandNotation.append(0)
                    elif (currToken == Token.CONCAT or
                            currToken == Token.SUBTRACT) and \
                            lastElement in {Token.CONCAT, Token.SUBTRACT}:
                        if currToken == Token.SUBTRACT:
                            operation = Token.CONCAT \
                                if (operationsStack.pop() == Token.SUBTRACT) \
                                else Token.SUBTRACT
                            operationsStack.append(operation)
                        continue
                    elif (currToken == Token.CONCAT or
                            currToken == Token.SUBTRACT) and \
                            lastElement not in \
                            {Token.PAREN_RIGHT, Token.NUMBER}:
                        number += chr
                        currToken = Token.NUMBER
                        continue
                    if not operationsStack or \
                       priority[operationsStack[-1]] < priority[currToken]:
                        operationsStack.append(currToken)
                    else:
                        while operationsStack and \
                              priority[operationsStack[-1]] >= \
                              priority[currToken]:
                            revPolandNotation.append(operationsStack.pop())
                        operationsStack.append(currToken)
                elif currToken == Token.PAREN_LEFT:
                    operationsStack.append(currToken)
                else:  # currToken == Token.PAREN_RIGHT
                    leftParenFinded = False
                    while not leftParenFinded and operationsStack:
                        poppedToken = operationsStack.pop()
                        if poppedToken != Token.PAREN_LEFT:
                            revPolandNotation.append(poppedToken)
                        else:
                            leftParenFinded = True
                    if not leftParenFinded:
                        return None
                lastElement = currToken
        if currToken == Token.NUMBER:
            revPolandNotation.append(float(number))
        while operationsStack:
            poppedToken = operationsStack.pop()
            if poppedToken != Token.PAREN_LEFT:
                revPolandNotation.append(poppedToken)
            else:
                return None
        # Calculate revPolandNotation
        numbersStack = []
        while revPolandNotation:
            poppedToken = revPolandNotation.popleft()
            if poppedToken not in operations.values():
                numbersStack.append(poppedToken)
            else:
                num1 = numbersStack.pop()
                num2 = numbersStack.pop()
                res = 0
                if poppedToken == Token.CONCAT:
                    res = num1 + num2
                if poppedToken == Token.SUBTRACT:
                    res = num2 - num1
                if poppedToken == Token.MULTIPLY:
                    res = num1 * num2
                if poppedToken == Token.DIVISION:
                    res = num2 / num1
                numbersStack.append(res)
        if len(numbersStack) == 1:
            return numbersStack.pop()
        else:
            return None
    except:
        return None
