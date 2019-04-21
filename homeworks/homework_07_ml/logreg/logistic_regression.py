#!/usr/bin/env python
# coding: utf-8


import numpy as np


class LogisticRegression:
    def __init__(
            self,
            n_iter=100,
            lambda_coef=1.0,
            regulatization=None,
            alpha=0.5):
        """
        LogReg for Binary case
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
        self.n = n_iter

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """

        def grad_f_withoutL(self, X_train, y_train, coef_last):
            return 1 / \
                len(X_train) * X_train.transpose() @ (self.sigmoid(X_train @ coef_last) - y_train)

        def grad_f_L1(self, X_train, y_train, coef_last):
            return 1 / len(X_train) * X_train.transpose() @ (self.sigmoid(
                X_train @ coef_last) - y_train) + self.alpha * 2 * coef_last

        def grad_f_L2(self, X_train, y_train, coef_last):
            return 1 / len(X_train) * X_train.transpose() @ (self.sigmoid(
                X_train @coef_last) - y_train) + self.alpha * np.ones(X_train.shape[1])

        def normalize(X_train):
            mean = np.mean(X_train, axis=0)
            std = np.std(X_train, axis=0)
            return (X_train - mean) / std

        assert X_train.shape[0] == y_train.shape[0], 'Invalid dimensions'

        X_train = normalize(X_train)
        step = self.lam
        X_train = np.c_[np.ones(X_train.shape[0]), X_train]
        self.coef_ = np.random.randn(X_train.shape[1])
        for i in range(self.n):
            coef_last = np.copy(self.coef_)
            if self.reg is None:
                self.coef_ = coef_last - step * \
                    grad_f_withoutL(self, X_train, y_train, coef_last)
            if self.reg == 'L1':
                self.coef_ = coef_last - step * \
                    grad_f_L1(self, X_train, y_train, coef_last)
            if self.reg == 'L2':
                self.coef_ = coef_last - step * \
                    grad_f_L2(self, X_train, y_train, coef_last)

            if np.all(abs(self.coef_ - coef_last) <
                      np.zeros(X_train.shape[1]) + 0.000001):
                self.intercept_ = self.coef_[0]
                self.coef_ = self.coef_[1:]
                return
        self.intercept_ = self.coef_[0]
        self.coef_ = self.coef_[1:]

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        try:
            pred_values = np.sign(
                np.sum(
                    self.intercept_ +
                    self.coef_ *
                    X_test,
                    axis=1))
            pred_values.astype(int)
            pred_values[pred_values == -1] = 0
            return pred_values
        except TypeError:
            print('Please, train your model first')

    def predict_proba(self, X_test):
        """
        Predict probability using model.
        :param X_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        try:
            return self.sigmoid(
                np.sum(
                    self.intercept_ +
                    self.coef_ *
                    X_test,
                    axis=1))
        except TypeError:
            print('Please, train your model first')

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if np.all(self.coef_ is None):
            print('Please, train your model first')
            return
        return np.hstack((self.intercept_, self.coef_))
