#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    def extract(elements):
        answer = []
        for element in elements:
            if isinstance(element, (list, dict, set)):
                answer += extract(element)
            else:
                answer.append(element)
        return answer

    if not isinstance(source_dict, dict):
        raise NotImplementedError
    new_dict = dict()
    for key, value in source_dict.items():
        if not isinstance(value, (list, dict, set)):
            new_dict[value] = key
        else:
            new_keys = []
            answer = extract(value)
            new_keys += answer
            for k in new_keys:
                new_dict[k] = key
    return new_dict
    raise NotImplementedError
