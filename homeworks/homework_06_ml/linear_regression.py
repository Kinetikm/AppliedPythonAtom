#!/usr/bin/env python
# coding: utf-8
from enum import Enum

import numpy as np


class UnfittedModel(Exception):
    pass


class LinearRegression:
    def __init__(self, lambda_coef=0.001, regularization=None, alpha=0.5):
        """
        :param lambda_coef: constant coefficient for gradient descent step
        :param regularization: regularization type ("L1" or "L2") or None
        :param alpha: regularization coefficient
        """

        self.alpha = alpha
        self.regularization = regularization
        self.lambda_coefficient = lambda_coef
        self.was_fitted = False

    def fit(self, X_train, y_train, max_iteration_number=1000, epsilon=1e-7):
        """
        Fit model using gradient descent method
        :param epsilon: convergence value
        :param max_iteration_number: maximum number of iterations
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        X_train = np.hstack([np.ones(X_train.shape), X_train])
        self.weights = np.ones(X_train.shape[1])
        weights = self.weights
        for i in range(max_iteration_number):
            if self.regularization == "L1":
                mse_alpha = self.alpha * (
                        self.weights / np.abs(self.weights)) / 2
            elif self.regularization == "L2":
                mse_alpha = self.alpha * self.weights
            else:
                mse_alpha = 0
            mse_loss = -2 / X_train.shape[0] * (
                    y_train - X_train @ self.weights) @ X_train + mse_alpha
            self.weights = self.weights - self.lambda_coefficient * mse_loss
            if all(np.abs(self.weights - weights)) < epsilon:
                break
            weights = self.weights
        self.was_fitted = True

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        X_test = np.hstack([np.ones(X_test.shape), X_test])
        if self.was_fitted:
            return (X_test @ self.weights).reshape(-1)
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
