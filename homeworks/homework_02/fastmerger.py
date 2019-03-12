#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k: int,
                      full_list: list = None, index: int = 0):
        """
        Принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию

        :param list_of_lists: список отсортированных непоубыванию списков
        :param k: ожидаемая длина конечного списка
        :param full_list: подготовленный список
        :param index: индекс элемента получаемого из heap
        :return: список длиной k, отсортированный по убыванию
        """
        if not full_list:
            full_list = []
            for list_item in list_of_lists:
                full_list += [(item, 0) for item in list_item]

        # отдавать не больше чем есть
        if k > len(full_list):
            k = len(full_list)

        h = MaxHeap(full_list)
        first_k = []
        for i in range(k):
            first_k.append(h.extract_maximum()[index])

        return first_k
