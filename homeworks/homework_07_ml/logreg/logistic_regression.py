#!/usr/bin/env python
# coding: utf-8

import numpy as np


class LogisticRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None,
                 alpha=0.5, iteration=5000, accuracy=0.001):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent step
    :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.lambda_coef = lambda_coef
        self.reg = regulatization
        self.alpha = alpha
        self.iteration = iteration
        self.accuracy = accuracy


# Сигмоида
    def function(self, X):
        return 1 / (1 + np.exp(-(self.weights @ X.T)))


# использую конечную формулу
    def grad(self, X_train, y_train):
        return np.dot(X_train.T, (function(X_train) - y_train)) / \
               X_train.shape[0]

    def regTest(self):
        if self.reg == 'L1':
            r = self.alpha * np.sign(self.w)
            return r

        if self.reg == 'L2':
            r = self.alpha * self.w
            return r

        return 0

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        size = X_train.shape[0]

        if size != y_train.shape[0]:
            raise Exception("Size error")
# заполнил массив весов (размер на 1 больше из-за w0)
        self.weights = np.random.randn(size + 1)
        previous_weights = self.weights
# добавил столбец 1 (первый)
        X_train = np.hstack([np.ones((n, 1), dtype='int64'),
                             X_train])

# цикл закончится, если на соседних итерациях точность будет подходящая
        for _ in range(self.iteration):
            self.weights -= (self.lambda_coef * self.grad(
                X_train, y_train) + regTest())

            if np.abs((self.weights - previous_weights).all()) <\
                    self.accuracy:
                return

            previous_weights = self.weights

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        predict = self.predict_proba(X_test)
        if predict > 0.5:
            return 1
        return 0

    def predict_proba(self, X_test):
        """
        Predict probability using model.
        :param X_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        size = X_test.shape[0]
        X = np.hstack(np.ones((size, 1)), X_test)
        return self.function(X)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        return self.weights
