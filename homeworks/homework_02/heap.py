#!/usr/bin/env python
# coding: utf-8


class Heap():

    def __init__(self, array):
        self.heap = array[:]
        self.build_heap()

    def add(self, elem_with_priority):
        self.heap.append(elem_with_priority)
        self.build_heap()

    def shift_down(self, i):
        top = 2 * i + 1
        bottom = 2 * i + 2
        highest = i
        if (bottom < len(self.heap)) \
                and comparator_d(self.heap[bottom], self.heap[highest]):
            highest = bottom
        if (top < len(self.heap)) \
                and comparator_d(self.heap[top], self.heap[highest]):
            highest = top
        if highest != i:
            self.heap[i], self.heap[highest] = self.heap[highest], self.heap[i]
            self.shift_down(highest)

    def build_heap(self):
        for i in range(len(self.heap) // 2, -1, -1):
            self.shift_down(i)


class MaxHeap(Heap):

    def __init__(self, array):
        super().__init__(array)
        raise NotImplementedError

    def extract_maximum(self):
        res = self.heap.pop(0)
        self.build_heap()
        return res


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
