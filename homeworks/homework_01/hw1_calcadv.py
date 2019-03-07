#!/usr/bin/env python
# coding: utf-8


opers = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

operates = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "(": 0
}


def input_modificate(input_string):
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
    if "* *" in input_string\
            or "- *" in input_string \
            or "- /" in input_string or \
            "+ *" in input_string or "+ /" in input_string:
        return None
    for i in range(len(input_string)):
        if input_string[i] == " "\
                and not input_string[i + 1] in opers\
                and not input_string[i - 1] in opers:
            return None
        if input_string[i] == "-"\
                and input_string[i + 1] != " "\
                and not input_string[i - 2] in opers:
            input_string = input_string[:i - 1] + " +" + input_string[i - 1:]
    return input_string


def string_to_pol(input_string):
    operators = []
    string = []
    input_string = input_modificate(input_string)
    if input_string is None:
        return None
    for tk in input_string.split(" "):
        if tk in opers:
            if len(operators) > 0\
                    and operates[tk] <= operates[operators[-1]]:
                while len(operators) > 0\
                        and operates[tk] <= operates[operators[-1]]:
                    string.append(operators.pop())
            operators.append(tk)
            continue
        if tk.endswith(")"):
            tk = tk.replace(")", '')
            try:
                string.append(float(tk))
            except ValueError:
                return None
            last_operator = operators.pop()
            while last_operator != "(":
                string.append(last_operator)
                if len(operators) == 0:
                    return None
                last_operator = operators.pop()
            continue
        if tk.startswith("("):
            tk = tk.replace("(", '')
            operators.append("(")
        try:
            string.append(float(tk))
        except ValueError:
            return None
    if len(operators) != 0:
        string = string + operators[::-1]
    return string


def advanced_calculator(input_string):
    input_string = string_to_pol(input_string)
    if input_string is None:
        return None
    stack = []
    for tk in input_string:
        if tk in opers:
            try:
                op2, op1 = stack.pop(), stack.pop()
            except IndexError:
                return None
            stack.append(opers[tk](op1, op2))
        else:
            try:
                stack.append(float(tk))
            except ValueError:
                return None
    try:
        return stack.pop()
    except IndexError:
        return None
    raise NotImplementedError
