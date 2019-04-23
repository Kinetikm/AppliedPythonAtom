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
        assert regulatization in (None, 'L1', 'L2'), \
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
        x_ = np.hstack((np.ones((x_train.shape[0], 1)), x_train))
        n = len(y_train)

        # инициализация весов небольшими значениями
        # и иниц.истории
        self.W = np.random.normal(scale=0.001, size=x_.shape[1])
        self._isTrain = True

        prev_err = 0.0
        # обучение
        for epoch in range(n_epochs):
            r_coef = 0.0
            if self.reg == 'L1':
                r_coef = np.hstack((0, self.reg_coef * np.ones(x_.shape[1] - 1) / 2))
            elif self.reg == 'L2':
                r_coef = np.hstack((self.W[0], self.reg_coef * self.W[1:]))

            y_hat = self.predict(x_train)
            self.W -= (2 * self.lr / n) * (np.dot(x_.T, y_hat - y_train) + r_coef)
            curr_err = mse(y_hat, y_train)

            if np.abs(curr_err - prev_err) < eps:
                break
            prev_err = curr_err

        self.coef_ = self.W[1:]
        self.intercept_ = self.W[0]
        print("Done")

    def predict(self, x_test):
        """
        Predict using model.
        :param x_test: test data for predict in
        :return: y_test: predicted values
        """
        assert self._isTrain, "Model not trained"
        x_test = np.hstack([np.ones((x_test.shape[0], 1)), x_test])
        return np.dot(x_test, self.W)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        assert self._isTrain, "Model not trained"
        return self.W
