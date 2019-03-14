#!/usr/bin/env python
# coding: utf-8


class Heap:
    def __init__(self, array):
        self.heap = array[:]
        self.build_heap()

    def add(self, elem_with_priority):
        self.heap.append(elem_with_priority)
        self._sift_up(len(self.heap) - 1)

    def build_heap(self):
        for i in reversed(range(len(self.heap) // 2)):
            self._sift_down(i)

    def _sift_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2

        largest = i
        if left < len(self.heap) and comparator_d(self.heap[left], self.heap[i]):
            largest = left
        if right < len(self.heap) and comparator_d(self.heap[right], self.heap[largest]):
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._sift_down(largest)

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if not comparator_d(self.heap[index], self.heap[parent]):
                return
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent

    def pop(self):
        last_element = self.heap.pop()
        if self.heap:
            min_element = self.heap[0]
            self.heap[0] = last_element
            self._sift_down(0)
            return min_element
        return last_element


class MaxHeap(Heap):
    def __init__(self, array):
        mod_array = []
        print(array)
        for value in array:
            mod_array.append(value)
        super().__init__(mod_array)

    def extract_maximum(self):
        return super().pop()


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
