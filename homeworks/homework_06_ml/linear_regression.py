#!/usr/bin/env python
# coding: utf-8
import numpy as np
from metrics import mse


class LinearRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5):
        """
        :param lambda_coef: constant coef for gradient descent step шаг спуска
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.learning_rate = lambda_coef
        self.regularizarion = regulatization
        self.alpha = alpha
        self.train = False

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        iterations = 1000
        delta = 0.1 ** 5
        if (X_train.shape[0] == y_train.shape[0]):
            # создааем матрицу Х ов ,где первый столбец единичный
            x_vect = np.hstack(((np.ones((X_train.shape[0], 1))), X_train))
            # колчисество стобцов в матрице X
            cols_X = x_vect.shape[1]
            # веса.первый стобец будет для w0
            self.w = (np.random.randn(cols_X) / np.sqrt(cols_X)).reshape(1, -1)
            history = np.zeros(iterations + 1)
            for it in range(iterations):
                # https://habr.com/ru/company/ods/blog/322076/ брал отсюда
                if self.regularizarion == 'L1':
                    r = self.alpha * np.absolute(self.w) / 2
                    r[0] = 0
                elif self.regularizarion == 'L2':
                    r = self.alpha * np.square(self.w ** 2) / 2
                    r[0] = 0
                else:
                    r = 0
                self.w -= (-2) * self.lambda_coef * x_vect.T @ (y_train - (x_vect @ self.w)) + r
                prediction = self.predict(X_train)
                history[it + 1] = mse(y_train, prediction)
                if np.abs(history[it + 1] - history[it]) < delta:
                    break
            # coef = self.w[1:] intercept = self.w[0]
            self.train = True
            return self

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        assert getattr(self, 'w', 0) != 0, 'Model is not fitted'
        x_test = np.hstack([np.ones((X_test.shape[0], 1)), X_test])
        return x_test.dot(self.w)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        assert getattr(self, 'w', 0) != 0, 'Model is not fitted'
        return self.w
