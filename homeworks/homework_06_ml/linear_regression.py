#!/usr/bin/env python
# coding: utf-8
import numpy as np
from metrics import mse


class LinearRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5):
        """
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.lr = lambda_coef
        assert regulatization in (None, 'L1, L2'), \
            "Wrong regularization value"
        self.reg = regulatization
        self.reg_coef = alpha
        self._isTrain = False

    def fit(self, x_train, y_train, n_epochs=100, eps=1e-5):
        """
        Fit model using gradient descent method
        :param x_train: training data
        :param y_train: target values for training data
        :param n_epochs: number of epochs
        :param eps: ...
        :return: None
        """
        assert x_train.shape[0] == y_train.shape[0], \
            "X and y shapes mismatch"

        # инициализация весов небольшими значениями
        # и иниц.истории
        self.W = np.random.normal(scale=0.001, size=x_train.shape[1])
        self.history = np.zeros(n_epochs)

        self._max = x_train.max(axis=0)
        self._min = x_train.min(axis=0)
        x_train = (x_train - self._min) / (self._max - self._min)
        X = np.hstack((np.ones(x_train.shape[0], 1), x_train))
        N = len(y_train)

        # обучение
        for epoch in range(n_epochs):

            l_coef = 1.0
            if self.reg == 'L1':
                l_coef = self.reg_coef * np.ones(X.shape[1]) / 2
            elif self.reg == 'L2':
                l_coef = self.lr * self.W

            y_hat = self.predict(x_train)
            self.W -= (2 * self.lr / N) * (np.dot(X.T, y_hat - y_train) + l_coef)
            self.history[epoch] = mse(y_hat - y_train)

            if np.abs(self.history[epoch] - self.history[epoch + 1]) < eps:
                self.history = self.history[:epoch + 1]
                self._isTrain = True
                break

        self._isTrain = True

    def predict(self, x_test):
        """
        Predict using model.
        :param x_test: test data for predict in
        :return: y_test: predicted values
        """
        assert (not self._isTrain), "Model not trained"
        x_test = (x_test - self._min) / (self._max - self._min)
        x_test = np.hstack([np.ones(x_test.shape[1]), x_test])
        return np.dot(x_test, self.W)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        assert (not self._isTrain), "Model not trained"
        return self.W
