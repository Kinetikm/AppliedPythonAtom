#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    """
    Mean squared error regression loss
    :param derivative: take a derivative or not take
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    if derivative:
        # вроде в Slack'е сказали, что не надо
        return
    else:
        return np.sum((y_true - y_hat) ** 2 / len(y_true))


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    return np.sum(np.abs(y_true - y_hat) / len(y_true))


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    return 1 - (mse(y_true, y_hat) / mse(y_true, np.mean(y_true)))
