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
    n = y_true.shape[0]
    if derivative is False:
        loss = (1 / n) * np.sum((y_true - y_hat) ** 2)
    elif derivative is True:
        #  не понял по какому аргументу брать производную. и как поступать со знаком. взял производную по прогнозу.
        loss = -(2 / n) * np.sum(y_true - y_hat)
    return loss


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    n1 = y_true.shape[0]
    loss = (1 / n1) * np.sum((np.abs(y_true - y_hat)))
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
    return loss
