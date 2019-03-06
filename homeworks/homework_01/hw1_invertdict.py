def invert_dict(d):
    result_d = {}
    for key in d.keys():
        new_key = d[key]
        new_value = key
        if type(new_key) == str or type(new_key) == float or type(new_key) == int:
            new_key = [new_key]
        else:
            new_key = list(new_key)
        for new_new_key in new_key:
            if new_new_key in result_d:
                result_d[new_new_key].append(new_value)
            else:
                result_d[new_new_key] = [new_value]
    return result_d
