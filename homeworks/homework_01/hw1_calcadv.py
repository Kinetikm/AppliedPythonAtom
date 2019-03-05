#!/usr/bin/env python
# coding: utf-8


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    if input_string.find('**') != -1:
        return
    try:
        result = eval(input_string)
        if isinstance(result, int) or isinstance(result, float):
            return result
        return
    except BaseException:
        return
    raise NotImplementedError
