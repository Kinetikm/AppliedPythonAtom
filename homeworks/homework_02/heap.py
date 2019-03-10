#!/usr/bin/env python
# coding: utf-8

import heapq


class MaxHeapObj:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return comparator_d(self.value, other)

    def __eq__(self, other):
        return self.value == other

    def __str__(self):
        return str(self.value)

    def __getitem__(self, item):
        return self.value[item]


class Heap(object):

    def __init__(self, array):
        self._heap = array
        self.build_heap()

    def add(self, elem_with_priority):
        heapq.heappush(self._heap, elem_with_priority)

    def build_heap(self):
        heapq.heapify(self._heap)

    def __len__(self):
        return len(self._heap)


class MaxHeap(Heap):

    def __init__(self, array):
        modifiedArray = []
        for value in array:
            modifiedArray.append(MaxHeapObj(value))
        super().__init__(modifiedArray)

    def add(self, elem_with_priority):
        super().add(MaxHeapObj(elem_with_priority))

    def extract_maximum(self):
        return heapq.heappop(self._heap).value


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
