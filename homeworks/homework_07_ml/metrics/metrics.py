#!/usr/bin/env python
# coding: utf-8


import numpy as np


def logloss(y_true, y_pred):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    assert y_true == y_pred, 'The sizes of y_true and y_pred vectors \
    are different'
    return np.log(1 + np.exp(- y_true*y_pred))


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    assert y_true == y_pred, 'The sizes of y_true and y_pred vectors \
    are different'
    n_true = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            n_true += 1
    return n_true/len(y_true)


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    assert y_true == y_pred, 'The sizes of y_true and y_pred vectors \
    are different'
    tp = 0  # True positive
    fp = 0  # False positive
    for i in range(len(y_true)):
        if y_true[i] == 1 and y_true[i] == y_pred[i]:
            tp += 1
        if y_pred[i] == 1 and y_true[i] != y_pred[i]:
            fp += 1
    return tp/(tp + fp)


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    assert y_true == y_pred, 'The sizes of y_true and y_pred vectors \
    are different'
    tp = 0  # True positive
    fn = 0  # False negative
    for i in range(len(y_true)):
        if y_true == 1 and y_true[i] == y_pred[i]:
            tp += 1
        if y_true == 1 and y_true[i] != y_pred[i]:
            fn += 1
    return tp/(tp + fn)


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    assert y_true == y_pred, 'The sizes of y_true and y_pred vectors \
    are different'
    treshold = 0.5  # If a probability given by y_pred is higher than
    #  this value, we think that's a positive prediction
    np.where(y_pred > treshold, 1, y_pred)
    np.where(y_pred <= treshold, 0, y_pred)
    tp = 0  # True positive
    fp = 0  # False positive
    for i in range(len(y_true)):
        if y_true == 1 and y_true[i] == y_pred[i]:
            tp += 1
        if y_pred[i] == 1 and y_true[i] != y_pred[i]:
            fp += 1
    return np.trapz(fp, tp)
