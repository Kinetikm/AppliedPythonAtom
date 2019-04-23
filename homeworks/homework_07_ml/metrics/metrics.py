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
    # accuracy = (TP + TN) / (TP + FP + FN + TN)
    # TP + TN = sum(y_true == y_pred)
    # FP + FN = sum(y_true != y_pred)
    # TP + FP + FN + TN = len(y_pred)
    return np.sum(y_true == y_pred) / len(y_pred)


def precision(y_true, y_pred):
    """
    Precision
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    # precision = TP / (TP + FP)
    # TP = sum(y_true * y_pred)
    # TP + FP = sum(pred)
    return np.sum(y_true * y_pred) / np.sum(y_pred)


def recall(y_true, y_pred):
    """
    Recall
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    # recall = TP / (TP + FN)
    # TP = sum(y_true * y_pred)
    # TP + FN = sum(y_true)
    return np.sum(y_true * y_pred) / np.sum(y_true)


def fpr(y_true, y_pred):
    """
    False positive rate
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return:
    """
    # FPR = FP / (FP + TN)
    # FP = sum((y_true == 0) & (y_pred == 1))
    # FP + TN = sum(y_true == 0)
    zt = (y_true == 0)
    return np.sum(zt & (y_pred == 1)) / np.sum(zt)


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_pred: vector of estimated probabilities
    :return: loss
    """
    # roc_auc = (1 + TPR - FPR) / 2
    # TPR = recall
    return (1 + recall(y_true, y_pred) - fpr(y_true, y_pred)) / 2
