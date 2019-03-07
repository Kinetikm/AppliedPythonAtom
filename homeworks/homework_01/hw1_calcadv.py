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

    stack_out = []
    stack_ops = []
    priority = {'/': 3, '*': 3, '+': 2, '-': 2, '(': 1, ')': 1}

    args = []
    i = 0
    filtr = True #Костыль для чисел вроде .12345
    while i < len(input_string):
        try:
            if filtr is True: #Костыль для чисел вроде .12345
                int(input_string[i])
            if filtr is False: #Костыль для чисел вроде .12345
                filtr = True
            num = ''
            dot = False
            while True:
                if input_string[i] is '.':
                    if dot is False:
                        num += input_string[i]
                        dot = True
                    else:
                        return None
                    i += 1
                    continue
                try:
                    int(input_string[i])
                    num += input_string[i]
                    if i + 1 is len(input_string):
                        args.append(num)
                        break
                except ValueError:
                    i -= 1
                    args.append(num)
                    break
                i += 1
        except ValueError:
            if input_string[i] is '.' and filtr is True: #Костыль для чисел вроде .12345
                filtr = False
                continue
            if input_string[i] is ' ':
                i += 1
                continue
            if input_string[i] is '(' or input_string[i] is ')':
                args.append(input_string[i])
                try:
                    if input_string[i] is ')' and input_string[i - 1] is '(':
                        return None
                except KeyError:
                    return None
            elif input_string[i] is '*' or input_string[i] is '/':
                if len(args) is 0:
                    return None
                try:
                    float(args[-1])
                    args.append(input_string[i])
                except ValueError:
                    if args[-1] is ')':
                        args.append(input_string[i])
                    else:
                        return None
            elif input_string[i] is '+':
                if len(args) > 0 and (args[-1] is '+' or args[-1] is '-'):
                    i += 1
                    continue
                else:
                    args.append(input_string[i])
            elif input_string[i] is '-':
                if len(args) > 0:
                    if args[-1] is '+':
                        args[-1] = '-'
                    elif args[-1] is '-':
                        args[-1] = '+'
                    else:
                        args.append(input_string[i])
                else:
                    args.append(input_string[i])
            else:
                return None
        i += 1

    shortArgs = []
    for i in range(len(args)):
        if args[i] is '+' or args[i] is '-':
            try:
                float(args[i + 1])
                if i is 0 or args[i - 1] is '/' or args[i - 1] is '*':
                    if args[i] is '-':
                        args[i + 1] = (-1) * float(args[i + 1])
                else:
                    shortArgs.append(args[i])
            except KeyError:
                return None
            except ValueError:
                if args[i + 1] is '(':
                    shortArgs.append(args[i])
                else:
                    return None
        else:
            shortArgs.append(args[i])

    for item in shortArgs:
        try:
            float(item)
            stack_out.append(item)
        except ValueError:
            if item is ')':
                if len(stack_ops) is 0:
                    return None
                value = stack_ops.pop()
                while value != '(':
                    if len(stack_ops) is 0:
                        return None
                    stack_out.append(value)
                    value = stack_ops.pop()
            elif item is '(':
                stack_ops.append(item)
            else:
                if len(stack_ops) is 0:
                    stack_ops.append(item)
                else:
                    if priority[stack_ops[-1]] < priority[item]:
                        stack_ops.append(item)
                    else:
                        value = stack_ops[-1]
                        while priority[value] >= priority[item]:
                            stack_out.append(value)
                            stack_ops.pop()
                            if len(stack_ops) is 0:
                                break
                            value = stack_ops[-1]
                        stack_ops.append(item)
    while len(stack_ops) > 0:
        stack_out.append(stack_ops.pop())

    stack_nums = []
    for value in stack_out:
        try:
            priority[value]
            if len(stack_nums) < 2:
                return None
            else:
                b = stack_nums.pop()
                a = stack_nums.pop()
                if value is '*':
                    stack_nums.append(float(a) * float(b))
                elif value is '/':
                    if b is 0:
                        return None
                    else:
                        stack_nums.append(float(a) / float(b))
                elif value is '+':
                    stack_nums.append(float(a) + float(b))
                else:
                    stack_nums.append(float(a) - float(b))
        except KeyError:
            stack_nums.append(value)
    if len(stack_nums) is 1:
        return float(stack_nums[0])
    else:
        return None
