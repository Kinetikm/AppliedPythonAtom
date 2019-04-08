#!/usr/bin/env python
# coding: utf-8

import numpy as np


class CSRMatrix:
    def __init__(self, init_matrix):
        self.A = np.array([], dtype=int)
        self.IA = np.array([], dtype=int)
        self.JA = np.array([], dtype=int)
        if isinstance(init_matrix, tuple) and len(init_matrix) == 3:
            self.IA = np.array([0])
            init_0 = np.array(init_matrix[0])
            init_1 = np.array(init_matrix[1])
            init_2 = np.array(init_matrix[2])
            nonzero_indices = init_2.nonzero()
            self.A = np.append(self.A, init_2[nonzero_indices])
            self.JA = np.append(self.JA, init_1[nonzero_indices])
            _, cnt = np.unique(init_0[nonzero_indices], return_counts=True)
            self.IA = np.append(self.IA, cnt.cumsum(dtype=int))
            self.col_num = np.unique(init_1).size  # количество строк итак сможем вычислить по IA
        elif isinstance(init_matrix, np.ndarray):
            self.A = init_matrix[init_matrix.nonzero()]
            ia_list = np.array([int(0)])
            for row in init_matrix:
                self.JA = np.append(self.JA, row.nonzero())
                try:
                    ia_list = np.append(ia_list, np.unique(row, return_counts=True)[1][1])
                except IndexError:  # если встречается полностью нулевая строка, она игнорируется
                    ia_list = np.append(ia_list, int(ia_list[-1]))
                    continue
            self.IA = ia_list.cumsum(dtype=int)
            self.col_num = init_matrix.shape[1]
        else:
            raise ValueError

    def get_item(self, i, j):
        if 0 <= i < self.IA.size and 0 <= j <= self.col_num:
            for k in range(self.IA[i], self.IA[i + 1]):
                if self.JA[k] == j:
                    return self.A[k]
        else:
            raise IndexError
        return 0

    def set_item(self, i, j, value):
        if not(0 <= i < self.IA.size and 0 <= j < self.col_num):
            raise IndexError

        for k in range(self.IA[i], self.IA[i + 1]):
            if self.JA[k] == j:
                self.A[k] = value
                return

        if self.IA[i + 1] - self.IA[i]:
            for k in range(self.IA[i], self.IA[i + 1]):
                if j < self.JA[k]:
                    self.A = np.insert(self.A, k + 1, value)
                    self.JA = np.insert(self.JA, k + 1, j)
                    self.IA[i + 1:] += 1
                    return

        self.A = np.insert(self.A, self.IA[i + 1], value)
        self.JA = np.insert(self.JA, self.IA[i + 1], j)
        self.IA[i + 1:] += 1
        return

    def to_dense(self):
        res = np.zeros([self.IA.size - 1, self.col_num])
        for i in range(self.IA.size - 1):
            for j in range(self.IA[i], self.IA[i + 1]):
                k = self.JA[j]
                res[i][k] = self.A[j]
        return res
