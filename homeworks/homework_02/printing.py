def print_table(converted_info):
    dict_for_col_max_len = dict.fromkeys([i for i in range(len(converted_info[0]))], -1)
    for x in converted_info:
        for i in dict_for_col_max_len.keys():
            if len(x[i]) > dict_for_col_max_len[i]:
                dict_for_col_max_len[i] = len(x[i])
    for x in converted_info:
        if (converted_info.index(x) != 0):
            for i in range(len(x)):
                if (i < len(x) - 1):
                    x[i] = '|  ' + x[i] + ' ' * (dict_for_col_max_len[i] - len(x[i])) + '  '
                else:
                    x[i] = '|  ' + ' ' * (dict_for_col_max_len[i] - len(x[i])) + x[i] + '  |'
        else:
            for i in range(len(x)):
                tab = (dict_for_col_max_len[i] - len(x[i])) // 2
                if (i < len(x) - 1):
                    if ((dict_for_col_max_len[i] - len(x[i])) % 2 == 0):
                        x[i] = '|  ' + ' ' * tab + x[i] + ' ' * tab + '  '
                    else:
                        x[i] = '|  ' + ' ' * tab + x[i] + ' ' * (tab + 1) + '  '
                else:
                    if ((dict_for_col_max_len[i] - len(x[i])) % 2 == 0):
                        x[i] = '|  ' + ' ' * tab + x[i] + ' ' * tab + '  |'
                    else:
                        x[i] = '|  ' + ' ' * tab + x[i] + ' ' * (tab + 1) + '  |'
    sum_length = 0
    for i in dict_for_col_max_len.keys():
        sum_length += dict_for_col_max_len[i]
    sum_length += (len(converted_info[0]) - 1) * 5 + 6
    line = '-' * sum_length
    converted_info.append(line)
    converted_info.insert(0, line)
    for row in converted_info:
        print(''.join(row))
