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
    if len(y_true) != len(y_pred):
        raise Exception("Size error")
    # формула из лекции
    coef = (-1)/len(y_true)
    return coef*np.sum((y_true * np.log(y_pred)) +
                       (1 - y_true) * np.log(1 - y_pred))


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    if len(y_true) != len(y_pred):
        raise Exception("Size error")
    loss = 0
    for i in len(y_true):
        if y_true[i] == y_true[i]:
            loss = loss + 1
    return loss / len(y_pred)


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    if len(y_true) != len(y_pred):
        raise Exception("Size error")
    TP = sum(y_true * y_pred)
    FP = 0
    for i in range(y_true):
        if (y_true[i] == 0 and y_pred[i] == 1):
            FP += 1
    return TP / (FP + TP)


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    if len(y_true) != len(y_pred):
        raise Exception("Size error")
    TP = sum(y_true * y_pred)
    FN = 0
    for i in range(y_true):
        if (y_true[i] == 1 and y_pred[i] == 0):
            FN += 1

    # формула из лекции

    return TP / (TP + FN)


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    if len(y_true) != len(y_pred):
        raise Exception("Size error")
    TPR = recall(y_true, y_pred)
    FP = 0
    TN = 0
    for i in range(y_true):
        if (y_true[i] == 0 and y_pred[i] == 1):
            FP += 1
        if (y_true[i] == 0 and y_pred[i] == 0):
            TN += 1
    FPR = FP/(FP + TN)
    # общий случай площади для бинарного решения
    return (1 + TPR - FPR)/2
