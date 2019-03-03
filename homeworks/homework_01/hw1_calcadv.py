#!/usr/bin/env python
# coding: utf-8

import pickle
import copy
from pythonds.basic.stack import Stack
import re

def stack_print(source_stack):
    copy_stack = copy.deepcopy(source_stack)
    while True:
        try:
            print(copy_stack.pop(), " ")
        except IndexError:
            print("**")
            return

# def add_close_bracket(postfix_expr):


# def infixToPostfix(infixexpr):
#     prec = {}
#     prec["*"] = 3
#     prec["/"] = 3
#     prec["+"] = 2
#     prec["-"] = 2
#     prec["("] = 1
#     opStack = Stack()
#     postfixList = []
#     #tokenList = infixexpr.split()
#
#     for token in infixexpr.split():
#         # print("token = ", token)
#         # print("opstack:")
#         # stack_print(opStack)
#         #print("postfix: ", postfixList)
#         #print("***")
#         # stack_print(opStack)
#         res = re.match('[0-9]+', token)
#         #print("group:", res.group(0))
#         if not (res is None):
#             postfixList.append(token)
#             continue
#         res_unary = re.match('-+[0-9]+', token)
#         if not (res_unary is None):
#
#             for char in token:
#                 if char != '-':
#                    break
#                 cnt += 1
#             print(float(token[cnt:]))
#             if cnt % 2 == 0:
#                 postfixList.append(float(token[cnt:]))
#             else:
#                 postfixList.append(-float(token[cnt:]))
#             continue
#         res_open = re.match('\(+[0-9]+', token)
#         if not (res_open is None):
#             cnt = 0
#             for char in token:
#                 if char != '(':
#                    break
#                 cnt += 1
#                 opStack.push('(')
#             postfixList.append(float(token[cnt:]))
#         res_close = re.match('[0-9]+\)+', token)
#         if not (res_close is None):
#             cnt = 0
#             for char in token:
#                 if char == ')':
#                     cnt += 1
#                 opStack.push('(')
#             postfixList.append(float(token[cnt:]))
#         if token == '(':
#             opStack.push(token)
#
#         elif token == ')':
#             topToken = opStack.pop()
#             while topToken != '(':
#                 postfixList.append(topToken)
#                 topToken = opStack.pop()
#         else:
#             if prec.get(token) is None:
#                 return None
#             while (not opStack.isEmpty()) and \
#                (prec[opStack.peek()] >= prec[token]):
#                   postfixList.append(opStack.pop())
#             opStack.push(token)
#     while not opStack.isEmpty():
#         postfixList.append(opStack.pop())
#
#     #print("in the end: ",postfixList)
#     # for i in range(postfixList):
#     #     try:
#     #         if postfixList[i] == ' ':
#     #             postfixList.pop(i)
#     #         if not (prec.get(postfixList[i]) is None):
#     #             continue
#     #         postfixList[i] = float(postfixList[i])
#     #     except ValueError:
#     #         return None
#     return postfixList

#print(infixToPostfix("A * B + C * D"))
#print(infixToPostfix("89+23"))
#print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
# advanced_calculator("")



# def run_tests():
#     with open("../../tests/tests_data/test_hw_01_calcadv.ini.pkl", "rb") as f:
#         data = pickle.load(f)
#     for item in data:
#         if item[1] == calculate(item[0]):
#             print("yes")
#         else:
#             print("fail")
#             print(item[0])
#             print("expected: ", item[1], "result: ", calculate(item[0]))
#         print("******************")
#
#     return


def add_right_bracket(expr, op_stack, num):
    try:
        for _ in range(num):
            top_token = op_stack.pop()
            while top_token != '(':
                expr.append(top_token)
                top_token = op_stack.pop()
    except IndexError:
        raise IndexError
    return


def add_left_bracket(op_stack, num):
    for _ in range(num):
        op_stack.push('(')
    return


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    cnt = 0
    for item in infixexpr:
        if item in "0123456789":
            if cnt > 2:
                return None
            cnt = 0
        elif prec.get(item) is not None:
            cnt += 1
            if item != '-' and item != '(' and cnt == 2:
                return None

    opStack = Stack()
    postfixList = []
    for token in infixexpr:
        if token == '\n':
            return None
    tokenList = infixexpr.split()
    for token in tokenList:
        try:
            #print("token:", token)
            # print("list: ", postfixList)
            res = re.match('(\\(*)(-*[0-9]*([.][0-9]*)*)(\\)*)', token)
            if not(res is None) and token != '-' and token != '+' and token != '*' and token != '/':
                check = re.search('[0-9]+\\/[1-9]\\.', token)
                if not (check is None):
                    st = ""
                    flag = 0
                    for char in token:
                        if char == '/':
                            flag = 1
                            continue
                        if not flag or char == ')':
                            st += char
                    token = st
                    #print(token)
                    res = re.match('(\\(*)(-*[0-9]*([.][0-9]+)*)(\\)*)', token)
                    #print(len(res.group(1)))
                    #print(len(res.group(4)))
                error = re.search('[^0-9|\\(|\\)|\\-|\\.]', token)
                if not (error is None):
                    return None

                add_left_bracket(opStack, len(res.group(1)))
                cnt = 0
                for char in res.group(2):
                    if char != '-':
                        break
                    cnt += 1
                if cnt % 2 == 0:
                    postfixList.append(float(res.group(2)[cnt:]))
                else:
                    postfixList.append(-float(res.group(2)[cnt:]))
                add_right_bracket(postfixList, opStack, len(res.group(4)))
            elif token == '(':
                add_left_bracket(opStack, 1)
            elif token == ')':
                add_right_bracket(postfixList, opStack, 1)
            else:

                while (not opStack.isEmpty()) and \
                   (prec[opStack.peek()] >= prec[token]):
                      postfixList.append(opStack.pop())
                opStack.push(token)
        except IndexError:
            return None
        except ValueError:
            return None
        except KeyError:
            return None
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList


def calculate(input_string):

    op_stack = infixToPostfix(input_string)
    print(op_stack)
    if op_stack is None:
        return None
    res_stack = []
    for token in op_stack:
        #stack_print(op_stack)
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

def  advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''

    # with open("../../tests/tests_data/test_hw_01_calcadv.ini.pkl", "rb") as f:
    #     data = pickle.load(f)
    # for item in data:
    #     print(item)
    #
    #     print("******************")
    print("input: ", input_string)
    #raise NotImplementedError
    res = calculate(input_string)
    if res is None:
        return None
    else:
        return float(res)

#print(calculate("2"))
#advanced_calculator("")
#print(advanced_calculator("(89 - 100)"))
#print(infixToPostfix("--3"))
print(advanced_calculator("15 + -24 - * 2 -26"))

