#!/usr/bin/env python
# coding: utf-8


def advanced_calculator(input):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    for i in range(10):
        input = input.replace(str(i) + " ", str(i) + "|")
    while " " in input:
        input = input.replace(" ", "")
    while "\t" in input:
        input = input.replace("\t", "")
    while "--" in input:
        input = input.replace("--", "+")
    while "++" in input:
        input = input.replace("++", "+")
    while "+-" in input:
        input = input.replace("+-", "-")
    while "(-" in input:
        input = input.replace("(-", "(0-")
    while "/-" in input:
        input = input.replace("/-", "*(0-1)/")
    while "*-" in input:
        input = input.replace("*-", "*(0-1)*")
    if len(input) > 0 and (input[0] is "-" or input[0] is "+"):
        input = "0" + input
    unit = ""
    output_list = []
    st = []

    def is_op(operator):
        return operator is "+" or operator is "-" \
               or operator is "/" or operator is "*"

    while len(input) > 0:
        if is_op(input[0]):
            if len(unit) > 0:
                try:
                    output_list.append(float(unit))
                    unit = ""
                except (TypeError, ValueError):
                    return None
            while len(st) > 0 and st[len(st) - 1] is not "(":
                if st[len(st) - 1] is '*' or input[0] is '+' \
                        or st[len(st) - 1] is '/' or input[0] is '-':
                    output_list.append(st.pop())
                else:
                    break
            st.append(input[0])
            input = input[1:]

        elif input[0] is "(":
            if len(unit) > 0:
                return None
            st.append("(")
            input = input[1:]

        elif input[0] is ")":
            if len(unit) == 0:
                return None
            try:
                output_list.append(float(unit))
                unit = ""
            except (TypeError, ValueError):
                return None

            input = input[1:]

            try:
                unit = st.pop()
                while unit is not "(":
                    output_list.append(unit)
                    unit = st.pop()
                unit = ""
            except IndexError:
                return None

        elif input[0].isdigit() or input[0] is ".":
            unit += input[0]
            input = input[1:]

        elif input[0] is "|":
            output_list.append(float(unit))
            unit = ""
            input = input[1:]

        else:
            return None

    if len(unit) > 0:
        try:
            output_list.append(float(unit))
            unit = ""
        except (ValueError, TypeError):
            return None

    while len(st) > 0:
        output_list.append(st.pop())

    try:

        while len(output_list) > 0:

            unit = output_list.pop(0)

            if isinstance(unit, float):
                st.append(unit)

            else:
                unit2 = st.pop()
                unit1 = st.pop()

                if unit is "+":
                    st.append(unit1 + unit2)

                elif unit is "-":
                    st.append(unit1 - unit2)

                elif unit is "/":
                    try:
                        st.append(unit1 / unit2)
                    except ZeroDivisionError:
                        return None

                elif unit is "*":
                    st.append(unit1 * unit2)
    except IndexError:
        return None

    if len(st) != 1:
        return None

    return st[0]
