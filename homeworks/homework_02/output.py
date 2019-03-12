def output(lists):
    n = len(lists[0])
    for spis in lists:
        if len(spis) != n:
            raise AssertionError
    max = list()
    for i in range(n):
        max.append(0)
        for spisok in lists:
            if len(str(spisok[i])) > max[i]:
                max[i] = len(str(spisok[i]))
    all = 0
    for k in max:
        all += k
    print("-" * (5 * n + 1 + all), end="\n")

    for j in range(n):
        print("|  ", end="")
        f = (max[j] - len(str(lists[0][j]))) // 2
        s = (max[j] - len(str(lists[0][j]))) % 2
        print(" " * f + str(lists[0][j]) + " " * (f + s), end="  ")
    print("|", end="\n")

    for spis in lists[1:]:
        for j in range(n):
            print("|  ", end="")
            st = str(spis[j])
            if j == n - 1:
                print(" " * (max[j] - len(str(spis[j]))) + st, end="")
            else:
                print(st + " " * (max[j] - len(str(spis[j])) + 2), end="")
        print("  |", end="\n")

    print("-" * (5 * n + 1 + all), end="\n")
