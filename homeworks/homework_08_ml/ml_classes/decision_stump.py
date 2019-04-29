#!/usr/bin/env python
# coding: utf-8
import numpy as np
from sklearn.metrics import mean_squared_error
from operator import itemgetter


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

    def sorting(self, X, y):
        X_and_y = np.vstack((X, y))
        X_and_y = np.array(
            sorted(
                X_and_y.transpose(),
                key=lambda x: x[0])).transpose()
        return X_and_y[0], X_and_y[1]

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        assert len(X) == len(y), 'Invalid dimensions'

        mse_min = np.var(y)
        X, y = self.sorting(X, y)
        # граничный случай, если все на 1 прямой лежит
        if len(np.unique(y)) == 1:
            self.th = np.min(X)
            self.left = None
            self.right = np.mean(y)
            return

        for i in range(len(X) - 1):
            th = np.mean(X[i:i + 2])
            mse_left = np.var(y[:i + 1])
            mse_right = np.var(y[i + 1:])
            mse_new = mse_left + mse_right
            if mse_new < mse_min:
                self.th = th
                self.left = np.mean(y[:i + 1])
                self.right = np.mean(y[i + 1:])
                mse_min = mse_new

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        y_pred = np.zeros(X.shape[0])
        for x in X:
            if x < self.th:
                y_pred[x] = self.y_left
            else:
                y_pred[x] = self.y_right
        return y_pred
