def printing_the_file(file, form, enc):
    MaxStr = []
    if form == 'json':
        Lst = preparing_json(file, enc)
    else:
        Lst = preparing_tsv(file, enc)
    for i in range(len(Lst[0])):
        MaxLen = 0
        for j in range(len(Lst)):
            if len(str(Lst[j][i])) > MaxLen:
                MaxLen = len(str(Lst[j][i]))
        MaxStr.append(MaxLen)
    TopLen = sum(MaxStr) + 6 + 5 * (len(Lst[0]) - 1)
    print("-" * TopLen)
    print("|", end="")
    for i in range(len(Lst[0])):
        Spcs = MaxStr[i]
        print("  " + Lst[0][i].center(Spcs) + "  ", end="")
        print("|", end="")
    print()
    for i in range(1, len(Lst)):
        print("|", end="")
        for j in range(len(Lst[i]) - 1):
            Spcs = MaxStr[j]
            print(("  " + Lst[i][j]).ljust(Spcs + 2) + "  ", end="")
            print("|", end="")
        Spcs = MaxStr[len(Lst[i]) - 1]
        print("  " + str(Lst[i][len(Lst[i]) - 1]).rjust(Spcs) + "  ", end="")
        print("|")
    print("-" * TopLen)
