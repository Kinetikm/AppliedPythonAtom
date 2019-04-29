#!/usr/bin/env python
# coding: utf-8
import numpy as np


class KNNRegressor:
    """
    Построим регрессию с помощью KNN. Классификацию писали на паре
    """

    def __init__(self, n):
        '''
        Конструктор
        :param n: число ближайших соседей, которые используются
        '''
        self.n = n

    def normalize(self, X_train):
        mean = np.mean(X_train, axis=0)
        std = np.std(X_train, axis=0)
        return (X_train - mean) / std

    def fit(self, X, y):
        '''
        :param X: обучающая выборка, матрица размерности (num_obj, num_features)
        :param y: целевая переменная, матрица размерности (num_obj, 1)
        :return: None
        '''
        X = self.normalize(X)
        self.X = X
        self.y = y

    def predict(self, X):
        '''
        :param X: выборка, на которой хотим строить предсказания (num_test_obj, num_features)
        :return: вектор предсказаний, матрица размерности (num_test_obj, 1)
        '''
        y = []
        X = self.normalize(X)
        assert len(X.shape) == 2
        for t in X:
            # Посчитаем расстояние от всех элементов в тренировочной выборке
            # до текущего примера -> результат - вектор размерности трейна
            # TODO d =
            # Возьмем индексы n элементов, расстояние до которых минимально
            # результат -> вектор из n элементов
            # TODO idx =
            # TODO
            d = np.sqrt(np.sum((self.X - t) ** 2, axis=1))
            idx = np.argsort(d)[:self.n]
            prediction = np.mean(self.y[idx])
            y.append(prediction)
        return y
