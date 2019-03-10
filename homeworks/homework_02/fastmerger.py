#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap
import copy


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k) -> list:
        '''
        принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        '''
        resultList = []
        heap = MaxHeap([])
        for oneList in list_of_lists:
            if len(oneList) > 0:
                heap.add((oneList[-1], oneList))
        for i in range(k):
            if len(heap) > 0:
                extracted = heap.extract_maximum()
                resultList.append(extracted[1].pop())
                if len(extracted[1]) > 0:
                    heap.add((extracted[1][-1], extracted[1]))
        return resultList
