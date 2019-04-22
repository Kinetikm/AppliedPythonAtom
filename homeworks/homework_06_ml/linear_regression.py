#!/usr/bin/env python
# coding: utf-8


from metrics import mse
import numpy as np


class LinearRegression:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None
        self.__weights = None

    def fit(self, x_train, y_train, n_steps=100, eps=0.00001,
            lambda_coef=1.0, regularization=None, alpha=0.5):
        """
        Fit model using gradient descent method
        :param x_train: training data
        :param y_train: target values for training data
        :param n_steps: number of gradient descent steps
        :param eps: awaited difference of loss values between steps
        :param lambda_coef: constant coef for gradient descent step
        :param regularization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficient
        :return: None
        """
        assert regularization in [None, 'L1', 'L2'], 'Accept only None, L1 or L2 regularization'
        assert x_train.shape[0] == y_train.shape[0], 'Wrong X and y shapes'

        # подготовка
        n = len(y_train)
        prev_step = 0
        x_tmp = np.hstack([np.ones((x_train.shape[0], 1)), x_train])
        self.__weights = np.zeros(x_tmp.shape[1])

        # спуск
        for step in range(n_steps):
            # регуляризация
            reg_val = 0.0
            if regularization == 'L1':
                reg_val = alpha * np.ones(x_tmp.shape[1]) / 2
                reg_val[0] = 0.0
            elif regularization == 'L2':
                reg_val = alpha * self.__weights
                reg_val[0] = 0.0

            # расчёт
            y_hat = self.predict(x_train)
            self.__weights -= (2 * lambda_coef / n) * (np.dot(x_tmp.T, y_hat - y_train) + reg_val)

            # проверка критерия завершения
            cur_step = mse(y_hat, y_train)
            if np.abs(cur_step - prev_step) < eps:
                break
            prev_step = cur_step

        # запоминание коэффициентов (вес и bias)
        self.intercept_ = self.__weights[0]
        self.coef_ = self.__weights[1:]

    def predict(self, x_test):
        """
        Predict using model.
        :param x_test: test data for predict in
        :return: y_test: predicted values
        """
        assert self.__weights is not None, 'Model not trained'
        tmp = np.hstack([np.ones((x_test.shape[0], 1)), x_test])
        return np.dot(tmp, self.__weights)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        assert self.__weights is not None, 'Model not trained'
        return self.__weights
