def convert(data):
    if data is not None:
        col_format = []
        u = 0
        for i in range(0, len(data[u])):
            line1 = []
            col = []
            for j in range(0, len(data)):
                line1.append(str(data[j][i]))

            u = u + 1
            max_len = len(max(line1, key=len))
            col = [line.ljust(max_len) for line in line1]
            col_format.append(col)

        data_itog = []
        u = 0
        for j in range(len(col_format[u])):
            data_line = ""
            for i in range(len(col_format)):
                if j == 0:
                    len1 = len(col_format[i][j])
                    str0 = col_format[i][j].strip(' ')
                    str1 = str0.center(len1)
                    col_format[i][j] = str1
                data_line = data_line + "  |  " + col_format[i][j]
            data_line = data_line + "  |"
            data_line1 = data_line.strip(' ')
            data_itog.append(data_line1)
            u = u + 1

        size = len(data_itog[0])
        str_head = ""
        for i in range(0, size):
            str_head = str_head + '-'

        data_itog1 = []
        data_itog1.append(str_head)
        # print(str_head)
        for i in range(len(data_itog)):
            data_itog1.append(data_itog[i])
            # print(data_itog[i])
        data_itog1.append(str_head)
        # print(str_head)
        return data_itog1
    else:
        print('формат json не валиден')
        return None
