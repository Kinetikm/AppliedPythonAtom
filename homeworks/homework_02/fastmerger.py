#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        '''
        принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        '''
        max_list = []
        _list = []

        for i in range(len(list_of_lists)):
            if (len(list_of_lists[i]) > 0):
                _list.append((list_of_lists[i].pop(), i))

        heap = MaxHeap(_list)

        while (k > 0):
            if (len(heap._heap) == 0):
                break
            max_list.append(heap.extract_maximum())
            elem, list_index = max_list[-1]
            if (len(list_of_lists[list_index]) > 0):
                heap.add((list_of_lists[list_index].pop(), list_index))
            k -= 1

        return [elem[0] for elem in max_list]
