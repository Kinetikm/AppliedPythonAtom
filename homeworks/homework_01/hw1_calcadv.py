#!/usr/bin/env python
# coding: utf-8

'''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
'''


def advanced_calculator(input_string):
    raise NotImplementedError  # не доработал все случаи
    if len(input_string) == 0:
        return None

    def search(list, z, x=0, y=-1):
        if y == -1:
            y = len(list)
        for i in range(x, y):
            if list[i] == z:
                return i
        return -1

    def is_digit(string):
        if string.isdigit():
            return True
        else:
            try:
                float(string)
                return True
            except ValueError:
                return False

    def adv_calc(obj):

        while search(obj, '*') != -1:
            p = search(obj, '*')
            try:
                obj[p - 1] = obj[p - 1] * obj[p + 1]
            except Exception:
                return None
            obj.pop(p)
            obj.pop(p)

        while search(obj, '/') != -1:
            p = search(obj, '/')
            try:
                obj[p - 1] = obj[p - 1] / obj[p + 1]
            except Exception:
                return None
            obj.pop(p)
            obj.pop(p)

        while search(obj, '-') != -1:
            p = search(obj, '-')
            try:
                obj[p - 1] = obj[p - 1] - obj[p + 1]
            except Exception:
                return None
            obj.pop(p)
            obj.pop(p)

        while search(obj, '+') != -1:
            p = search(obj, '+')
            try:
                obj[p - 1] = obj[p - 1] + obj[p + 1]
            except Exception:
                return None
            obj.pop(p)
            obj.pop(p)

        return obj[0]

    j = 0
    while input_string.find(')', j) != -1:
        p = input_string.find(')', j)
        j = p + 2
        input_string = input_string[:p] + ' ' + input_string[p:]

    j = 0
    while input_string.find('(', j) != -1:
        p = input_string.find('(', j)
        j = p + 2
        input_string = input_string[:p + 1] + ' ' + input_string[p + 1:]

    input_string = input_string.strip(' ')

    obj = input_string.split(' ')

    znak = 0
    os = 0
    zs = 0
    numbers = 0

    for i in range(len(obj)):
        if obj[i] == '':
            return None
        elif obj[i] == '++':
            obj[i] = '+'
        elif obj[i] == '--':
            obj[i] = '-'
        elif obj[i] == '+' or obj[i] == '-' or obj[i] == '*' \
                or obj[i] == '/':
            znak += 1
        elif obj[i] == '(':
            os += 1
        elif obj[i] == ')':
            zs += 1
        elif is_digit(obj[i]):
            obj[i] = float(obj[i])
            numbers += 1
        elif obj[i][0] == '-' and obj[i][1] == '-':
            if is_digit(obj[i][2:]):
                obj[i] = float(obj[i][2:])
                numbers += 1
        else:
            return None
    if os != zs or znak != numbers - 1:
        return None

    while search(obj, '(') != -1:
        p1 = search(obj, '(')
        p2 = search(obj, ')')
        while search(obj, '(', p1 + 1, p2) != -1:
            p1 = search(obj, '(', p1 + 1, p2)
        obj[p1] = adv_calc(obj[p1 + 1: p2])
        for k in range(p2 - p1):
            obj.pop(p1 + 1)

    return adv_calc(obj)


print(advanced_calculator('()'))
