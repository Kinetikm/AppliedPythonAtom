def print_table(data):
    if len(data) == 0:
        raise ValueError
    for line in data:
        if len(line) == 0 or len(line) != len(data[0]):
            raise ValueError
    columns_size = []
    for i in range(len(data[0])):
        pseudo_max = 0
        for j in data:
            pseudo_max = max(len(str(j[i])), pseudo_max)
        columns_size.append(pseudo_max)
    super_print(columns_size)
    hat = data.pop(0)
    for i, j in enumerate(hat):
        print("|  {:^{width}}  ".format(j, width=columns_size[i]), end='')
    print("|")
    for i in data:
        for j, k in enumerate(i):
            output = "|  {:" + (">" if j == len(i) - 1 else "<") + "{width}}  "
            print(output.format(k, width=columns_size[j]), end='')
        print("|")
    super_print(columns_size)


def super_print(x):
    print("-" * (sum(x) + 5 * len(x) + 1))
