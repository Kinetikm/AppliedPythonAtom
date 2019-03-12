#!/usr/bin/env python
# coding: utf-8


class Heap(object):
    def __init__(self, array):
        self.array = array[:]
        self._build_heap()

    def add(self, elem_with_priority):
        self.array.append(elem_with_priority)
        self._shift_up(len(self.array) - 1)

    def _heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(self.array) and comparator_d(self.array[left],
                                                   self.array[largest]):
            largest = left
        if right < len(self.array) and comparator_d(self.array[right],
                                                    self.array[largest]):
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = (self.array[largest],
                                                  self.array[i])
            self._heapify(largest)

    def _shift_up(self, i):
        while i >= 1 and comparator_d(self.array[i], self.array[(i - 1) // 2]):
            self.array[i], self.array[(i - 1) // 2] = (
                self.array[(i - 1) // 2], self.array[i])
            i = (i - 1) // 2

    def _build_heap(self):
        for i in range(len(self.array) // 2)[::-1]:
            self._heapify(i)


class MaxHeap(Heap):

    def __init__(self, array):
        super(MaxHeap, self).__init__(array)

    def extract_maximum(self):
        res = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop(-1)
        self._heapify(0)
        return res


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
