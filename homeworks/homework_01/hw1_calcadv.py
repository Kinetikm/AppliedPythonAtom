#!/usr/bin/env python
# coding: utf-8


import re


def advanced_calculator(input_string):
    if input_string == '':  # отсеивает пустую
        return None

    for c in input_string:
        if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+',
                     '-', '*', '/', '(', ')', '.', ' ', '\t']:
            return None  # отсеивает строки с неприемлемыми символами

    if re.search("^[^0-9]+$", input_string):
        return None  # отсеивает строки без цифр

    if re.search(r"[\+\-\*/]$", input_string) or \
            re.search(r"^[\*/]", input_string):
        return None  # отсеивает строки с не тем знаком на конце/начале

    lst = re.findall(r"[\w+-/()*]+", input_string)
    # хитрый сплит по любому служебному символу (пробелам и таб сразу)

    for i in range(len(lst) - 1):  # отсеивает 2 числа через проб или таб
        try:
            float(lst[i])
            float(lst[i + 1])
            if float(lst[i + 1]) >= 0:
                return None  # если 2-ое число <0, то это вычитание
        except:
            pass

    st = ''.join(lst)  # обратное превращение в строку (так надо)

    while True:  # сокращает все --- ++- и тд до ОДНОГО знака
        st = st.replace('--', '+')
        st = st.replace('++', '+')
        st = st.replace('+-', '-')
        st = st.replace('-+', '-')

        cnt = 0
        cnt += (st.count('--') + st.count('++') +
                st.count('+-') + st.count('-+'))
        if cnt == 0:
            break

    if st[0] == '-':  # если начинается с - , то подписываем 0
        st_new = '0' + st
    else:
        st_new = st
    if st[0] == '+':  # если начинается с + , то убираем его
        st_new = st[1:]

    st_new = st_new.replace('(-', '(0-')
    st_new = st_new.replace('(+', '(')

    if re.search(r'\.[\d]+\.', st_new):  # отсеивает случай 1.2.3
        return None

    if '()' in st_new or st_new.count('(') != st_new.count(')'):
        return None  # проверка на пустые скобки и равенство откр. и закр.

    a, b = 0, 0
    for c in st_new:  # например, отсеет )(2+5)(
        if c == '(':
            a += 1
        if c == ')':
            b += 1
        if a < b:
            return None

    while st_new.count('/-') != 0 or st_new.count('/+') != 0 or \
            st_new.count('*-') != 0 or st_new.count('*+') != 0:
        st_new = re.sub(r"([\d\+\-\(\)])([\/\*])([\-\+]\d+\.?[0-9]*)",
                        r"\1\2(0\3)", st_new)  # для умн/дел на отриц.числа

    wrong = [r'\+\*', r'\+/', r'\+\)', r'\-\*', r'-\/', r'-\)', r'\*\*',
             r'\*/', r'\*\)', r'/\*', r'//', r'/\)', r'\(\*', r'\(/',
             r'\)\(', r'\)\d', r'\d\(', r'\.{2,}']
    for part in wrong:
        if re.search(part, st_new):
            return None  # отсеивание других невозможных вариантов

    # ЕСЛИ СТРОКА ДОШЛА ДО ЭТОГО МЕСТА, ТО ОНА ВАЛИДНАЯ И ЕЕ МОЖНО ПОСЧИТАТЬ

    priority = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}  # перевод в ОПЗ
    st_new += '_'
    stek_numbers = []
    stek_oper = []
    stek_count = []
    num = ''

    for s in st_new:
        if s.isdigit() or s == '.':
            num += s
        elif num != '':
            stek_numbers.append(float(num))
            num = ''

        if s in ['+', '-', '*', '/'] and \
                (stek_oper == [] or priority[s] > priority[stek_oper[-1]]):
            stek_oper.append(s)
        elif s in ['+', '-', '*', '/'] and \
                priority[s] <= priority[stek_oper[-1]]:
            while stek_oper != [] and \
                    priority[s] <= priority[stek_oper[-1]]:
                stek_numbers.append(stek_oper.pop())
            stek_oper.append(s)
        elif s == '(':
            stek_oper.append(s)
        elif s == ')':
            while stek_oper[-1] != '(':
                stek_numbers.append(stek_oper.pop())
            stek_oper.pop()

    while stek_oper != []:
        stek_numbers.append(stek_oper.pop())

    # вычисление выражения

    for k in stek_numbers:
        if type(k) == float:
            stek_count.append(k)

        elif k == '+':
            stek_count.append(float(stek_count.pop()) +
                              float(stek_count.pop()))
        elif k == '-':
            stek_count.append(-float(stek_count.pop()) +
                              float(stek_count.pop()))
        elif k == '*':
            stek_count.append(float(stek_count.pop()) *
                              float(stek_count.pop()))
        elif k == '/':
            try:
                stek_count.append(1 / (float(stek_count.pop()) /
                                       float(stek_count.pop())))
            except ZeroDivisionError:
                return None

    return (stek_count[0])
