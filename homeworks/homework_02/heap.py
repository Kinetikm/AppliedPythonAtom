#!/usr/bin/env python
# coding: utf-8


class MaxHeapObj:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return comparator_d(self.value, other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    def __getitem__(self, item):
        return self.value[item]


class Heap(object):

    def __init__(self, array):
        self._heap = array
        self.build_heap()

    def add(self, elem_with_priority):
        self._heap.append(elem_with_priority)
        self._sift_down(len(self) - 1)

    def build_heap(self):
        for i in reversed(range(len(self)//2)):
            self._sift_up(i)

    def pop(self):
        lastElement = self._heap.pop()
        if self._heap:
            minElement = self._heap[0]
            self._heap[0] = lastElement
            self._sift_up(0)
            return minElement
        return lastElement

    def __len__(self):
        return len(self._heap)

    def _sift_down(self, position):
        while position > 0:
            parent = (position - 1) // 2
            if self._heap[parent] < self._heap[position]:
                return
            self._heap[parent], self._heap[position] = \
                self._heap[position], self._heap[parent]
            position = parent

    def _sift_up(self, position):
        left = 2 * position + 1
        right = 2 * position + 2
        lowest = position
        if left < len(self) and self._heap[left] < self._heap[lowest]:
            lowest = left
        if right < len(self) and self._heap[right] < self._heap[lowest]:
            lowest = right
        if lowest != position:
            self._heap[lowest], self._heap[position] = \
                self._heap[position], self._heap[lowest]
            self._sift_up(lowest)


class MaxHeap(Heap):

    def __init__(self, array):
        modifiedArray = []
        for value in array:
            modifiedArray.append(MaxHeapObj(value))
        super().__init__(modifiedArray)

    def add(self, elem_with_priority):
        super().add(MaxHeapObj(elem_with_priority))

    def extract_maximum(self):
        return super().pop().value


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
