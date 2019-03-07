#!/usr/bin/env python
# coding: utf-8

c_types = {list, tuple, set}


def unwrap_list(list1, list2):
    for i in list1:
        if type(i) in c_types:
            unwrap_list(i, list2)
        else:
            list2.append(i)


def invert_dict(source_dict):
    if type(source_dict) != dict:
        return (None)
    print(source_dict)
    inverted_dict = {}
    for key in source_dict.keys():
        val = source_dict.get(key)
        if (type(val) not in c_types):
            if (inverted_dict.get(val) is None):
                inverted_dict[val] = key
            elif(type(inverted_dict.get(val)) not in c_types):
                inverted_dict[val] = [inverted_dict.get(val), key]
            else:
                inverted_dict.get(val).append(key)
            print("Это inv: ", inverted_dict)
        else:
            unval = []
            for el in val:
                print("Это эл, ", el, type(el))
                if type(el) in c_types:
                    unwrap_list(el, unval)
                    print("это unval: ", unval)
                    for el in unval:
                        if (inverted_dict.get(el) is None):
                            inverted_dict[el] = key
                        elif(type(inverted_dict.get(el)) not in c_types):
                            inverted_dict[el] = [inverted_dict.get(el), key]
                        else:
                            inverted_dict.get(el).append(key)
                else:
                    print("inv el", inverted_dict.get(el))
                    print(val, el)
                    if inverted_dict.get(el) is None:
                        inverted_dict[el] = key
                    elif(type(inverted_dict.get(el)) not in c_types):
                        inverted_dict[el] = [inverted_dict.get(el), key]
                    else:
                        inverted_dict.get(el).append(key)
                    print("inv el", inverted_dict.get(el))

            print("Это inv: ", inverted_dict)

    print(inverted_dict)
    return(inverted_dict)
