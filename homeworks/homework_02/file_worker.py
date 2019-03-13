def print_table(data):
    max_lengths = []
    if len(data) > 1:
        for i in range(len(data[0]) - 1):
            comparing = []
            for j in range(1, len(data)):
                comparing.append(data[j][i])
            max_lengths.append(len(max(comparing,
                                       key=lambda el: 1 if type(el) == int
                                       else len(el))))
        max_lengths.append(len(data[0][-1]))
    else:
        for item in data[0]:
            max_lengths.append(len(item))
    print('-' * (sum(max_lengths) + 5 * len(max_lengths) + 1))
    for i in range(len(data)):
        print('|', end='')
        for j in range(len(data[i])):
            if i == 0:
                print(' ' * (((max_lengths[j] - len(str(data[i][j]))) // 2)
                             + 1)
                      , data[i][j],
                      ' ' * ((max_lengths[j] - len(str(data[i][j]))) // 2)
                      , '|', end='')
            else:
                if len(str(data[i][j])) == 1:
                    print(' ' * len(data[0][j]), data[i][j], ' |', end='')
                else:
                    print(' ', data[i][j], ' ' * (max_lengths[j] -
                                                  len(str(data[i][j]))),
                          '|', end='')
        print()
    print('-' * (sum(max_lengths) + 5 * len(max_lengths) + 1))
    return
