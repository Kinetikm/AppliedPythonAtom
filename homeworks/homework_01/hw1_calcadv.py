#!/usr/bin/env python
# coding: utf-8
'''
     Калькулятор на основе обратной польской записи.
     Разрешенные операции: открытая скобка, закрытая скобка,
          плюс, минус, умножить, делить
     :param input_string: строка, содержащая выражение
     :return: результат выполнение операции, если строка валидная - иначе None
'''


def rev(char):
    if char == ')':
        return '('
    elif char == ']':
        return '['
    elif char == '}':
        return '{'
    elif char == '(':
        return ')'
    elif char == '[':
        return ']'
    elif char == '{':
        return '}'


def is_bracket_correct(input_string):
    if len(input_string) % 2 != 0:
        return False
    else:
        while len(input_string) != 0:
            i = 0
            while input_string[i] != ')'\
                    and input_string[i] != ']'\
                    and input_string[i] != '}':
                i += 1
                if i > len(input_string)-1:
                    return False
            if input_string[0] == (')' or ']' or '}'):
                return False
            if input_string[i-1] == rev(input_string[i]):
                if len(input_string) > 2:
                    if i > 1:
                        input_string = input_string[:i-1]+input_string[i+1:]
                    else:
                        input_string = input_string[i+1:]
                else:
                    input_string = ''
            else:
                return False
        return True


def Check_valid(string):
    check_str = "\
    qwertyuiop[]';lkjhgfdsazxcvbnm,йцукенгшщзхъэждлорпавыфячсмитьбю\n\t\
         "
    for i in string:
        if i in check_str:
            return False
        if i in check_str.upper():
            return False
    brstr = ''
    for i in string:
        if i == '(' or i == ')':
            brstr += i
    br = is_bracket_correct(brstr)
    if br is True:
        for i in range(len(string)):
            if string[i] == '(' and string[i+1] == ')':
                return False
        string = string.replace('(', '')
        string = string.replace(')', '')
        numblist = []
        znaklist = []
        i = 0
        while i < len(string):
            j = string[i]
            tmp = ''
            while j != '-' and j != '+'\
                    and j != '*' and j != '/'\
                    and i < len(string):
                tmp += string[i]
                i += 1
                if i < len(string):
                    j = string[i]
            if tmp != '':
                numblist.append(tmp)
            if i < len(string):
                if j == '-' or j == "+":
                    if string[i] != string[i+1]:
                        znaklist.append(string[i])
                    else:
                        znaklist.append('+')
                        i += 1
                else:
                    znaklist.append(string[i])
            i += 1
        if len(numblist) == 1 and len(znaklist) == 1:
            return True
        if len(numblist) == len(znaklist)+1:
            return True
    return False


def equals_or_higher(prev, cur):
    if prev == '+' and cur == "*":
        return False
    if prev == '-' and cur == "*":
        return False
    if prev == '+' and cur == "/":
        return False
    if prev == '-' and cur == "/":
        return False
    if prev == '(' or prev == ')' or cur == '(' or cur == ')':
        return False
    return True


def OPN(string):
    numb = []
    operation = []
    string = string.replace(" ", '')
    i = 0
    while i < len(string):
        j = string[i]
        tmp = ''
        while j != '-' and j != '+'\
                and j != '*' and j != '/'\
                and j != '(' and j != ')'\
                and i < len(string):
            if string[i] == '.':
                if i != 0:
                    lol = string[i-1]
                    if lol == "-" or lol == '+'\
                            or lol == '*' or lol == '/'\
                            or lol == ')' or lol == '(':
                        tmp += '0'
                else:
                    tmp += '0'
            tmp += string[i]
            i += 1
            if i < len(string):
                j = string[i]
        if tmp != '':
            numb.append(tmp)
        if i < len(string):
            if string[i] == ')':
                for tail in reversed(operation):
                    if tail == '(':
                        operation.pop()
                        break
                    numb.append(operation.pop())
            if string[i] != '(' and len(operation) != 0:
                if equals_or_higher(
                    operation[len(operation)-1], string[i]
                ) is True:
                    numb.append(operation.pop())

            if string[i] == '-' or string[i] == "+":
                if string[i] != string[i+1]:
                    operation.append(string[i])
                else:
                    operation.append('+')
                    i += 1
            else:
                if string[i] != ')':
                    operation.append(string[i])
        i += 1
    for o in reversed(operation):
        numb.append(o)
    return numb


def calculate(var1, var2, op):
    if op == '+':
        return float(var1)+float(var2)
    if op == '-':
        return float(var1)-float(var2)
    if op == '*':
        return float(var1)*float(var2)
    if op == '/':
        if var2 == 0:
            return None
        return float(var1)/float(var2)


def count(oplist):
    if len(oplist) == 2:
        if oplist[1] == "+":
            return float(oplist[0])
        elif oplist[1] == '-':
            return -float(oplist[0])
        else:
            return None
    j = 0
    while j < len(oplist) and len(oplist) != 1:
        i = oplist[j]
        if i == '+' or i == '-' or i == '/' or i == '*':
            value = calculate(oplist[j-2], oplist[j-1], oplist[j])
            if value is None:
                return None
            oplist = oplist[:j-2]+oplist[j+1:]
            oplist.insert(j-2, value)
            j = 0
        else:
            j += 1

    return float(oplist[0])


def advanced_calculator(input_string):
    print(input_string)
    flag = Check_valid(input_string)
    if flag is True:
        operation_list = OPN(input_string)
        print(operation_list)
        answer = count(operation_list)
        return answer
    return None