#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    """
    Mean squared error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :param derivative: if true return mse derivative regression loss
    :return: loss
    """
    # mse = ( 1 / N ) * sum( (y_true[i] - y_hat[i]) ^ 2 )
    # mse = mean( (y_true[i] - y_hat[i]) ^ 2 )
    # mse_derivative = ( -2 / N ) * sum( y_true[i] - y_hat[i] )
    # mse_derivative = -2 * mean( y_true[i] - y_hat[i] )

    n = len(y_true)

    if derivative:
        part_x = [(y_true[i] - y_hat[i]) for i in range(n)]
        return np.mean(part_x) * -2

    part_x = [(y_true[i] - y_hat[i]) ** 2 for i in range(n)]
    return np.mean(part_x)


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    # mae = ( 1 / N ) * sum( |y_true[i] - y_hat[i]| )
    # mae = mean( |y_true[i] - y_hat[i]| )

    n = len(y_true)
    part_x = [abs(y_true[i] - y_hat[i]) for i in range(n)]

    return np.mean(part_x)


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    # r2 = 1 - sum( (y_true[i] - y_hat[i]) ^ 2 ) / sum( (y_true[i] - mean) ^ 2 )
    # mean = sum(y_true) / N
    n = len(y_true)
    part_x = [(y_true[i] - y_hat[i]) ** 2 for i in range(n)]

    m = np.mean(y_true)
    part_y = [(y_true[i] - m) ** 2 for i in range(n)]

    r2 = 1 - (sum(part_x) / sum(part_y))

    return r2
