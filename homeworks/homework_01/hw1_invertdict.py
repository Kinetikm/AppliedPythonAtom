#!/usr/bin/env python
# coding: utf-8


def deploy_element(el, tmp):
    if (type(el) != list) and (type(el) != tuple) and (type(el) != set):
        tmp.append(el)
    else:
        for new_el in el:
            deploy_element(new_el, tmp)


def is_list(el):
    if (type(el) == int) or (type(el) == float) or (type(el) == str):
        return False
    else:
        return True


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    if type(source_dict) != dict:
        return None
    new_dict = dict()
    for key, value in source_dict.items():
        tmp = list()
        deploy_element(value, tmp)
        for new_key in tmp:
            if new_key in new_dict:
                if is_list(new_dict[new_key]):
                    new_dict[new_key].append(key)
                else:
                    tmp_list = [new_dict[new_key], key]
                    new_dict[new_key] = tmp_list
            else:
                new_dict[new_key] = key
    return new_dict
    raise NotImplementedError
