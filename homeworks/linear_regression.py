#!/usr/bin/env python
# coding: utf-8
import numpy as np


class LinearRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5):
        """
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.lam = lambda_coef
        assert regulatization is None or regulatization == 'L1' or regulatization == 'L2', 'You entered wrong reg'
        self.reg = regulatization
        self.alpha = alpha
        self.coef_ = None
        self.intercept_ = None
        self.n_range = 3000
        self._eps = 1e-9
        self._flag = False

    def grad_f(self, X_train, y_train, coef_last, regulator):
        return -2 * (1 / X_train.shape[0]) * X_train.transpose().dot(y_train) + 2 * (
            1 / X_train.shape[0]) * X_train.transpose().dot(X_train).dot(coef_last) + regulator

    def normalize(self, X_train):
        mean = np.mean(X_train, axis=0)
        std = np.std(X_train, axis=0)
        return (X_train - mean) / std

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        assert X_train.shape[0] == y_train.shape[0], 'Invalid dimensions'
        X_train = self.normalize(X_train)
        step = self.lam
        X_train = np.c_[np.ones(X_train.shape[0]), X_train]
        self.coef_ = np.random.randn(X_train.shape[1])
        regulator = 0
        for i in range(self.n_range):
            coef_last = np.copy(self.coef_)
            if self.reg is None:
                regulator == 0
            if self.reg == 'L1':
                regulator = self.alpha * 2 * coef_last
            if self.reg == 'L2':
                regulator == self.alpha * np.ones(X_train.shape[1])

            self.coef_ = coef_last - step * \
                self.grad_f(X_train, y_train, coef_last, regulator)

            err = np.sum(np.abs(self.coef_ - coef_last))
            if err < self._eps:
                break
        self.intercept_ = self.coef_[0]
        self.coef_ = self.coef_[1:]
        self._flag = True

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        if self.flag
        return np.sum(self.intercept_ + self.coef_ * X_test, axis=1)
        print('Please, train your model first')

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if self._flag:
            return np.hstack((self.intercept_, self.coef_))
        print('Please, train your model first')
