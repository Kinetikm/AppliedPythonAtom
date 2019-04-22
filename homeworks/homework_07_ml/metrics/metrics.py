#!/usr/bin/env python
# coding: utf-8


import numpy as np


def logloss(y_true, y_pred, eps=1e-8):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated probabilities
    :param eps: ...
    :return: loss
    """
    # (-1 / l) * ( y_true * log(y_pred) + (1 - y_true) * log(1 - y_pred) )
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return -1 * (y_true.dot(np.log(y_pred)) + (1 - y_true).dot(np.log(1 - y_pred))) / len(y_true)


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    pass


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    pass


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    pass


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_pred: vector of estimated probabilities
    :return: loss
    """
    pass
