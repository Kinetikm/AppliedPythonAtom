#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    """
    Mean squared error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    n = y_true.size()
    loss = (1 / n) * np.sum((y_true - y_hat) ** 2)
    return loss


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    n = y_true.size()
    loss = (1 / n) * np.sum((np.abs(y_true - y_hat)) ** 2)
    return loss


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    mean = np.mean(y_true)
    loss = 1 - ((np.sum((y_true - y_hat) ** 2)) / (np.sum((mean - y_true) ** 2)))
