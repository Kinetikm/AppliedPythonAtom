#!/usr/bin/env python
# coding: utf-8
# (1) - проверка на ошибки в выражении через eval
# (2) - проверка на ошибки в выражении по ходу разбора


def infix_to_postfix(infix):
    """
    Конвертирует инфиксную запись в постфиксную
    или возвращает None в случае некорректной записи
    """
    # проверяем возможность вычисления инфиксной записи (1)
    # try:
    #    float(eval(infix))
    # except (SyntaxError, NameError, TypeError):
    #    return None

    # преобразуем валидную инфиксную запись в постфиксную
    signs = ['(', ')', '+', '-', '*', '/']
    priorities = {'(': 2, ')': 2, '+': 0, '-': 0, '*': 1, '/': 1}
    temp = ''
    postfix_data = []
    stack = []
    last_is_digit = False  # для проверки на унарные операции
    has_space = False  # (2)
    for ch in infix:
        if ch.isspace():  # (2)
            has_space = True
        elif ch.isdigit() or ch in ['.', ',']:
            if last_is_digit and has_space:  # (2) -> 41   28
                # Если до этого было число и пробел -> ошибка
                return None
            temp += ch
            last_is_digit = True
            has_space = False  # (2)
        elif ch in signs:
            if not last_is_digit and ch != '(':
                temp += ch
            else:
                if temp:
                    postfix_data.append(temp)
                    temp = ''
                if len(stack) and ch == ')':
                    # забираем все что вошло до скобки
                    while stack[-1] != '(':
                        postfix_data.append(stack.pop())
                        # если стек при этом опустел - ошибка (2)
                        if not len(stack):
                            return None
                    # выкидываем скобку
                    stack.pop()
                else:
                    # выталкивание всех более приоритетных операций
                    if ch != '(':
                        while len(stack) and stack[-1] != '(' and \
                                priorities[ch] <= priorities[stack[-1]]:
                            postfix_data.append(stack.pop())
                    stack.append(ch)
            if ch != ')':
                last_is_digit = False
            has_space = False  # (2)
        else:  # (2) elif not ch.isspace()
            return None

    if temp:
        postfix_data.append(temp)

    while len(stack):
        postfix_data.append(stack.pop())

    return postfix_data


def calculate_postfix(postfix):
    """
    Вычисление выражения представленного в
    обратной польской записи (постфиксной)
    :param postfix: постфиксное выражение
    :return: результат вычисления или None
    """
    signs = ['+', '-', '*', '/']

    stack = []
    for item in postfix:
        try:
            stack.append(float(item))
        except ValueError:
            if item in signs:
                if len(stack) < 2:
                    # если операция невозможна (2)
                    return None

                y, x = stack.pop(), stack.pop()
                if item == '+':
                    stack.append(x + y)
                elif item == '-':
                    stack.append(x - y)
                elif item == '*':
                    stack.append(x * y)
                elif item == '/':
                    if x != 0:
                        stack.append(x / y)
                    else:  # деление на 0
                        return None
            else:  # недопустимый оператор
                return None

    return stack.pop() if len(stack) else None


def advanced_calculator(input_string):
    """
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    """
    # отсекаем все недопустимые операции (возведение в степень, ...)
    if '**' in input_string:
        return None

    # отсекаем недопустимые переносы строк (2)
    # (хотя в реалии это можно вычислить)
    # 3498
    #  +
    #  94894 -
    #  1.0
    if '\n' in input_string:
        return None

    # переведение всех операций к нормальному виду (-- -> +, ...)
    input_string = input_string.replace('++', '+')
    input_string = input_string.replace('--', '+')
    input_string = input_string.replace('+ +', '+')
    # input_string = input_string.replace('-+', '-')
    # input_string = input_string.replace('+-', '-')

    # переведение инфиксную нотацию к постфиксной
    postfix = infix_to_postfix(input_string)
    if not postfix:
        return None

    # приведение к постфиксному виду
    return calculate_postfix(postfix)


if __name__ == '__main__':
    print(advanced_calculator('(1 + 2) * 4'))
    print(advanced_calculator('62 - (24 + 21)'))
    print(advanced_calculator('28 - (11 + .16) * 82 - (29/1. + 17/1.)'))
