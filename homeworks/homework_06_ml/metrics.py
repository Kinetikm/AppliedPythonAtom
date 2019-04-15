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
    num = np.array(y_true).shape[0]
    loss = (np.array(y_true) - np.array(y_hat)) ** 2
    return loss.sum() / num


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    num = np.array(y_true).shape[0]
    return abs(np.array(y_true) - np.array(y_hat)).sum() / num


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    y_true_np = np.array(y_true)
    y_mean = np.zeros(y_true_np.shape[0]) + y_true_np.mean()
    return 1 - mse(y_true, y_hat) / mse(y_true, y_mean)
