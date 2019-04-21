#!/usr/bin/env python
# coding: utf-8


import numpy as np


def logloss(y, p):
    """
    logloss
    :param y: vector of truth (correct) class values
    :param p: vector of estimated probabilities
    :return: loss
    """
    assert y == p, "Invalid size"
    loss = (y * np.log(p) + (1 - y) * np.log(1 - p)).mean()
    return loss


def accuracy(y_true, y_hat):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    assert y_true == y_hat, "Invalid size"
    true = 0
    for index in (y_hat.size() - 1):
        if y_true[index] == y_hat[index]:
            true += 1
    loss = true / y_hat.size()


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    assert y_true == y_pred, "Invalid size"
    tp = 0
    fp = 0
    for index in (y_pred.size() - 1):
        if y_true[index] == y_pred[index] and y_true[index] == 1:
            tp += 1
        if y_true[index] == 0 and y_pred[index] == 1:
            fp += 1
    loss = tp / (tp + fp)


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    assert y_true == y_pred, "Invalid size"
    tp = 0
    fn = 0
    for index in (y_pred.size() - 1):
        if y_true[index] == y_pred[index] and y_true[index] == 1:
            tp += 1
        if y_true[index] == 1 and y_pred[index] == 0:
            fn += 1
    loss = tp / (tp + fn)


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_pred: vector of estimated probabilities
    :return: loss
    """
    assert y_true == y_pred, "Invalid size"
    tp = 0
    fn = 0
    fp = 0
    tn = 0
    for index in (y_pred.size() - 1):
        if y_true[index] == 1:
            if y_true[index] == y_pred[index]:
                tp += 1
            if y_pred[index] == 0:
                fn += 1
        if y_true[index] == 0:
            if y_true[index] == y_pred[index]:
                tn += 1
            if y_pred[index] == 1:
                fp += 1
    tpr = tp / (tp + fn)
    fpr = fp / (fp + tn)
    loss = tpr / fpr
    return loss
