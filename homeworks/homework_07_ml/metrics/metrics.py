#!/usr/bin/env python
# coding: utf-8
import numpy as np
from collections import Counter


def logloss(y_true, y_pred, eps=1e-5):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated probabilities
    :param eps: epsilon
    :return: loss
    """
    y_pred = np.clip(y_pred, eps, 1-eps)
    return -np.sum(y_true*np.log(y_pred) + (1-y_true)*np.log(1-y_pred))/len(y_pred)


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    return Counter(y_pred)[1] / len(y_pred)


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    buf = len([x for x, y in zip(y_pred, y_true) if x[0] == y[0] == 1])
    return buf / Counter(y_pred)[1]


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    buf = len([x for x, y in zip(y_pred, y_true) if x[0] == y[0] == 1])
    return buf / Counter(y_true)[1]


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_pred: vector of estimated probabilities
    :return: loss
    """
    tpr = recall(y_true, y_pred)
    buf = len([x for x, y in zip(y_pred, y_true) if x[0] == 1 and y[0] == 0])
    fpr = buf / Counter(y_true)[0]
    return (1 + tpr - fpr) / 2
