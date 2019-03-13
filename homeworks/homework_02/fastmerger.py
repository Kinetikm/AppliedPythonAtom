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
        output = []  # результат
        array = []  # массив для построения кучи
        for i, list_ in enumerate(list_of_lists):  # из каждого списка берем поседний(наибольший) элемент
            tmp = (list_.pop(), i)  # записываем кортеж (значение элемента, из какого списка был взят)
            array.append(tmp)
        heap = MaxHeap(array)  # строим кучу
        j = 0  # счетщик длинны исходного списка
        while j != k and h.heap:
            j += 1
            maximum, number = heap.extract_maximum()
            output.append(maximum)
            if list_of_lists[number]:
                tmp = (list_of_lists[number].pop(),
                       number)  # достаем элемент из того списка,из которого был только что записанный максимум
                heap.add(tmp)  # добавляем его в кучу
        return output
