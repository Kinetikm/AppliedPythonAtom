#!/usr/bin/env python
# coding: utf-8
import numpy as np


class DecisionTreeClassifier:
    '''
    Пишем свой велосипед - дерево для классификации
    '''

    def __init__(
            self,
            max_depth=None,
            min_leaf_size=None,
            max_leaf_number=None,
            min_inform_criter=None):
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
        self.root = None  # наше дерево

    def to_terminal(group):
        outcomes = [row[-1] for row in group]
        return max(set(outcomes), key=outcomes.count)

    def compute_split_information(self, groups, classes):
        '''
        Вспомогательный метод, позволяющий посчитать джини/энтропию для заданного разбиения
        :param X: Матрица (num_objects, 1) - срез по какой-то 1 фиче, по которой считаем разбиение
        :param y: Матрица (num_object, 1) - целевые переменные
        :param th: Порог, который проверяется
        :return: прирост информации
        '''
        # count all samples at split point
        n_instances = float(sum([len(group) for group in groups]))
        # sum weighted Gini index for each group
        gini = 0.0
        for group in groups:
            size = float(len(group))
            # avoid divide by zero
            if size == 0:
                continue
            score = 0.0
            # score the group based on the score for each class
            for class_val in classes:
                p = [row[-1] for row in group].count(class_val) / size
                score += p * p
            # weight the group score by its relative size
            gini += (1.0 - score) * (size / n_instances)
        return gini

    def test_split(self, index, value, X):
        left, right = list(), list()
        for row in X:
            if row[index] < value:
                left.append(row)
            else:
                right.append(row)
        return left, right

    def get_split(self, X, y):  # формируем левые и правые листья
        class_values = list(set(y))
        b_index, b_value, b_score, b_groups = None, None, 2, None
        for index in range(len(X)):
            for row in X:
                groups = self.test_split(index, row[index], X)
                gini = self.compute_split_information(groups, class_values)
                if gini < b_score:
                    b_index, b_value, b_score, b_groups = index, row[index], gini, groups
        return {'index': b_index, 'value': b_value, 'groups': b_groups}

    def split(self, depth):
        left, right = self.root['groups']
        del(self.root['groups'])
        # check for a no split
        if not left or not right:
            self.root['left'] = self.root['right'] = self.to_terminal(
                left + right)
            return
        # check for max depth
        if depth >= self.max_depth:
            self.root['left'], self.root['right'] = self.to_terminal(
                left), self.to_terminal(right)
            return
        # process left child
        if len(left) <= self.min_leaf_size:
            self.root['left'] = self.to_terminal(left)
        else:
            self.root['left'] = self.get_split(left)
            self.split(depth + 1)
        # process right child
        if len(right) <= self.min_leaf_size:
            self.root['right'] = self.to_terminal(right)
        else:
            self.root['right'] = self.get_split(right)
            self.split(depth + 1)

    def fit(self, X, y):
        '''
        Стендартный метод обучения
        :param X: матрица объекто-признаков (num_objects, num_features)
        :param y: матрица целевой переменной (num_objects, 1)
        :return: None
        '''
        self.root = self.get_split(X, y)
        self.split(1)
        # self.root = root

    def help_predict(self, node, row):
        if row[node['index']] < node['value']:
            if isinstance(node['left'], dict):
                return self.help_predict(node['left'], row)
            else:
                return node['left']
        else:
            if isinstance(node['right'], dict):
                return self.help_predict(node['right'], row)
            else:
                return node['right']

    def predict(self, X):
        '''
        Метод для предсказания меток на объектах X
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказаний (num_objects, 1)
        '''
        predictions = []
        for row in X:
            prediction = self.help_predict(self.root, row)
            predictions.append(prediction)
        return np.array(predictions)

    def predict_proba(self, X):
        '''
        метод, возвращающий предсказания принадлежности к классу
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказанных вероятностей (num_objects, 1)
        '''
        raise NotImplementedError
