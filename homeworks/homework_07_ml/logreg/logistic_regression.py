#!/usr/bin/env python
# coding: utf-8


import numpy as np


class LogisticRegression:
    def __init__(self, lambda_coef=0.3, regulatization=None, alpha=0.7):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.learning_rate = lambda_coef
        self.regularizarion = regulatization
        self.alpha = alpha
        self.train = False

    def fit(self, X_train, y_train, iterations=1000, delta=0.1 ** 7):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """

        def normalize(X_train):
            mean = np.mean(X_train, axis=0)
            std = np.std(X_train, axis=0)
            return (X_train - mean) / std

        if (X_train.shape[0] == y_train.shape[0]):
            X_train = normalize(X_train)
            # создааем матрицу Х ов ,где последний  столбец единичный
            x_vect = np.hstack([X_train, np.ones((X_train.shape[0], 1))])
            # колчисество стобцов в матрице X
            cols_X = x_vect.shape[1]
            # веса.первый признак будет для w0-свободный член
            self.w = (np.random.randn(cols_X) / np.sqrt(cols_X)).reshape(-1, 1)
            hist0 = np.zeros(cols_X)
            hist1 = np.zeros(cols_X)
            for it in range(iterations):
                # https://habr.com/ru/company/ods/blog/322076/ брал отсюда
                if self.regularizarion == 'L1':
                    r = self.alpha * np.sign(self.w)
                    r[0] = 0
                elif self.regularizarion == 'L2':
                    r = self.alpha * self.w
                    r[0] = 0
                else:
                    r = 0
                prediction = self.predict_proba(X_train).T
                y_train = y_train.T
                p = (prediction.T - y_train).T
                self.w -= ((-2 / x_vect.shape[0]) * (self.learning_rate * x_vect.T.dot(p
                                                                                       ) + r))
                if it % 2 == 0:
                    hist0 = self.w
                else:
                    hist1 = self.w

                # coef = self.r[1:] intercept = self.r[0]
            self.train = True
            return self

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        assert getattr(self, 'train') is False, 'Model is not fitted'
        x_test = np.hstack([X_test, np.ones((X_test.shape[0], 1))])
        xw = x_test.dot(self.w)
        p = 1 / (1 + np.exp(-xw))
        if p > 0.5:
            return 1
        else:
            return 0

    def predict_proba(self, X_test):
        """
        Predict probability using model.
        :param X_test: test data for predict in
        :return: y_test: predicted probabilities
        """

        x_test = np.hstack([X_test, np.ones((X_test.shape[0], 1))])
        xw = x_test.dot(self.w).T
        res = 1 / (1 + np.exp(-xw))
        return res

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        return self.w
