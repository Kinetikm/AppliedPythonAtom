#!/usr/bin/env python
# coding: utf-8
import numpy as np


class Tree:
    def __init__(self, left_tree=None, right_tree=None, index=0):
        self.left = left_tree
        self.right = right_tree
        self.index = index

    def set_values(self, th, index):
        self.th = th
        self.index = index

    def set_right_tree(self, tree):
        self.right = tree

    def set_left_tree(self, tree):
        self.left = tree


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
        self.init_tree = None
        self.classes = 0
        self.leaf_number = 0

    def compute_split_information(self, X, y, th):
        '''
        Вспомогательный метод, позволяющий посчитать джини/энтропию для заданного разбиения
        :param X: Матрица (num_objects, 1) - срез по какой-то 1 фиче, по которой считаем разбиение
        :param y: Матрица (num_object, 1) - целевые переменные
        :param th: Порог, который проверяется
        :return: прирост информации
        '''
        # число элементов
        n_instances = len(X)
        gini_old = 0.0
        size_0 = float(len(y))
        score_0 = 0.0
        # для каждого класса
        unique_0 = np.unique(y)
        if len(unique_0) > self.classes:
            self.classes = len(unique_0)
        for i in range(len(unique_0)):
            p = np.count_nonzero(y == unique_0[i]) / size_0
            score_0 += p * p
        # Джини для разбиения
        gini_old += (1.0 - score_0) * (size_0 / n_instances)

        right = np.zeros(0)
        left = np.zeros(0)
        # делим данные
        for i in range(n_instances):
            if X[i] < th:
                left = np.append(left, y[i])
            else:
                right = np.append(right, y[i])
        # считаем джини уже после разбиения
        gini_new = 0.0
        for group in [left, right]:
            size = float(len(group))
            # проверка на 0
            if size == 0:
                continue
            score = 0.0
            # для каждого класса
            unique = np.unique(group)
            for i in range(len(unique)):
                p = np.count_nonzero(group == unique[i]) / size
                score += p * p
            #  Джини для разбиения
            gini_new += (1.0 - score) * (size / n_instances)
        return (gini_old - gini_new)

    def fit(self, X, y, current_tree=None, depth=0):
        '''
        Стендартный метод обучения
        :param X: матрица объекто-признаков (num_objects, num_features)
        :param y: матрица целевой переменной (num_objects, 1)
        :return: None
        '''

        if (self.min_leaf_size and len(y) <= self.min_leaf_size):
            return
        if (self.max_depth and depth >= self.max_depth):
            return
        if (self.max_leaf_number and self.leaf_number >= self.max_leaf_number):
            return
        self.leaf_number += 1
        print(self.leaf_number, "leaf number")
        best_info = 0
        best_th = None
        best_index = None
        print("shape", X.shape[1])
        for i in range(X.shape[1]):
            # print(i)
            x_train = X[:, i]
            indexes = x_train.argsort()
            x_train, y_train = x_train[indexes], y[indexes]
            for j in range(1, y_train.shape[0]):
                if y_train[j - 1] != y_train[j]:
                    info = self.compute_split_information(x_train, y_train,
                                                          th=j)

                    if info > best_info:
                        best_th = x_train[j]
                        best_info = info
                        best_index = i
        if best_info == 0:
            return
        if not current_tree:
            current_tree = Tree()
            self.init_tree = current_tree
            print("create")

        print(best_th, best_index)
        current_tree.set_values(best_th, best_index)
        current_tree.set_right_tree(Tree())

        current_tree.set_left_tree(Tree())

        self.fit(X[np.all([X[:, best_index] < best_th], axis=0)],
                 y[np.all([X[:, best_index] < best_th], axis=0)], current_tree.left, depth + 1)
        if current_tree.left.index == 0:
            current_tree.left = None
        self.fit(X[np.all([X[:, best_index] >= best_th], axis=0)],
                 y[np.all([X[:, best_index] >= best_th], axis=0)], current_tree.right, depth + 1)
        if current_tree.right.index == 0:
            current_tree.right = None
        self.init_tree = current_tree

    def predict_proba(self, X, current_tree):
        '''
        метод, возвращающий предсказания принадлежности к классу
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказанных вероятностей (num_objects, 1)
        '''
        assert self.init_tree
        if not current_tree.left_tree and not current_tree.right_tree:
            return np.array(
                [list(current_tree.index.values()) for _ in
                 range(X.shape[0])])
        predict = np.ones((X.shape[0], len(self.classes)))
        if X[X[:, current_tree.index] > current_tree.th].shape[0] != 0:
            predict[X[:, current_tree.index] > current_tree.th] = \
                self.predict_proba(
                    X[X[:, current_tree.index] > current_tree.th],
                    current_tree.left_tree)
        if X[X[:, current_tree.index] <= current_tree.th].shape[0] != 0:
            predict[X[:, self.init_tree.index] <= current_tree.th] = \
                self.predict_proba(
                    X[X[:, current_tree.index] <= current_tree.th],
                    current_tree.right_tree)
        return predict

    def predict(self, X, current_tree):
        '''
        Метод для предсказания меток на объектах X
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказаний (num_objects, 1)
        '''
        assert self.init_tree
        if (current_tree == None):
            current_tree = self.init_tree

        if not current_tree.left and not current_tree.right:
            return np.array([max(current_tree.index,
                                 key=lambda x: current_tree.index[x])] *
                            X.shape[0])
        prediction = np.zeros((X.shape[0],))
        if X[X[:, current_tree.index] > current_tree.th].shape[0] != 0:
            prediction[X[:, current_tree.index] > current_tree.th] = \
                self.predict(
                    X[X[:, current_tree.index] > current_tree.th],
                    current_tree.left)
        if X[X[:, current_tree.index] <= current_tree.th].shape[0] != 0:
            prediction[X[:, current_tree.index] <= current_tree.th] = \
                self.predict(
                    X[X[:, current_tree.index] <= current_tree.th],
                    current_tree.right)
        return prediction
