#!/usr/bin/env python
# coding: utf-8


class Heap1:
    '''
    Что то вроде реализации Heap но неправильная, так как сделана не
    через дерево, поэтому вынесена в отдельный файл.
    '''

    def __init__(self, array):
        self.list = array
        if array:
            self.build_heap()

    def add(self, elem_with_priority):
        if comparator_d(elem_with_priority, self.list[len(self.list) - 1]):
            self.list.append(elem_with_priority)
        for i in range(len(self.list)):
            if comparator_d(self.list[i], elem_with_priority):
                self.list.insert(i, elem_with_priority)
                break

    def build_heap(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.list) - 1):
                if comparator_d(self.list[i], self.list[i + 1]):
                    self.list[i], self.list[i + 1] = self.list[i + 1], \
                                                     self.list[i]
                    swapped = True


class MaxHeap1(Heap1):

    def __init__(self, array):
        super().__init__(array)

    def extract_maximum(self):
        maximum = self.list.pop()
        return maximum


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
