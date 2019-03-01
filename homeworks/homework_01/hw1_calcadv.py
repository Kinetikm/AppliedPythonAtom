#!/usr/bin/env python
# coding: utf-8


def rm(line, a, b):
    while a in line:
        line = line.replace(a, b)
    return line


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    queue = []
    open_bracket = '('
    close_bracket = ')'
    good = open_bracket + close_bracket
    not_good = ''
    for i in input_string:
        if i not in good:
            not_good += i
    for i in not_good:
        input_string = rm(input_string, i, '')
    for char in input_string:
        if char in open_bracket:
            queue.append(char)
        else:
            if len(queue) == 0:
                return False
            if open_bracket.find(queue[-1]) == close_bracket.find(char):
                queue.pop()
            else:
                return False
    return len(queue) == 0


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    if input_string is None:
        return None
    try:
        input_string = str(input_string)
        possible_symbols = '0123456789()-+/*. '
        nums = '01234567890'
        for i in input_string:
            if i not in possible_symbols:
                return None
        input_string = str(input_string)
        input_string = rm(input_string, '  ', ' ')
        for i in range(1, len(input_string) - 1):
            if input_string[i] == ' ' \
                    and input_string[i - 1] in nums \
                    and input_string[i + 1] in nums:
                return None
        input_string = rm(input_string, ' ', '')
        input_string = rm(input_string, '++', '+')
        input_string = rm(input_string, '--', '+')
        input_string = rm(input_string, '+-', '-')
        input_string = rm(input_string, '-+', '-')
        input_string = rm(input_string, ' ', '')
        input_string = rm(input_string, '++', '+')
        input_string = rm(input_string, '--', '+')
        input_string = rm(input_string, '+-', '-')
        input_string = rm(input_string, '-+', '-')
        error_operations = ['+*', '-*', '-/', '+/',
                            '**', '//', '*/', '/*',
                            '-)', '+)', '*)', '/)', '()',
                            '(/', '(*']
        for error_pairs in error_operations:
            if error_pairs in input_string:
                return None
        input_string = input_string.replace('(', ' ( ')
        input_string = input_string.replace(')', ' ) ')
        input_string = input_string.replace('+', ' + ')
        input_string = input_string.replace('-', ' - ')
        input_string = input_string.replace('/', ' / ')
        input_string = input_string.replace('*', ' * ')
        input_string = rm(input_string, '  ', ' ')
        if not is_bracket_correct(input_string):
            return None
        sequence = input_string.split()
        if len(sequence) == 0:
            return None
        if sequence[0] == '+':
            sequence = sequence[1::]
        for i in range(len(sequence)):
            if sequence[i] not in '+-*/()':
                sequence[i] = float(sequence[i])
        for i in range(len(sequence) - 1):
            if isinstance(sequence[i], float) \
                    and isinstance(sequence[i + 1], float):
                return None
            if isinstance(sequence[i], float) \
                    and sequence[i + 1] == '(':
                return None
            if isinstance(sequence[i + 1], float) \
                    and sequence[i] == ')':
                return None
        for i in range(len(sequence) - 1):
            if sequence[i] != '-':
                continue
            if isinstance(sequence[i + 1], float):
                # '-','1' -> ' ','-1'
                sequence[i + 1] *= -1
                if i == 0 or sequence[i - 1] == '(' \
                        or sequence[i - 1] == '/' \
                        or sequence[i - 1] == '*':
                    sequence[i] = ' '
                else:
                    sequence[i] = '+'
        while ' ' in sequence:
            sequence.remove(' ')

        priority = {'-': 1, '+': 1, '/': 2, '*': 2,
                    '(': 0, ')': 0}

        operators = {'-': lambda x, y: x - y,
                     '+': lambda x, y: x + y,
                     '/': lambda x, y: x / y,
                     '*': lambda x, y: x * y
                     }
        operations_stack = []  # для избежания лишних
        # обращений к try/except
        output_array = []
        for i in sequence:
            if isinstance(i, float):
                output_array.append(i)
            else:
                if i == ')':
                    cur = operations_stack[-1]
                    while cur != '(':
                        output_array.append(cur)
                        operations_stack.pop(-1)
                        cur = operations_stack[-1]
                    operations_stack.pop()
                elif len(operations_stack) == 0:
                    operations_stack.append(i)
                elif i == '(':
                    operations_stack.append('(')
                else:
                    while len(operations_stack) > 0 \
                            and priority[operations_stack[-1]] \
                            >= priority[i]:
                        output_array.append(operations_stack[-1])
                        operations_stack.pop(-1)
                    operations_stack.append(i)
        while len(operations_stack) > 0:
            output_array.append(operations_stack[-1])
            operations_stack.pop()
        stack = []
        print(output_array)
        for i in output_array:
            if isinstance(i, float):
                stack.append(i)
            else:
                if len(stack) < 2:
                    return None
                x = stack[-1]
                stack.pop()
                y = stack[-1]
                stack.pop()
                try:
                    stack.append(operators[i](y, x))
                except ZeroDivisionError:
                    return None
        if len(stack) == 1:
            return stack[0]
        else:
            return None
        return None
    except Exception:
        return None
