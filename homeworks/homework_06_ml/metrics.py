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
    n = len(y_true)
    return np.sum(np.power(y_true-y_hat, 2)) / n


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    n = len(y_true)
    return np.sum(np.abs(y_true-y_hat)) / n


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    return 1 - np.sum(np.power(y_true-y_hat, 2)) / np.sum(np.power(y_true-np.mean(y_true), 2))
