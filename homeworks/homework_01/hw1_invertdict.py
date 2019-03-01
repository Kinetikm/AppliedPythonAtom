#!/usr/bin/env python
# coding: utf-8


def simplificate(lst):
    simple_list = list()
    queue = list()
    queue.append(lst)
    map_checker = {}
    while len(queue) > 0:
        next_element = queue[-1]
        queue.pop()
        try:
            map_checker[next_element] = 1
            simple_list.append(next_element)
        except TypeError:
            for i in next_element:
                queue.append(i)
    return simple_list


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    answer_map = {}
    for key in source_dict:
        for i in simplificate(source_dict[key]):
            answer_map[i] = []
    for key in source_dict:
        for i in simplificate(source_dict[key]):
            answer_map[i].append(key)
    for key in answer_map:
        try:
            if len(answer_map[key]) == 1:
                answer_map[key] = answer_map[key][0]
        except KeyError:
            continue
    return answer_map
