#!/usr/bin/env python
# coding: utf-8


import numpy as np


class CSRMatrix:
    """
    CSR (2D) matrix.
    Here you can read how CSR sparse matrix works: https://en.wikipedia.org/wiki/Sparse_matrix
    """

    def __init__(self, init_matrix_representation):
        """
        :param init_matrix_representation: can be usual dense matrix
        or
        (row_ind, col, data) tuple with np.arrays,
            where data, row_ind and col_ind satisfy the relationship:
            a[row_ind[k], col_ind[k]] = data[k]
        """
        self.A = np.array([])
        self.JA = np.array([])

        if isinstance(init_matrix_representation, tuple) and len(init_matrix_representation) == 3:
            self.IA = np.zeros(int(np.max(init_matrix_representation[0])) + 1)
            self.A = np.append(self.A, init_matrix_representation[2])
            self.JA = np.append(self.JA, init_matrix_representation[1])
            for i in init_matrix_representation[0]:
                self.IA[init_matrix_representation[0][i] + 1:] += 1
        elif isinstance(init_matrix_representation, np.ndarray):
            self.IA = np.zeros(int(init_matrix_representation.shape[0]) + 1)
            for i in np.arange(0, init_matrix_representation.shape[0]):
                self.IA[i + 1] = self.IA[i]
                for j in np.arange(0, init_matrix_representation.shape[1]):
                    if init_matrix_representation[i][j] and init_matrix_representation[i][j] != 0:
                        self.A = np.append(self.A, init_matrix_representation[i][j])
                        self.JA = np.append(self.JA, j)
                        self.IA[i + 1] += 1
        else:
            raise ValueError

    def get_item(self, i, j):
        """
        Return value in i-th row and j-th column.
        Be careful, i and j may have invalid values (-1 / bigger that matrix size / etc.).
        """
        if i > len(self.IA) - 1 or j > np.max(self.JA):
            return None
        if i < 0 or j < 0:
            return None
        for k in np.arange(self.IA[i], self.IA[i + 1]):
            k1 = int(k)
            if self.JA[k1] == j:
                return self.A[k1]
        return 0

    def set_item(self, i, j, value):
        """
        Set the value to i-th row and j-th column.
        Be careful, i and j may have invalid values (-1 / bigger that matrix size / etc.).
        """
        if i < 0 or j < 0:
            raise KeyError
        if value == 0:
            return
        if not self.A:  # матрица пуста
            self.A = np.array([value])  # вставляем
            self.IA[i + 1:] += 1
            self.JA[0] = j
        else:  # матрица не пуста
            j1 = int(self.IA[i] - 1)
            # есть ли в (i, j) элемент ?
            for ind in np.arange(self.self.IA[i], self.self.IA[i + 1]):
                ind = int(ind)
                if self.JA[ind] == j:  # в (i, j) есть элемент
                    self.A[ind] = value  # вставляем
                elif self.JA[ind] > j:
                    # ячейка (i, j) пуста
                    break
                j1 = ind
            #  вставляем.
            self.A = np.insert(self.A, j1 + 1, value)
            self.IA[i + 1:] += 1
            self.JA = np.insert(self.JA, j1 + 1, j)

    def to_dense(self):
        """
        Return dense representation of matrix (2D np.array).
        """
        row = int(self.IA.shape[0] - 1)
        col = int(np.amax(self.JA) + 1)
        result = np.zeros([row, col])
        for i in np.arange(row):
            for j in np.arange(self.IA[int(i)], self.IA[int(i) + 1]):
                result[int(i), int(self.JA[int(j)])] = self.A[int(j)]
        return result
