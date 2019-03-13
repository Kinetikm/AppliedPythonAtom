#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap
import copy


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        '''
        принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        '''
        output = []  # результат
        array = []  # массив для построения кучи
        copy_list = copy.deepcopy(list_of_lists)
        # из каждого списка берем поседний(наибольший) элемент
        for i, list_ in enumerate(copy_list):
            # записываем кортеж
            # (значение элемента, из какого списка был взят)
            if list_:
                tmp = (list_.pop(), i)
                array.append(tmp)
        heap_ = MaxHeap(array)  # строим кучу
        j = 0  # счетщик длинны исходного списка
        while j != k and heap_.heap:
            j += 1
            maximum, number = heap_.extract_maximum()
            output.append(maximum)
            # достаем элемент из того списка,
            # из которого был только что записанный максимум
            if copy_list[number]:
                tmp = (list_of_lists[number].pop(), number)
                heap_.add(tmp)  # добавляем его в кучу
        return output
