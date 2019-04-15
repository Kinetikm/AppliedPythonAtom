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
        self.reg = regulatization
        self.alpha = alpha
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """

        def grad_f_withoutL(self, X_train, y_train, coef_last):
            return -2 * (1 / X_train.shape[0]) * X_train.transpose().dot(y_train) + 2 * (
                1 / X_train.shape[0]) * X_train.transpose().dot(X_train).dot(coef_last)

        def grad_f_L1(self, X_train, y_train, coef_last):
            return -2 * (1 / X_train.shape[0]) * X_train.transpose().dot(y_train) + 2 * (
                1 / X_train.shape[0]) * X_train.transpose().dot(X_train).dot(coef_last) + self.alpha * 2 * coef_last

        def grad_f_L2(self, X_train, y_train, coef_last):
            return -2 * (1 / X_train.shape[0]) * X_train.transpose().dot(y_train) + 2 * (1 / X_train.shape[0]) * \
                X_train.transpose().dot(X_train).dot(coef_last) + self.alpha * np.ones(X_train.shape[1])

        def normalize(X_train):
            mean = np.mean(X_train, axis=0)
            std = np.std(X_train, axis=0)
            return (X_train - mean) / std

        X_train = normalize(X_train)
        step = self.lam
        X_train = np.c_[np.ones(X_train.shape[0]), X_train]
        self.coef_ = np.random.randn(X_train.shape[1])
        i = 0
        while True:
            i += 1
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
                break
            if i == 3000:
                self.intercept_ = self.coef_[0]
                self.coef_ = self.coef_[1:]
                break

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        return np.sum(self.intercept_ + self.coef_ * X_test, axis=1)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        return np.hstack((self.intercept_, self.coef_))
