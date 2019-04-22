#!/usr/bin/env python
# coding: utf-8

import numpy as np


class UnfittedModel(Exception):
    pass


class LogisticRegression:
    def __init__(self, lambda_coef=0.1, regularization=None, alpha=0.5):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent step
        :param regularization: regularization type ("L1" or "L2") or None
        :param alpha: regularization coefficient
        """
        self.lambda_coef = lambda_coef
        self.regularization = regularization
        self.alpha = alpha
        self.was_fitted = False

    def fit(self, X_train, y_train, max_iteration_number=1000):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        self.number_of_classes = len(np.unique(y_train))
        X_train = np.hstack([np.ones((X_train.shape[0], 1)), X_train])
        self.weights = np.ones(
            shape=(self.number_of_classes, X_train.shape[1]))
        for m in range(self.number_of_classes):
            y_train_for_class = (y_train == m).astype(int)

            iter_weights = self.weights[m, :]

            for i in range(max_iteration_number):
                if self.regularization == "L1":
                    regularization = self.alpha * np.sign(iter_weights) / 2
                elif self.regularization == "L2":
                    regularization = self.alpha * iter_weights
                else:
                    regularization = 0
                log_loss = self.cost_gradient(
                    iter_weights, X_train, y_train_for_class) + regularization
                iter_weights -= self.lambda_coef * log_loss
            self.weights[m, :] = iter_weights

        self.was_fitted = True

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        if self.was_fitted:
            return self.predict_proba(X_test).argmax(axis=1)
        else:
            raise UnfittedModel("Model is not fitted!")

    def predict_proba(self, X_test):
        """
        Predict probability using model.
        :param X_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        if self.was_fitted:
            X_test = np.hstack([np.ones((X_test.shape[0], 1)), X_test])
            return self._sigmoid_(self.weights @ X_test.T).T
        else:
            raise UnfittedModel("Model is not fitted!")

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if self.was_fitted:
            return self.weights
        else:
            raise UnfittedModel("Model is not fitted!")

    def _sigmoid_(self, z):
        return 1 / (1 + np.exp(-z))

    def cost_gradient(self, theta, X_train, y_train):
        y_hat = self._sigmoid_(X_train @ theta)
        return X_train.transpose() @ (y_hat - y_train) / len(y_train)
