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
        h = MaxHeap([(l[-1], idx, len(l) - 1) for idx, l
                     in enumerate(list_of_lists) if len(l)])

        res = []
        for _ in range(k):
            try:
                fresh = h.extract_maximum()
            except IndexError:
                return res

            res.append(fresh[0])
            try:
                l = list_of_lists[fresh[1]]
                next_el = fresh[2] - 1
                if next_el < 0:
                    continue
                h.add((l[next_el], fresh[1], next_el))
            except IndexError:
                pass
        return res
