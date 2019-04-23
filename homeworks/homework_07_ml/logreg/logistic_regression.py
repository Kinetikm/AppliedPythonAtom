#!/usr/bin/env python
# coding: utf-8
import numpy as np


class LogisticRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5, n_iter=100):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.learn_rate = lambda_coef
        assert regulatization in (None, 'L1', 'L2'), \
            "Wrong regularization value"
        self.reg = regulatization
        self.reg_rate = alpha
        self.n_iter = n_iter
        self._isTrain = False

    def fit(self, x_train, y_train, eps=1e-5):
        """
        Fit model using gradient descent method
        :param x_train: training data
        :param y_train: target values for training data
        :param eps: epsilon
        :return: None
        """
        assert x_train.shape[0] == y_train.shape[0], \
            "X and y shapes mismatch"

        self.mean_, self.std_ = np.mean(x_train), np.std(x_train)
        self.X_train = (x_train - self.mean_) / self.std_

        x_tr = np.hstack((np.ones((x_train.shape[0], 1)), x_train))
        self.W = np.random.normal(scale=0.001, size=x_tr.shape[1])

        # prev_w = np.zeros(self.W.shape)
        for epoch in range(self.n_iter):
            self._isTrain = True

            r_coef = 0.0
            if self.reg == 'L1':
                r_coef = np.hstack((0, self.reg_rate * np.ones(x_tr.shape[1] - 1) / 2))
            elif self.reg == 'L2':
                r_coef = np.hstack((self.W[0], self.reg_rate * self.W[1:]))

            y_hat = self.predict(x_train)
            grad = self._grad(y_hat, y_train, x_tr)
            self.W -= self.learn_rate * (grad + r_coef) / len(y_train)

            # if np.sum(np.abs(self.W - prev_w)) < eps:
            #    break
            # prev_w = self.W

        self.coef_ = self.W[1:]
        self.intercept_ = self.W[0]
        print("Done")

    def _grad(self, y_hat, y_true, x):
        """
        Calculate gradient
        """
        buf = 1 / len(y_true) * np.dot(x.T, y_hat - y_true)
        return buf

    def _loss(self, y_hat, y_true):
        """
        Calculate loss
        """
        res = np.sum(np.log(1 + np.exp(-y_true * y_hat)))
        return res / len(y_true)

    def _predict_proba(self, x_test):
        """
        Predict using model.
        :param x_test: test data for predict in
        :return: y_test: predicted values
        """
        assert self._isTrain, "Model not trained"
        x_test = (x_test - self.mean_) / self.std_
        x_test = np.hstack([np.ones((x_test.shape[0], 1)), x_test])
        z = 1 / (1 + np.exp(-np.dot(x_test, self.W)))
        return np.vstack((1 - z, z)).T

    def predict_proba(self, x_test):
        """
        Predict using model.
        :param x_test: test data for predict in
        :return: y_test: predicted values
        """
        assert self._isTrain, "Model not trained"
        x_test = np.hstack([np.ones((x_test.shape[0], 1)), x_test])
        z = 1 / (1 + np.exp(-np.dot(x_test, self.W)))
        return np.vstack((1 - z, z)).T

    def predict(self, x_test):
        """
        Predict probability using model.
        :param x_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        assert self._isTrain, "Model not trained"
        x_test = np.hstack([np.ones((x_test.shape[0], 1)), x_test])
        z = np.dot(x_test, self.W)
        return (1 / (1 + np.exp(-z))).astype(int)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        assert (not self._isTrain), "Model not trained"
        return self.W
