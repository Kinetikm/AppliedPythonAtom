#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    new_dict = {}
    def go_deeper(obj):
        if not isinstance(obj, (set, tuple, list)):
            str_value = str(obj)
            if str_value in new_dict:
                if type(new_dict[str_value]) != list:
                    templist = []
                    templist.append(new_dict[str_value])
                    new_dict[str_value] = templist
                new_dict[str_value].append(k)
            else:
                new_dict[str_value] = k
            return None
        else:
            for elem in obj:
                go_deeper(elem)
    for k in source_dict:
        go_deeper(source_dict[k])
    print(new_dict)
    return new_dict


dic = invert_dict({
    'one': 1,
    'two': 2,
    'three': 3,
    'lie' : False,
    'truth' : True,
    'name': 'Oleg',
    'father': 'Oleg',
    'TUPLE' : (888, 888, [111, 111, [404, ('STOP', True)]], 888)
})
