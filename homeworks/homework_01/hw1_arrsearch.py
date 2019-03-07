#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    mas = input_list
    sum = n
    mas.sort()
    levyi = 0
    pravyi = len(mas) - 1
    if len(mas) == 0 or len(mas) == 1:
        return None
    while levyi != pravyi:
        g = mas[levyi] + mas[pravyi]
        if g < sum:
            levyi += 1
        elif g > sum:
            pravyi -= 1
        else:
            return levyi, pravyi
            break
    if levyi == pravyi and g != mas[levyi] + mas[pravyi]:
        return None
