#!/usr/bin/env python
# coding: utf-8


class Heap:
    """Двоичная куча"""

    def __init__(self, array):
        self.heap = array[:]
        self.build_heap()

    def add(self, elem_with_priority) -> None:
        """Добавление элемента"""
        self.heap.append(elem_with_priority)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, i: int):
        """
        Восстановление упорядоченности
        Проталкивание вверх
        :param i: индекс элемента
        :return:
        """
        parent = (i - 1) // 2
        while i > 0 and comparator_d(self.heap[i], self.heap[parent]):
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def sift_down(self, i: int) -> None:
        """
        Восстановление упорядоченности
        Проталкивание вниз
        :param i: индекс элемента
        """
        heap_size = len(self.heap)
        while True:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            largest = i

            if left_child < heap_size and \
                    comparator_d(self.heap[left_child], self.heap[largest]):
                largest = left_child

            if right_child < heap_size and \
                    comparator_d(self.heap[right_child], self.heap[largest]):
                largest = right_child

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

    def build_heap(self) -> None:
        """Построение"""
        for i in range(len(self.heap) // 2, -1, -1):
            self.sift_down(i)


class MaxHeap(Heap):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def extract_maximum(self):
        """
        Извлечение максимального элемента с удалением - O(log N)
        :return: максимальный элемент (корень)
        """
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        tmp = self.heap.pop()
        self.sift_down(0)
        return tmp


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
