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
    sum = y_true @ np.log(y_pred) + (np.ones(len(y_pred)) -
                                     y_true) @ np.log(np.ones(len(y_pred)) - y_pred)
    return -sum / len(y_true)


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    TP = 0
    TN = 0
    for i in range(len(y_true)):
        if (y_true[i] == 1 and y_pred[i] == 1):
            TP += 1
        if (y_true[i] == 0 and y_pred[i] == 0):
            TN += 1
    return (TP + TN) / len(y_pred)


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    TP = 0
    FP = 0
    for i in range(len(y_true)):
        if (y_true[i] == 1 and y_pred[i] == 1):
            TP += 1
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
    TP = 0
    FN = 0
    for i in range(len(y_true)):
        if (y_true[i] == 1 and y_pred[i] == 1):
            TP += 1
        if (y_true[i] == 1 and y_pred[i] == 0):
            FN += 1
    return TP / (TP + FN)


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    TPR = []
    FPR = []
    threshold = 0
    for _ in range(100):
        y_pred1 = np.copy(y_pred)
        TP, FN, FP, TN = 0, 0, 0, 0
        y_pred1[y_pred1 >= threshold] = 1
        y_pred1[y_pred1 < threshold] = 0
        y_pred1.astype(int)
        for i in range(len(y_true)):
            if (y_true[i] == 1 and y_pred1[i] == 1):
                TP += 1
            if (y_true[i] == 0 and y_pred1[i] == 1):
                FP += 1
            if (y_true[i] == 0 and y_pred1[i] == 0):
                TN += 1
            if (y_true[i] == 1 and y_pred1[i] == 0):
                FN += 1
        TPR = np.append(TPR, TP / (TP + FN))
        FPR = np.append(FPR, FP / (FP + TN))
        threshold += 0.01
    return -np.trapz(TPR, FPR, axis=0)
