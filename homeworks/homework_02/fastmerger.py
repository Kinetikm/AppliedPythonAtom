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

        heap = MaxHeap([])
        ans = []
        for lst in list_of_lists:
            if len(lst) > 0:
                heap.add((lst[-1], lst))  # tuple of max and list
        for i in range(k):
            if len(heap.heap) > 0:
                mx = heap.extract_maximum()
                ans.append(mx[1].pop())
                if len(mx[1]) > 0:
                    heap.add((mx[1][-1], mx[1]))
        return ans
