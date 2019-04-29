#!/usr/bin/env python
# coding: utf-8


import numpy as np


class LogisticRegression:
    def __init__(self, lambda_coef=1.0,
                 regularization=None,
                 alpha=0.5,
                 iterations=1000,
                 accuracy=0.01
                 ):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent coef
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.coef = lambda_coef
        self.theta = None
        self.alpha = alpha
        self.regularization = regularization
        self.iterations = iterations
        self.accuracy = accuracy

        self._reg_dict = {"L1": lambda y_true, y_pred:
                          self._logloss(y_true, y_pred) +
                          alpha * np.abs(self.theta).sum() +
                          alpha * np.sign(self.theta),

                          "L2": lambda y_true, y_pred:
                          self._logloss(y_true, y_pred) +
                          alpha * np.sqrt((self.theta ** 2).sum()) +
                          2 * alpha * self.theta,
                          }

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        x = np.hstack(np.ones(y_train.shape), X_train)
        self.theta = np.ones((x, 1))
        prev_y = np.dot(x, self.theta)

        for _ in range(self.iterations):
            self.theta -= self.coef * self._reg_dict[self.regularization](y_train, x)
            new_y = np.dot(x, self.theta)
            if (new_y - prev_y) < self.accuracy:
                break
            prev_y = new_y

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        return self.predict_proba(X_test).apply(
            lambda i: 1 if i >= 0.5 else 0
        )

    def predict_proba(self, X_test):
        """
        Predict probability using model.
        :param X_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        x = np.hstack(np.ones((X_test.shape[0], 1)), X_test)
        return self._sigmoid(np.dot(-x, self.theta))

    def get_weights(self):
        """
        Get theta from fitted linear model
        :return: theta array
        """
        return self.theta

    @staticmethod
    def _sigmoid(z):
        return 1 / (1 + np.exp(-z))

    @staticmethod
    def _logloss(y_true, y_pred, eps=1e-15):
        y_pred = np.clip(y_pred, eps, 1 - eps)
        return (y_true.dot(np.log(y_pred)) +
                (1 - y_true).dot(np.log(1 - y_pred))) / (-len(y_true))

    def _loss_l1(self, y_true, y_pred):
        return self._logloss(y_true, y_pred) + \
               self.alpha * np.abs(self.theta).sum()

    def _loss_l2(self, y_true, y_pred):
        return self._logloss(y_true, y_pred) + \
               self.alpha * np.sqrt((self.theta ** 2).sum())
