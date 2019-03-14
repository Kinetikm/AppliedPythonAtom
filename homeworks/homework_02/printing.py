def print_file(list_of_lists: list):
    if len(list_of_lists) < 1:
        raise ValueError("Формат не валиден")
    for i in list_of_lists:
        if len(i) != len(list_of_lists[0]) or len(i) == 0:
            raise ValueError("Формат не валиден")
    lengths = list()
    for i in range(len(list_of_lists[0])):
        current_length = 0
        for j in list_of_lists:
            current_length = max(len(str(j[i])), current_length)
        lengths.append(current_length)
    print("-" * (sum(lengths) + 5 * len(lengths) + 1))
    data_headers = list_of_lists.pop(0)
    for i, j in enumerate(data_headers):
        print("|  {:^{width}}  ".format(j, width=lengths[i]), end='')
    print("|")
    for i in list_of_lists:
        for j, k in enumerate(i):
            output = "|  {:" + (">" if j == len(i) - 1 else "<") + "{width}}  "
            print(output.format(k, width=lengths[j]), end='')
        print("|")
    print("-" * (sum(lengths) + 5 * len(lengths) + 1))