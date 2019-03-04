#!/usr/bin/env python
# coding: utf-8


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''

    infix_list = cast(input_string)
    postfix_list = infix_to_postfix(infix_list)

    while True:
        bool = 0
        for idx, val in enumerate(postfix_list):
            if idx == len(postfix_list) - 1:
                break
            if val == '+' and postfix_list[idx+1] == '-' or val == '-' and postfix_list[idx+1] == '+':
                postfix_list = postfix_list[:idx-1] + ['-'] + postfix_list[:idx+2]
                bool += 1
                break
            if val == '-' and postfix_list[idx+1] == '-' or val == '+' and postfix_list[idx+1] == '+':
                postfix_list = postfix_list[:idx-1] + ['-'] + postfix_list[:idx+2]
                bool += 1
                break
        if bool == 0:
            break

    stack = []
    sp = 0
    for val in postfix_list:
        try:
            if val == '+':
                stack[sp - 2] = stack[sp - 2] + stack[sp - 1]
                sp -= 1

            if val == '-':
                stack[sp - 2] = stack[sp - 2] - stack[sp - 1]
                sp -= 1

            if val == '*':
                stack[sp - 2] = stack[sp - 2] * stack[sp - 1]
                sp -= 1

            if val == '/':
                stack[sp - 2] = stack[sp - 2] / stack[sp - 1]
                sp -= 1

            if represents_int(val):
                stack.append(val)
                sp += 1
        except ZeroDivisionError:
            return None
        except ValueError:
            return None
        except IndexError:
            return None
    try:
        answer = stack[sp-1]
    except IndexError:
        return None

    return answer


def cast(input_string):
    return "".join(input_string.split())\
        .replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')\
        .replace('(', ' ( ')\
        .replace(')', ' ) ')\
        .split()


def infix_to_postfix(input_list):
    s = Stack()
    lst = []

    for elem in input_list:

        if represents_int(elem):
            lst.append(elem)

        if elem == '(':
            s.push(elem)

        if elem == ')':
            fl = True
            while fl:
                while not s.is_empty():
                    tmp = s.pop()
                    if tmp == '(':
                        fl = False
                        continue
                    else:
                        lst.append(tmp)

        if elem == '/' or elem == '*' or elem == '+' or elem == '-':
            if s.is_empty():
                s.push(elem)
                continue
            while pop_elems_by_prior(elem, s.peek()):
                lst.append(s.pop())
                if s.is_empty():
                    break
            s.push('/')

    while not s.is_empty():
        lst.append(s.pop())

    return lst


def pop_elems_by_prior(elem, peek):
    priorities = {
        '(': 1,
        ')': 1,
        '+': 2,
        '-': 2,
        '*': 3,
        '/': 3,
    }

    if priorities[elem] <= priorities[peek]:
        return True
    return False


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    print(infix_to_postfix('2+1*'))
