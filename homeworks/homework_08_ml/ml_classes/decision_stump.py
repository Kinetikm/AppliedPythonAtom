#!/usr/bin/env python
# coding: utf-8


import numpy as np


class DecisionStumpRegressor:
    '''
    Класс, реализующий решающий пень (дерево глубиной 1)
    для регрессии. Ошибку считаем в смысле MSE
    '''

    def __init__(self):
        '''
        Мы должны создать поля, чтобы сохранять наш порог th и ответы для
        x <= th и x > th
        '''
        self.th = None
        self.left = None
        self.right = None

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, left, right
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        X, y = zip(sorted(zip(X, y), key=lambda x: x[0]))
        X, y = np.array(X), np.array(y)
        hall = np.average(np.square(X - X.mean()))
        n = len(y)
        res_th = []
        for i in range(1, n):
            th = ((X[i - 1] + X[i]) / 2)[0]
            left, right = X[X < th], X[X > th]
            hleft = np.average(np.square(left - left.mean()))
            hright = np.average(np.square(right - right.mean()))
            res_th.append((th, hall - (len(left) * hleft + len(right) * hright) / n))

        self.th = max(res_th, key=lambda x: x[1])[0]
        self.left = y[(X <= self.th)].mean()
        self.right = y[(X > self.th)].mean()

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        return [self.right if x > self.th else self.left for x in X]
