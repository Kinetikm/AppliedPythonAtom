#!/usr/bin/env python
# coding: utf-8

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''

    map1 = {
        '{': '{}',
        '[': '[]',
        '(': '()',
        '}': '{}',
        ']': '[]',
        ')': '()'
    }

    s = Stack()
    list_push = ['{', '[', '(']
    list_pop = ['}', ']', ')']

    for br in input_string:
        if br in map1.keys():
            if br in list_push:
                s.push(map1[br])
            if br in list_pop:
                try:
                    tmp = s.pop()
                except IndexError:
                    return False
                if map1[br] != tmp:
                    return False

    if s.isEmpty():
        return True

    return False
