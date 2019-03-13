def data_convert(data):
    if data is not None:
        transp_to_column = []
        counter = 0
        for i in range(0, len(data[counter])):
            line1 = []
            column = []
            for j in range(0, len(data)):
                line1.append(str(data[j][i]))

            counter = counter + 1
            max_len = len(max(line1, key=len))
            column = [line.ljust(max_len) for line in line1]
            transp_to_column.append(column)

        data_result_buf = []
        counter = 0
        for j in range(len(transp_to_column[counter])):
            line_in_data = ""
            for i in range(len(transp_to_column)):
                if j == 0:
                    fst_len = len(transp_to_column[i][j])
                    str0 = transp_to_column[i][j].strip(' ')
                    str1 = str0.center(fst_len)
                    transp_to_column[i][j] = str1
                line_in_data = line_in_data + "  |  " + transp_to_column[i][j]
            line_in_data = line_in_data + "  |"
            data_line1 = line_in_data.strip(' ')
            data_result_buf.append(data_line1)
            counter = counter + 1

        size = len(data_result_buf[0])
        str_head = ""
        for i in range(0, size):
            str_head = str_head + '-'

        data_result = []
        data_result.append(str_head)
        # print(str_head)
        for i in range(len(data_result_buf)):
            data_result.append(data_result_buf[i])
            # print(data_result_buf[i])
        data_result.append(str_head)
        return data_result
    else:
        print('формат json не валиден')
        return None
