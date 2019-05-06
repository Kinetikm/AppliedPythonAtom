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
        self.right = None
        self.left = None
        self.th = None

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        y_pred = np.zeros(y.shape)
        mse = mean_squared_error(y, 0)
        self.th = np.mean(X)
        self.right = np.mean(y[(y.size // 2) + 1:])
        self.left = np.mean(y[:(y.size // 2) + 1])
        for i in range(len(X) - 1):
            th = (X[i] + X[i + 1]) / 2
            y_left = np.mean(y[:i + 1])
            y_pred[:i + 1] = y_left
            y_right = np.mean(y[i + 1:])
            y_pred[i + 1:] = y_right
            mse_1 = mean_squared_error(y, y_pred)
            if mse >= mse_1:
                self.th = th
                self.right = y_right
                self.left = y_left
                mse = mse_1

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        y_pred = np.zeros(X.shape)
        for x in X:
            if x < self.th:
                y_pred[x] = self.y_left
            else:
                y_pred[x] = self.y_right
        return y_pred
