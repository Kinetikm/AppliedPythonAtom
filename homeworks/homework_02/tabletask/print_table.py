from homeworks.homework_02.tabletask import InvalidFormat


def print_table(data):
    if len(data) < 1:
        raise InvalidFormat
    for i in data:
        if len(i) != len(data[0]) or len(i) == 0:
            raise InvalidFormat
    lengths = []
    for i in range(len(data[0])):
        current_length = 0
        for j in data:
            current_length = max(len(str(j[i])), current_length)
        lengths.append(current_length)
    print("-" * (sum(lengths) + 5 * len(lengths) + 1))
    data_headers = data.pop(0)
    for i, j in enumerate(data_headers):
        print("|  {:^{width}}  ".format(j, width=lengths[i]), end='')
    print("|")
    for i in data:
        for j, k in enumerate(i):
            output = "|  {:" + (">" if j == len(i) - 1 else "<") + "{width}}  "
            print(output.format(k, width=lengths[j]), end='')
        print("|")
    print("-" * (sum(lengths) + 5 * len(lengths) + 1))
