#!/usr/bin/env python
# coding: utf-8

import numpy as np


class LinearRegression:
    def __init__(self, lambda_coef=0.0004, regulatization=None, alpha=0.5):
        """
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.gradient = lambda_coef
        self.name_reg = regulatization
        self.coef_reg = alpha
        self.flag = False

    def fit(self, X_train, y_train, iteration=1000):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        self.weights = np.ones(X_train.shape[1] + 1)
        y_test = self._predict(X_train)
        for item in range(iteration):
            self.weights[:-1] -= 2 * self.gradient / X_train.shape[0] * \
                                 (y_test - y_train) @ X_train
            self.weights[-1] -= 2 * self.gradient / X_train.shape[0] * (
                    y_test - y_train).sum()
            if self.name_reg == 'L1':
                self.weights -= self.gradient * np.sign(self.weights)
            elif self.name_reg == 'L2':
                y_test -= self.gradient * self.weights
        self.flag = True

    def _predict(self, X_test):
        y_test = np.zeros(X_test.shape[0])
        for item in range(X_test.shape[0]):
            y_test[item] = (X_test[item, :] * self.weights[:-1]).sum() + \
                           self.weights[-1]
        if self.name_reg == 'L1':
            y_test += abs(self.weights).sum() * self.coef_reg
        elif self.name_reg == 'L2':
            y_test += (self.weights ** 2).sum() * self.coef_reg / 2
        return y_test

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        if not self.flag:
            raise Exception('This model instance is not fitted yet.')
        y_test = np.zeros(X_test.shape[0])
        for item in range(X_test.shape[0]):
            y_test[item] = (X_test[item, :] * self.weights[:-1]).sum() + \
                           self.weights[-1]
        if self.name_reg == 'L1':
            y_test += abs(self.weights).sum() * self.coef_reg
        elif self.name_reg == 'L2':
            y_test += (self.weights ** 2).sum() * self.coef_reg / 2
        return y_test

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if not self.flag:
            raise Exception('This model instance is not fitted yet.')
        return self.weights
