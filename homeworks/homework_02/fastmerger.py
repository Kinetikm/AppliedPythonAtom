#!/usr/bin/env python
# coding: utf-8

from heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        help_list = []
        result_list = []  # итоговый список 
        i = 0
        # заполним список кортежами следующего вида:
        # (макимальный элемент i-го "подсписка", i)
        while i < len(list_of_lists):  # o(N)
            if list_of_lists[i]:
                help_list.append((list_of_lists[i][-1], i))
            i += 1
        # переделаем его в кучу
        h = MaxHeap(help_list)  # o(N)
        i = 0
        while i < k: # o(k)
            # извлекаем максимум из кучи
            m = h.extract_maximum()  # o(log(N))
            # добавляем 0-ый элемент кортежа к итоговому списку
            result_list.append(m[0])

            # 1-ый элемент кортежа является номер необходимого "подспиcка"

            # удаляем последний элемент из найденного "подсписка"
            list_of_lists[m[1]].pop()
            # добавляем в кучу последний элемент из найденного "подсписка"
            if list_of_lists[m[1]]:
                h.add((list_of_lists[m[1]][-1], m[1]))  # o(log(N))
            i += 1
        return result_list
        raise NotImplementedError
