

def calculate_determinant(list_of_lists):
    res = 0
    m = len(list_of_lists)
    for i in list_of_lists:
        n = len(i)
        if m != n:
           return None
    if n == 1:
       return list_of_lists[0][0]
    i = 0
    while i < len(list_of_lists):
        sup_matr = list_of_lists[::]
        sup_matr.pop(0)
        j = 0
        while j < len(sup_matr):
            sup_matr[j].pop(i)
            j += 1
        res += list_of_lists[0][i] * (1 ** i) * calculate_determinant(sup_matr)
        i += 1
    return res