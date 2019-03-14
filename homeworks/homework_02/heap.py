#!/usr/bin/python
# -*- coding: utf-8 -*-


class Heap:

    def __init__(self, array):
        self._heap = array[:]
        self.build_heap()

    def sift_up(self, element_index):
        _list = self._heap
        parent = (element_index - 1) // 2
        while element_index > 0 and comparator_d(_list[element_index],
                _list[parent]):
            (_list[element_index], _list[parent]) = (_list[parent],
                    _list[element_index])
            element_index = parent
            parent = (element_index - 1) // 2

    def sift_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(self._heap) and comparator_d(self._heap[left],
                self._heap[largest]):
            largest = left

        if right < len(self._heap) and comparator_d(self._heap[right],
                self._heap[largest]):
            largest = right
        if largest != i:
            (self._heap[i], self._heap[largest]) = \
                (self._heap[largest], self._heap[i])
            self.sift_down(largest)

    def add(self, elem_with_priority):
        self._heap.append(elem_with_priority)
        self.sift_up(len(self._heap) - 1)

    def build_heap(self):
        for i in reversed(range(len(self._heap) // 2)):
            self.sift_down(i)


class MaxHeap(Heap):

    def __init__(self, array):
        super().__init__(array)

    def extract_maximum(self):
        max_elem = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop(-1)
        self.sift_down(0)
        return max_elem


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
