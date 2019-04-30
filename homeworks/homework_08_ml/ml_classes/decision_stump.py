#!/usr/bin/env python
# coding: utf-8

import numpy as np
from sklearn.metrics import mean_squared_error


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
        self.left = None
        self.right = None
        self.th = None

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        xy = np.array(sorted(zip(X, y)))
        X, y = xy[:, 0], xy[:, 1]
        y2 = np.zeros(y.shape)
        mse = mean_squared_error(y, 0)
        for i in range(len(X) - 1):
            left = np.average(y[:i + 1])
            right = np.average(y[i + 1:])
            th = np.average(X[i:i + 2])
            y2[:i + 1] = left
            y2[i + 1:] = right
        if mse > mean_squared_error(y, y2):
            self.left = left
            self.right = right
            self.th = th

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        return [self.right if x > self.th else self.left for x in X]
