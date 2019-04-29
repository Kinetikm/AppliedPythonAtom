#!/usr/bin/env python
# coding: utf-8
import numpy as np
import sys

sys.setrecursionlimit(10000)


class Tree:
    def __init__(self, left_tree=None, right_tree=None):
        self.left_tree = left_tree
        self.right_tree = right_tree
        self.was_settled = False

    def set_values(self, th, index):
        self.th = th
        self.index = index
        self.was_settled = True


class DecisionTreeClassifier:
    '''
    Пишем свой велосипед - дерево для классификации
    '''

    def __init__(self, max_depth=None, min_leaf_size=1,
                 max_leaf_number=None, min_inform_criter=None):
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
        self.init_tree = None

    def compute_split_information(self, y, th):
        '''
        Вспомогательный метод, позволяющий посчитать джини/энтропию для заданного разбиения
        :param X: Матрица (num_objects, 1) - срез по какой-то 1 фиче, по которой считаем разбиение
        :param y: Матрица (num_object, 1) - целевые переменные
        :param th: Порог, который проверяется
        :return: прирост информации
        '''
        information = np.sum((y / len(y)) ** 2)
        left = th * information
        right = (len(y) - th) * information
        if self.min_inform_criter and self.min_inform_criter > information:
            return
        return (left + right) / len(y)

    def fit(self, X, y, current_tree=None, depth=0):
        '''
        Стендартный метод обучения
        :param X: матрица объекто-признаков (num_objects, num_features)
        :param y: матрица целевой переменной (num_objects, 1)
        :return: None
        '''
        if (self.max_depth and depth >= self.max_depth) or (
                self.min_leaf_size and len(y) <= self.min_leaf_size) or (
                self.max_leaf_number and len(y) > self.max_leaf_number):
            return
        max_info = 0
        max_th = None
        max_index = None
        for i in range(X.shape[1]):
            x_train = X[:, i]
            sorted_indexes = x_train.argsort()
            x_train, y_train = x_train[sorted_indexes], y[sorted_indexes]
            for j in range(1, y_train.shape[0]):
                if y_train[j - 1] != y_train[j]:
                    information = self.compute_split_information(y_train,
                                                                 th=j + 1)
                    if not information:
                        return
                    if information > max_info:
                        max_th = x_train[j]
                        max_info = information
                        max_index = i

        if not current_tree:
            current_tree = Tree()
            self.init_tree = current_tree

        current_tree.set_values(max_th, max_index)
        left_tree, right_tree = Tree(), Tree()
        current_tree.left_tree = left_tree
        current_tree.right_tree = right_tree
        self.fit(X[X[:, max_index] > max_th],
                 y[X[:, max_index] > max_th], left_tree, depth + 1)
        self.fit(X[X[:, max_index] <= max_th],
                 y[X[:, max_index] <= max_th], right_tree, depth + 1)

        def predict(self, X, current_tree):
            '''
            Метод для предсказания меток на объектах X
            :param X: матрица объектов-признаков (num_objects, num_features)
            :return: вектор предсказаний (num_objects, 1)
            '''
            assert self.init_tree.was_settled
            if not current_tree.left_tree and not current_tree.right_tree:
                return np.array([max(current_tree.index,
                                     key=lambda x: current_tree.index[x])] *
                                X.shape[0])
            prediction = np.zeros((X.shape[0],))
            if X[X[:, current_tree.index] > current_tree.th].shape[0] != 0:
                prediction[X[:, current_tree.index] > current_tree.th] = \
                    self.predict(
                        X[X[:, current_tree.index] > current_tree.th],
                        current_tree.left_tree)
            if X[X[:, current_tree.index] <= current_tree.th].shape[0] != 0:
                prediction[X[:, current_tree.index] <= current_tree.th] = \
                    self.predict(
                        X[X[:, current_tree.index] <= current_tree.th],
                        current_tree.right_tree)
            return prediction

        def predict_proba(self, X):
            '''
            метод, возвращающий предсказания принадлежности к классу
            :param X: матрица объектов-признаков (num_objects, num_features)
            :return: вектор предсказанных вероятностей (num_objects, 1)
            '''
            assert self.init_tree.was_settled
            if not current_tree.left_tree and not current_tree.right_tree:
                return np.array(
                    [list(current_tree.index.values()) for _ in
                     range(X.shape[0])])
            prediction = np.zeros((X.shape[0], len(self.classes)))
            if X[X[:, current_tree.index] > current_tree.th].shape[0] != 0:
                prediction[X[:, current_tree.index] > current_tree.th] = \
                    self.predict_proba(
                        X[X[:, current_tree.index] > current_tree.th],
                        current_tree.left_tree)
            if X[X[:, current_tree.index] <= current_tree.th].shape[0] != 0:
                prediction[X[:, current_tree.index] <= current_tree.th] = \
                    self.predict_proba(
                        X[X[:, current_tree.index] <= current_tree.th],
                        current_tree.right_tree)
            return prediction
