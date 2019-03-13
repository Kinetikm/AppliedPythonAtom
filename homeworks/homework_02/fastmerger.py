#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_02.heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        '''
        принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        '''

        merged_list = []
        result_list = []
        ind = 0
        for val in list_of_lists:
            if val != []:
                try:
                    merged_list.append((val.pop(), ind))
                except AttributeError:
                    merged_list.append((list_of_lists[ind], 'int'))
                finally:
                    ind += 1
        h = MaxHeap(merged_list)
        while (k != 0) and (len(h.data) > 0):
            val, ind = h.extract_maximum()
            result_list.append(val)
            if ind != 'int' and list_of_lists[ind]:
                h.add((list_of_lists[ind].pop(), ind))
            k -= 1
        return result_list
