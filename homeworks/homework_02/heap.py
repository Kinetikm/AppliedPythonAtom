#!/usr/bin/env python
# coding: utf-8


class Heap():

    def __init__(self, array):
        self.input_inf = array[:]
        self.main = []
        self.build_heap()

    def add(self, elem_with_priority):
        self.main.append(elem_with_priority)
        i = len(self.main) - 1
        while i > 0:
            parent_i = (i - 1)//2
            if comparator_d(self.main[i], self.main[parent_i]):
                h = self.main[i]
                self.main[i] = self.main[parent_i]
                self.main[parent_i] = h
                i = parent_i
            else:
                break

    def build_heap(self):
        i = 1
        if self.input_inf:
            self.main.append(self.input_inf[0])
            while i < len(self.input_inf):
                self.add(self.input_inf[i])
                i += 1


class MaxHeap(Heap):

    def __init__(self, array):
        Heap.__init__(self, array)

    def extract_maximum(self):
        result = self.main[0]
        i = len(self.main) - 1
        self.main[0] = self.main[i]  # перемещаем последний элемент в корень
        self.main.pop()
        i = 0
        while 2*i+1 < len(self.main) - 1:  # фактически метод shift down
            child_l_i = 2*i+1
            child_r_i = 2*i+2
            if comparator_d(self.main[child_l_i], self.main[child_r_i]):
                change_i = child_l_i
            else:
                change_i = child_r_i
            h = self.main[i]
            self.main[i] = self.main[change_i]
            self.main[change_i] = h
            i = change_i
        if 2*i+1 == len(self.main) - 1:  # случай единственного сына
            if comparator_d(self.main[2*i+1], self.main[i]):
                h = self.main[i]
                self.main[i] = self.main[2*i+1]
                self.main[2*i+1] = h
        return result


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
    