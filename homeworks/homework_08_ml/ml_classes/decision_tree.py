#!/usr/bin/env python
# coding: utf-8

import numpy as np


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def set_values(self, th, index):
        self.th = th
        self.index = index


class DecisionTreeClassifier:
    '''
    Пишем свой велосипед - дерево для классификации
    '''

    def __init__(self, max_depth=None, min_leaf_size=None, max_leaf_number=None, min_inform_criter=None):
        '''
        Инициализируем наше дерево
        :param max_depth: один из возможных критерием останова - максимальная глубина дерева
        :param min_leaf_size: один из возможных критериев останова - число элементов в листе
        :param max_leaf_number: один из возможных критериев останова - число листов в дереве.
        Нужно подумать как нам отобрать "лучшие" листы
        :param min_inform_criter: один из критериев останова - процент прироста информации, который
        считаем незначительным
        '''
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        self.max_leaf_number = max_leaf_number
        self.min_inform_criter = min_inform_criter
        self.root = None

    def compute_split_information(self, y, th):
        '''
        Вспомогательный метод, позволяющий посчитать джини/энтропию для заданного разбиения
        :param X: Матрица (num_objects, 1) - срез по какой-то 1 фиче, по которой считаем разбиение
        :param y: Матрица (num_object, 1) - целевые переменные
        :param th: Порог, который проверяется
        :return: прирост информации
        '''
        entropy = np.sum((y / len(y)) ** 2)
        if th is None:
            return entropy
        left = th * entropy
        right = (len(y) - th) * entropy
        if self.min_inform_criter and self.min_inform_criter > entropy:
            return None
        return (left + right) / len(y)

    def fit(self, X, y, cur=None, depth=0):
        '''
        Стендартный метод обучения
        :param X: матрица объекто-признаков (num_objects, num_features)
        :param y: матрица целевой переменной (num_objects, 1)
        :return: None
        '''
        if (self.max_depth and depth >= self.max_depth) or (
                self.max_leaf_number and len(y) > self.max_leaf_number) or (
                self.min_leaf_size and len(y) <= self.min_leaf_size) or (
                False not in [y[i] == y[i + 1] for i in range(len(y) - 1)]):
            return
        max_th = max_feature = max_info = 0
        for i in range(X.shape[1]):
            x_train = X[:, i]
            indices = x_train.argsort()
            x_train, y_train = x_train[indices], y[indices]
            for j in range(1, y_train.shape[0]):
                if y_train[j - 1] != y_train[j]:
                    new_max_info = self.compute_split_information(y_train, j + 1)
                    if not new_max_info:
                        return
                    if new_max_info > max_info:
                        max_th = x_train[j]
                        max_info = new_max_info
                        max_feature = i

        if not self.root:
            cur = Node()
            self.root = cur

        cur.set_values(max_th, max_feature)
        left, right = Node(), Node()
        cur.left = left
        cur.right = right
        self.fit(X[X[:, max_feature] > max_th],
                 y[X[:, max_feature] > max_th], left, depth + 1)
        self.fit(X[X[:, max_feature] <= max_th],
                 y[X[:, max_feature] <= max_th], right, depth + 1)

    def predict(self, X, t):
        '''
        Метод для предсказания меток на объектах X
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказаний (num_objects, 1)
        '''
        if not t.left and not t.right:
            return np.array([max(t.index,
                                 key=lambda x: t.index[x])] *
                            X.shape[0])
        classes = np.zeros(X.shape[0])

        if X[X[:, t.index] <= t.th].shape[0] != 0:
            classes[X[:, t.index] <= t.th] = self.predict(
                                                  X[X[:, t.index] <= t.th],
                                                  t.right)

        if X[X[:, t.index] > t.th].shape[0] != 0:
            classes[X[:, t.index] > t.th] = self.predict(
                                                 X[X[:, t.index] > t.th],
                                                 t.left)

        return classes

    def predict_proba(self, X, t):
        '''
        метод, возвращающий предсказания принадлежности к классу
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказанных вероятностей (num_objects, 1)
        '''
        if not t.left and not t.right:
            return np.array(
                [list(t.index.values()) for _ in
                 range(X.shape[0])])
        probas = np.zeros(X.shape[0])
        if X[X[:, t.index] <= t.th].shape[0] != 0:
            probas[X[:, t.index] <= t.th] = self.predict_proba(
                                                 X[X[:, t.index] <= t.th],
                                                 t.right)

        if X[X[:, t.index] > t.th].shape[0] != 0:
            probas[X[:, t.index] > t.th] = self.predict_proba(
                                                X[X[:, t.index] > t.th],
                                                t.left)
        return probas
