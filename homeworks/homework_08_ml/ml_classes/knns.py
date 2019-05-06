#!/usr/bin/env python
# coding: utf-8


class KNNRegressor:
    """
    Построим регрессию с помощью KNN. Классификацию писали на паре
    """

    def __init__(self, k):
        '''
        Конструктор
        :param k: число ближайших соседей, которые используются
        '''
        self.k = k

    def fit(self, X, y):
        '''
        :param X: обучающая выборка, матрица размерности (num_obj, num_features)
        :param y: целевая переменная, матрица размерности (num_obj, 1)
        :return: None
        '''
        self.x = X
        self.y = y

    def predict(self, X):
        '''
        :param X: выборка, на которой хотим строить предсказания (num_test_obj, num_features)
        :return: вектор предсказаний, матрица размерности (num_test_obj, 1)
        '''

        raise NotImplementedError

        y = []
        assert len(X.shape) == 2
        for t in X:
            # Посчитаем расстояние от всех элементов в тренировочной выборке
            # до текущего примера -> результат - вектор размерности трейна
            # TODO d =

            # посчитаю длину вектора (при вычитании получил матрицу, поэтому axis = 1)
            d = np.linalg.nortm(t - self.x, axis=1)  # ord = 2 стоит по-умолчанию

            # Возьмем индексы n элементов, расстояние до которых минимально
            # результат -> вектор из n элементов
            # TODO idx =
            idx = np.argsort(d)[:self.k]
            # TODO

            # усредняем значения, которые дали ближайшие соседи
            prediction = np.mean(self.y[idx])
            y.append(prediction)
        return y
