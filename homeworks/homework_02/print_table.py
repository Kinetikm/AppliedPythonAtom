def print_table(table):

    col_width = [max(len(x) for x in col) for col in zip(*table)]

    table_length = sum(col_width) + 21

    print('-' * table_length)

    print("|  " + "  |  ".join("{:^{}}".format(x, col_width[i])
                           for i, x in enumerate(table[0])) + "  |")
    for i in range(1, len(table)):
        line = table[i]
        print("|  " + "  |  ".join("{:{}}".format(x, col_width[i])
                               for i, x in enumerate(line)) + "  |")

    print('-' * table_length)
