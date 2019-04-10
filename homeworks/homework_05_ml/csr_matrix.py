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
        if isinstance(init_matrix_representation, tuple) and len(
                init_matrix_representation) == 3:
            data = np.array(init_matrix_representation[2])
            delete_zeros_condition = (data != 0)
            row_indexes = np.array(init_matrix_representation[0])[
                delete_zeros_condition].astype(int)
            column_indexes = np.array(init_matrix_representation[1])[
                delete_zeros_condition].astype(int)
            data = data[delete_zeros_condition]
            self.shape = (
                np.amax(row_indexes) + 1, np.amax(column_indexes) + 1)
            self.A = np.array([])
            self.IA = np.zeros(self.shape[0] + 1).astype(int)
            self.JA = np.array([]).astype(int)
            for i in range(len(data)):
                self.set_item(row_indexes[i], column_indexes[i], data[i])
        elif isinstance(init_matrix_representation, np.ndarray):
            delete_zeros_condition = (init_matrix_representation != 0)
            self.shape = init_matrix_representation.shape
            row_indexes = np.where(delete_zeros_condition)[0].astype(int)
            column_indexes = np.where(delete_zeros_condition)[1].astype(int)
            data = init_matrix_representation[delete_zeros_condition]
            self.A = np.array([])
            self.IA = np.zeros(self.shape[0] + 1).astype(int)
            self.JA = np.array([]).astype(int)
            for i in range(len(data)):
                self.set_item(row_indexes[i], column_indexes[i], data[i])
        else:
            raise ValueError

    def get_item(self, i, j):
        """
        Return value in i-th row and j-th column.
        Be careful, i and j may have invalid values (-1 / bigger that matrix size / etc.).
        """
        if not self.__i_j_check__(i, j):
            raise IndexError
        if self.IA[i + 1] - self.IA[i] > 0:
            for k in range(self.IA[i], self.IA[i + 1]):
                if self.JA[k] == j:
                    return self.A[k]
        return 0

    def set_item(self, i, j, value):
        """
        Set the value to i-th row and j-th column.
        Be careful, i and j may have invalid values (-1 / bigger that matrix size / etc.).
        # """
        if not self.__i_j_check__(i, j):
            raise IndexError
        for k in range(self.IA[i], self.IA[i + 1] + 1):
            if len(self.JA) > k:
                if self.JA[k] == j:
                    self.A[k] = value
                    break
                elif self.JA[k] > j:
                    self.A = np.concatenate((self.A[:k], [value], self.A[k:]))
                    self.JA = np.concatenate((self.JA[:k], [j], self.JA[k:]))
                    self.IA[i + 1:] = self.IA[i + 1:] + 1
                    break
                elif i == self.IA[i + 1]:
                    self.A = np.concatenate(
                        (self.A[:k], [value], self.A[k:]))
                    self.JA = np.concatenate(
                        (self.JA[:k], [j], self.JA[k:]))
                    self.IA[i + 1:] = self.IA[i + 1:] + 1
                    break
            else:
                self.JA = np.append(self.JA, j)
                self.A = np.append(self.A, value)
                self.IA[i + 1:] = self.IA[i + 1:] + 1
                break

    def to_dense(self):
        """
        Return dense representation of matrix (2D np.array).
        """
        dense = np.zeros((self.shape[0], self.shape[1]))
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                dense[i, j] += self.get_item(i, j)
        return dense

    def __i_j_check__(self, i, j):
        return 0 <= i < self.shape[0] and 0 <= j < self.shape[1] and \
               isinstance(i, (int, np.int64, np.int32)) and \
               isinstance(j, (int, np.int64, np.int32))
