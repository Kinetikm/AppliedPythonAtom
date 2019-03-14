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
        if list_of_lists is None or len(list_of_lists) == 0:
            return []
        max_heap = MaxHeap(list_of_lists)
        arr = [max_heap.extract_maximum() for i in range(k)]
        return [x for x in arr if x is not None]
