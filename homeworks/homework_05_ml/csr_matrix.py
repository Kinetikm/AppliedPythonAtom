#!/usr/bin/env python
# coding: utf-8


import numpy as np


class CSRMatrix:
    """
    CSR (2D) matrix.
    Here you can read how CSR sparse matrix works: https://en.wikipedia.org/wiki/Sparse_matrix
    """
    def __init__(self, init_matrix_representation):

        imr = init_matrix_representation
        self.a = np.array([], dtype=int)
        self.ia = np.array([0], dtype=int)
        self.ja = np.array([], dtype=int)
        if isinstance(imr, tuple) and len(imr) == 3:
            indx = np.lexsort((imr[1], imr[0]))
            self.a = \
                np.append(self.a, [imr[2][i] for i in indx if imr[2][i] != 0])
            self.ja = \
                np.append(self.ja, [imr[1][i] for i in indx if imr[2][i] != 0])
            self.ia = np.zeros(max(imr[0]) + 2, dtype=int)
            for i in [imr[0][i] for i in indx if imr[2][i] != 0]:
                self.ia[i + 1:] += 1
        elif isinstance(imr, np.ndarray):
            self.a = np.append(self.a, imr[np.nonzero(imr)])
            self.ja = np.append(self.ja, np.nonzero(imr)[1])
            total_elems = 0
            for i in np.arange(imr.shape[0]):
                total_elems += imr[i, :][np.nonzero(imr[i, :])].shape[0]
                self.ia = np.append(self.ia, total_elems)
        else:
            raise ValueError

    def get_item(self, i, j):
        """
        Return value in i-th row and j-th column.
        Be careful, i and j may have invalid values (-1 / bigger that matrix size / etc.).
        """
        if not isinstance(i, (int, float)):
            return None
        if not isinstance(j, (int, float)):
            return None
        if i < 0 or j < 0:
            return None
        if i > self.ia.shape[0] - 1 or j > np.amax(self.ja):
            return None
        item = 0
        for k in np.arange(self.ia[i], self.ia[i+1]):
            if self.ja[k] == j:
                item = self.a[int(k)]
                break
        return item

    def set_item(self, i, j, value):
        """
        Set the value to i-th row and j-th column.
        Be careful, i and j may have invalid values (-1 / bigger that matrix size / etc.).
        """
        if not isinstance(i, (int, float)):
            return None
        if not isinstance(j, (int, float)):
            return None
        if i < 0 or j < 0:
            return None
        is_zero = True
        for k in np.arange(self.ia[i], self.ia[i+1]):
            if self.ja[int(k)] == j:
                if value != 0:
                    self.a[int(k)] = value
                else:
                    self.a = np.delete(self.a, self.a[int(k)])
                    self.ja = np.delete(self.ja, self.ja[int(k)])
                    self.ia[i + 1:] -= 1
                is_zero = False
                break
        if not is_zero:
            return
        LB = self.ia[i]
        RB = self.ia[i + 1]
        if RB == LB:
            self.ja = np.insert(self.ja, LB, j)
            self.a = np.insert(self.a, LB, value)
            self.ia[i + 1:] += 1
        else:
            for k in range(LB, RB):
                if (j < self.ja[k] or k == np.arange(LB, RB)[-1]):
                    self.ja = np.insert(self.ja, k + 1, j)
                    self.a = np.insert(self.a, k + 1, value)
                    self.ia[i + 1:] += 1
        return

    def to_dense(self):
        """
        Return dense representation of matrix (2D np.array).
        """
        dense_mx = np.zeros([self.ia.shape[0] - 1, np.amax(self.ja) + 1])
        for i in np.arange(self.ia.shape[0] - 1):
            for j in np.arange(self.ia[i], self.ia[i + 1]):
                dense_mx[i, self.ja[j]] = self.a[j]
        return dense_mx
