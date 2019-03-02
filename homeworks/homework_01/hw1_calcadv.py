#!/usr/bin/env python
# coding: utf-8
import re


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    if any(re.findall(r'([^0-9.+ /\-\*()\t]{1,}|\*{2})', input_string)):
        return None
    try:
        return float(eval(input_string))
    except:
        return None
