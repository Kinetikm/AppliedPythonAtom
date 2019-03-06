#!/usr/bin/env python
# coding: utf-8


def infix_to_postfix(infixexpr):
    for item in infixexpr:
        if item not in "0123456789+-*/(). \t":
            return None

    infixexpr = infixexpr.replace('+-', '-')
    infixexpr = infixexpr.replace('++', '+')
    infixexpr = infixexpr.replace('-+', '-')
    infixexpr = infixexpr.replace('--', '+')

    errors = ['**', '()']

    for item in errors:
        if item in infixexpr:
            return None

    infixexpr = infixexpr.replace('(', ' ( ')
    infixexpr = infixexpr.replace(')', ' ) ')
    infixexpr = infixexpr.replace('+', ' + ')
    infixexpr = infixexpr.replace('-', ' - ')
    infixexpr = infixexpr.replace('*', ' * ')
    infixexpr = infixexpr.replace('/', ' / ')

    precedency = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    op_stack = []
    postfix_list = []
    token_list = infixexpr.split()
    last_char = ''

    while len(token_list) != 0 and token_list[0] == '+':
        token_list.pop(0)

    for i in range(len(token_list)):
        if token_list[i] not in '+-*/() ':
            token_list[i] = float(token_list[i])

    for i in range(len(token_list) - 1):
        if token_list[i] == '-':
            if i > 0 and type(token_list[i-1]) == float and\
                    type(token_list[i+1]) == float:
                continue
            elif type(token_list[i+1]) == float:
                token_list[i+1] = -token_list[i+1]
                token_list[i] = ' '
            else:
                continue

    for i in range(len(token_list) - 1):
        if i > 0:
            if token_list[i-1] == '+' and token_list[i+1] == '+' \
                    and token_list[i] == '+':
                token_list[i - 1] = ' '
                token_list[i + 1] = ' '

    while ' ' in token_list:
        token_list.remove(' ')

    for token in token_list:
        if type(token) == float:
            if type(last_char) == float:
                return None
            postfix_list.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            try:
                top_token = op_stack.pop()
                while top_token != '(':
                    postfix_list.append(top_token)
                    top_token = op_stack.pop()
            except IndexError:
                return None
        else:
            while (not len(op_stack) == 0) and \
               (precedency[op_stack[-1]] >= precedency[token]):
                    postfix_list.append(op_stack.pop())
            op_stack.append(token)
        last_char = token

    while not len(op_stack) == 0:
        postfix_list.append(op_stack.pop())
    return postfix_list


def advanced_calculator(input_string):
    print(input_string)
    op_stack = infix_to_postfix(input_string)
    if op_stack is None:
        return None
    res_stack = []
    for token in op_stack:
        try:
            if token == '-':
                op1 = res_stack.pop()
                op2 = res_stack.pop()
                res_stack.append(float(op2) - float(op1))
            elif token == '+':
                op1 = res_stack.pop()
                op2 = res_stack.pop()
                res_stack.append(float(op1) + float(op2))
            elif token == '/':
                op1 = res_stack.pop()
                op2 = res_stack.pop()
                res_stack.append(float(op2) / float(op1))
            elif token == '*':
                op1 = res_stack.pop()
                op2 = res_stack.pop()
                res_stack.append(float(op1) * float(op2))
            else:
                res_stack.append(float(token))
        except IndexError:
            return None
        except ValueError:
            return None
    if len(res_stack) == 1:
        return res_stack[0]
    return None
