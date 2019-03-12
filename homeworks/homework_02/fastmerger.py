#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k: int):
        """
        Принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        O(N + k * log k)
        """
        # наибольший элемент списка, номер списка, номер следующего элемента
        h = MaxHeap(
            [
                (item[-1], index, len(item) - 2)
                for index, item in enumerate(list_of_lists)
                if len(item) > 0
            ]
        )

        first_k = []
        for _ in range(k):
            # забираем из кучи максимальный элемент
            if h.heap:
                max_item = h.extract_maximum()
            else:
                return first_k
            first_k.append(max_item[0])

            # если список не опустел, добавляем следующий элемент в кучу
            if max_item[2] > -1:
                h.add(
                    (
                        list_of_lists[max_item[1]][max_item[2]],
                        max_item[1], max_item[2] - 1
                    )
                )

        return first_k
