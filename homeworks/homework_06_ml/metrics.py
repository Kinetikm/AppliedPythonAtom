#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    y_true = np.array(y_true)
    y_hat = np.array(y_hat)
    if derivative:
        return np.mean(2*(y_true - y_hat))

    return np.mean((y_true - y_hat)**2)


def mae(y_true, y_hat):
    y_true = np.array(y_true)
    y_hat = np.array(y_hat)
    return np.mean(np.abs(y_true - y_hat))


def r2_score(y_true, y_hat):
    y_true = np.array(y_true)
    y_hat = np.array(y_hat)
    return 1 - (np.sum((y_true - y_hat) ** 2) /
                np.sum((y_true - np.mean(y_true))) ** 2)
