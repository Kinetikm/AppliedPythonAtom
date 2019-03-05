#!/usr/bin/env python
# coding: utf-8
import re


def _is_valid(input_string):
    """
    Проверяет выражение на валидность
    :param input_string: выражение
    :return: True если выражение валидно, иначе False
    """
    if any(re.findall(r'([^0-9*/ ()+\-.\t]+)', input_string)):
        return False
    if any(re.findall(r'([*/]+[ +-]*[*/]+)', input_string)):
        return False
    if any(re.findall(r'([(]+[0-9]{0}[)])', input_string)):
        return False
    if any(re.findall(r'([+-]+[ ]?[*/]+)', input_string)):
        return False
    if any(re.findall(r'(\d+[ ]+\d+)', input_string)):
        return False
    start = input_string.split(maxsplit=1)
    if not len(start) or any(re.findall('[^0-9-+(]', start[0][0])):
        return False
    end = input_string.rsplit(maxsplit=1)
    if not len(end) or any(re.findall('[^0-9)]', end[-1][::-1][0])):
        return False
    return True


def _collapse(input_string):
    """
    Собирает последовательность из +- в одну операцию
    :param input_string: строка с выражением
    :return: строка с выражением, у которого нет повторяющихся +-
    """
    return re.sub(
        r'[ ]*[-+]+[ ]*[-+]*[ ]*[-+]*',
        lambda x: '-' if x.group().count('-') % 2 else '+',
        input_string)


def _convert(input_string):
    """
    Превращает строку в лист операторов и чисел
    :param input_string: строка с выражением
    :return: лист операторов и чисел
    """
    return re.findall('([0-9.]+|[()+-/*])', input_string)


def _to_polska(op_list):
    """
    Конвертирует лист с выражением в польскую нотацию
    :param op_list: лист операторов и чисел
    :return: Лист операторов и чисел в польской нотации
    """
    out = []
    op_stack = []
    op_high_prior = {'*', '/'}
    op_low_prior = {'+', '-'}

    prior_dict = {}
    prior_dict.update({op: 2 for op in op_high_prior})
    prior_dict.update({op: 1 for op in op_low_prior})
    ind_brackets = []
    previous_op = None
    for op in op_list:
        try:
            out.append(float(op))
        except ValueError:
            if previous_op in op_high_prior and op in op_low_prior:
                if op == '-':
                    out[-1] *= -1
            elif op == '(':
                op_stack.append(op)
                ind_brackets.append(len(op_stack))
            elif op == ')':
                if not ind_brackets:
                    return None
                out.extend(op_stack[ind_brackets[-1]:][::-1])
                op_stack = op_stack[:ind_brackets[-1] - 1]
                ind_brackets.pop()
            elif op_stack:
                while op_stack \
                        and prior_dict.get(op_stack[-1], 0) >= prior_dict[op]:
                    out.append(op_stack.pop())
                op_stack.append(op)
            else:
                op_stack.append(op)
        previous_op = op
    if ind_brackets:
        return None
    out.extend(op_stack[::-1])
    return out


def _process_calc(input_polska):
    """
    Калькулятор, принимающий запись в польской нотации
    :param input_polska: выражение в польской нотации
    :return: возвращает посчитанное значение или None если это невозможно
    """
    op_action = {
        '*': lambda x, y: x * y,
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x / y
    }
    if not input_polska:
        return None
    stack = [0, ]

    for op in input_polska:
        if isinstance(op, (int, float)):
            stack.append(op)
        else:
            try:
                stack.append(op_action[op](y=stack.pop(), x=stack.pop()))
            except (KeyError, ZeroDivisionError):
                return None

    if not stack:
        return None
    elif len(stack) == 2 and stack[0] != 0:
        return None
    elif len(stack) > 2:
        return None
    else:
        return stack.pop()


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    if not _is_valid(input_string):
        return None
    input_string = _collapse(input_string)
    out = _to_polska(_convert(input_string))
    res = _process_calc(out)
    return res
