#!/usr/bin/env python
# coding: utf-8

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

operations_weights = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "(": 0
}


def input_string_modifications(input_string):
    if set('[~!@#$%^&_{}";\'\n]').intersection(input_string):
        return None
    if len(input_string) > 0 and (input_string[0] is
                                  "-" or input_string[0] is "+"):
        input_string = "0 " + input_string
    input_string = input_string.replace("--", '+')
    while "++" in input_string:
        input_string = input_string.replace("++", '+')
    input_string = input_string.replace("/", " / ")
    input_string = input_string.replace("*", " * ")
    input_string = input_string.replace("+", " + ")
    input_string = " ".join(input_string.split())
    while "+ +" in input_string:
        input_string = input_string.replace("+ +", '+')
    if "* *" in input_string or "- *" in input_string or "- /" in input_string or \
            "+ *" in input_string or "+ /" in input_string:
        return None
    for i in range(len(input_string)):
        if input_string[i] == " " and not input_string[i + 1] in operations and not input_string[i - 1] in operations:
            return None
        if input_string[i] == "-" and input_string[i + 1] != " " and not input_string[i - 2] in operations:
            input_string = input_string[:i - 1] + " +" + input_string[i - 1:]
    return input_string


def from_input_string_to_pol(input_string):
    operators = []
    string = []
    input_string = input_string_modifications(input_string)
    if input_string is None:
        return None
    for token in input_string.split(" "):
        if token in operations:
            if len(operators) > 0 and operations_weights[token] <= operations_weights[operators[-1]]:
                while len(operators) > 0 and operations_weights[token] <= operations_weights[operators[-1]]:
                    string.append(operators.pop())
            operators.append(token)
            continue
        if token.endswith(")"):
            token = token.replace(")", '')
            try:
                string.append(float(token))
            except ValueError:
                return None
            last_operator = operators.pop()
            while last_operator != "(":
                string.append(last_operator)
                if len(operators) == 0:
                    return None
                last_operator = operators.pop()
            continue
        if token.startswith("("):
            token = token.replace("(", '')
            operators.append("(")
        try:
            string.append(float(token))
        except ValueError:
            return None
    if len(operators) != 0:
        string = string + operators[::-1]
    return string


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''

    input_string = from_input_string_to_pol(input_string)
    if input_string is None:
        return None
    stack = []
    for token in input_string:
        if token in operations:
            try:
                op2, op1 = stack.pop(), stack.pop()
            except IndexError:
                return None
            stack.append(operations[token](op1, op2))
        else:
            try:
                stack.append(float(token))
            except ValueError:
                return None
    try:
        return stack.pop()
    except IndexError:
        return None
