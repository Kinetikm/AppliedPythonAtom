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
        self.lth = None
        self.rth = None

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        sorted_indexes = X.argsort()
        X, y = X[0, sorted_indexes[0]], y[0, sorted_indexes[0]]
        n = len(y)
        qx = np.array([])
        for i in range(1, X.shape[0]):
            th = np.mean(X[i - 1:i + 1])
            qxi = (np.var(y[:i]) * i + np.var(y[i:]) * (y.shape[0] - i)) / \
                  y.shape[0]
            qx.append(qxi)
        idx = np.argmin(qx)
        self.th, self.rth, self.lth = X[idx], np.mean(y[:idx]), np.mean(
            y[idx:])

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        answer = np.array(X.shape)
        for x in X:
            if x <= self.th:
                answer[x] = self.lth
            else:
                answer[x] = self.rth
        return answer
