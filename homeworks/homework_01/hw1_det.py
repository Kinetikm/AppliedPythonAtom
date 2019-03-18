

def calculate_determinant(list_of_lists):
    if len(list_of_lists) == 0:
        return None
    for l in list_of_lists:
        if len(l) != len(list_of_lists):
            return None
    sup_matr = list_of_lists[::]
    i = 0
    while i < len(sup_matr):
        if sup_matr[i][i] == 0:
            j = i + 1
            while j < len(sup_matr):
                if sup_matr[j][i] != 0:
                    tmp = sup_matr[i]
                    sup_matr[i] = sup_matr[j]
                    sup_matr[j] = tmp
                    break
                j += 1
        k = i + 1
        while k < len(sup_matr):
            x = sup_matr[k][i] / sup_matr[i][i]
            m = i + 1
            while m < len(sup_matr):
                sup_matr[k][m] -= sup_matr[i][m] * x
                m += 1
            k += 1
        i += 1
    res = 1
    i = 0
    while i < len(sup_matr):
        res *= sup_matr[i][i]
        i += 1
    return res
