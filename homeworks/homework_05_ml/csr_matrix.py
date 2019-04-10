#!/usr/bin/env python
# coding: utf-8


import numpy as np


class CSRMatrix:

    def __init__(self, init_matrix):
        self.a = np.zeros(1)
        self.ja = np.zeros(1)
        if isinstance(init_matrix, tuple) and len(init_matrix) == 3:
            help_list = []
            for k in np.arange(0, len(init_matrix[2])):
                help_list.append((init_matrix[0][k], init_matrix[1][k],
                                  init_matrix[2][k]))
            help_list = sorted(help_list, key=lambda x: x[0])
            init_matrix = ([], [], [])
            for k in np.arange(0, len(help_list)):
                init_matrix[0].append(help_list[k][0])
                init_matrix[1].append(help_list[k][1])
                init_matrix[2].append(help_list[k][2])
            self.ia = np.zeros(np.max(init_matrix[0])+2)
            for k in np.arange(0, len(init_matrix[2])):
                if init_matrix[2][k]:
                    if not self.a[0]:
                        self.a[0] = init_matrix[2][k]
                        self.ja[0] = init_matrix[1][k]
                    else:
                        self.a = np.append(self.a, init_matrix[2][k])
                        self.ja = np.append(self.ja, init_matrix[1][k])
                    self.ia[init_matrix[0][k]+1:] += 1

        elif isinstance(init_matrix, np.ndarray):
            self.ia = np.zeros(init_matrix.shape[0]+1)
            for i in np.arange(0, init_matrix.shape[0]):
                self.ia[i+1] = self.ia[i]
                for j in np.arange(0, init_matrix.shape[1]):
                    if init_matrix[i][j]:
                        if not self.a[0]:
                            self.a[0] = init_matrix[i][j]
                            self.ja[0] = j
                        else:
                            self.a = np.append(self.a, init_matrix[i][j])
                            self.ja = np.append(self.ja, j)
                        self.ia[i+1] += 1
        else:
            raise ValueError

    def get_item(self, i, j):
        if i > len(self.ia)-1 or j > np.max(self.ja):
            return None
        if i < 0 or j < 0:
            return None
        for index in np.arange(self.ia[i], self.ia[i+1]):
            index = int(index)
            if self.ja[index] == j:
                return self.a[index]
        return 0

    def set_item(self, i, j, value):
        if self.a[0] == 0:  # в нынешней матрице нет ненулевых эл-ов
            self.a[0] = value  # изменяем значение
            # в случае изменения на ненулевое значение изменяем ia и ja
            if value != 0:
                self.ia[i+1:] += 1
                self.ja[0] = j
        else:  # в ином случае
            j_help = int(self.ia[i] - 1)
            # определяем, является ли нулевым эл-т (i, j)
            for index in np.arange(self.ia[i], self.ia[i+1]):
                index = int(index)
                if self.ja[index] == j:  # эл-т (i, j) ненулевой
                    self.a[index] = value  # изменяем значение
                    # в случае изменения на нулевое значение изменяем ia и ja
                    if value == 0:
                        self.ia[i+1:] -= 1
                        self.ja = np.delete(self.ja, j_help+1, j)
                    raise
                elif self.ja[index] > j:
                    # эл-т (i, j) не был обнаружен => он является нулевым
                    break
                j_help = index
            # в случае изменения на ненулевое значение изменяем a, ia и ja
            if value != 0:
                self.a = np.insert(self.a, j_help+1, value)
                self.ia[i+1:] += 1
                self.ja = np.insert(self.ja, j_help+1, j)

    def to_dense(self):
        result = np.zeros((len(self.ia)-1, int(np.max(self.ja)+1)))
        for i in np.arange(0, len(self.ia)-1):
            i = int(i)
            for j in np.arange(self.ia[i], self.ia[i+1]):
                k = int(self.ja[int(j)])
                result[i][k] = self.a[int(j)]
        return result
