#!/usr/bin/env python
# coding: utf-8
import operator
import re


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    
    # К сожалению, это задание не все сам сделал, обратился за помощью к одногруппнику
    # Но, вроде, хорошо разобрался в коде
    def validity(expr):
         # В строке только операторы
        only_operators = re.compile(r'^(?:\s*[\*\+\-\/\(\)]\s*)+$')

        # Строка начинается с символов / или *
        startswith_mult_div = re.compile(r'\s*[\/\*].*')

        # В троке присутствуют невалидные символы
        unknown_symbols = re.compile(r'[^\s\d\+\-\*\/\(\)\.]')

        # Между числами отсутствует оператор
        absent_operator = re.compile(r'\d\s+\d')

        # Пустая пара скобок
        empty_brackets = re.compile(r'\(\s*\)')

        # Рядом стоящие операторы
        near_operands = re.compile(r'([\+\-\*\/]\s*[\/\*])|([\/\*]\s*[\*\/])')

        if (not expr or
            '\n' in expr or
            re.fullmatch(startswith_mult_div, expr) or
            re.fullmatch(only_operators, expr) or
            expr.count('(') != expr.count(')') or
            re.search(unknown_symbols, expr) or
            re.search(absent_operator, expr) or
            re.search(empty_brackets, expr) or
                re.search(near_operands, expr)):

            return False
        else:
            return True

    def correct_operands(expr):
        near_plus_minus = re.compile(r'([\+\-]\s*[\+\-])')
        while re.search(near_plus_minus, expr):

            while re.search(r'\+\s*\+', expr):
                expr = re.sub(r'\+\s*\+', '+', expr)

            while re.search(r'\-\s*\-', expr):
                expr = re.sub(r'\-\s*\-', '+', expr)

            while re.search(r'(\+\s*\-)|(\-\s*\+)', expr):
                expr = re.sub(r'(\+\s*\-)|(\-\s*\+)', '-', expr)

        # Убираем + в начале, если он есть
        if re.search(r'^\s*\+\s*', expr):
            expr = re.sub(r'^\s*\+\s*', '', expr)

        return expr

    def convert_to_polish(string):

        string = string.strip() + ' '
        OPERANDS = {'+': 0, '-': 0, '*': 1, '/': 1, '(': -1, ')': -1}
        res = ''
        stack = []
        i = 0
        after_mult_div = False
        if string[0] == '-':
            res += '-'
            string = string[1:]

        while i < len(string) - 1:
            if string[i] in '*/':
                j = i + 1
                while not (string[j].isdigit() or string[j] == '('):
                    if string[j] in [' ', '\t']:
                        j += 1
                    elif string[j] in '-+':
                        res += ' ' + string[j]
                        string = string[:j] + string[j + 1:]
                        after_mult_div = True

            if string[i] in [' ', '\t']:
                i += 1
                continue

            elif string[i].isdigit() or string[i] == '.':
                res += string[i]
                i += 1

            elif string[i] == '(':
                stack.append(string[i])
                i += 1

            elif string[i] == ')':
                try:
                    while stack[-1] != '(':
                        res += ' ' + stack.pop()
                except IndexError:
                    return None
                stack.pop()
                i += 1

            elif string[i] in OPERANDS:
                while stack and OPERANDS[stack[-1]] >= OPERANDS[string[i]]:
                    res += ' ' + stack.pop()

                stack.append(string[i])
                res += '' if after_mult_div else ' '
                after_mult_div = False
                i += 1

            else:
                return None

        while len(stack) > 0:
            if stack[-1] not in OPERANDS:
                return None
            else:
                res += ' ' + stack.pop()

        return res.strip()

    def calc(expr):
        if expr is None:
            return None
        OPERATORS = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv}
        stack = []
        for token in expr.split():
            if token in OPERATORS:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(OPERATORS[token](op1, op2))
            elif token:
                stack.append(float(token))
        return stack.pop() if len(stack) == 1 else None

    if validity(input_string):
        return calc(convert_to_polish(correct_operands(input_string)))
    else:
        return None
