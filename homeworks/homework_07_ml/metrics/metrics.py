#!/usr/bin/env python
# coding: utf-8


import numpy as np


def logloss(y_true, y_pred, eps=1e-15):

    y_pred = np.clip(y_pred, eps, 1 - eps)
    return (y_true.dot(np.log(y_pred)) + (1 - y_true).dot(np.log(1 - y_pred))) / (-len(y_true))


def accuracy(y_true, y_pred):

    return np.sum(y_true == y_pred) / len(y_pred)


def precision(y_true, y_pred):

    TP = 0
    FP = 0
    for i in range(y_true):
        if y_true[i] == 0 and y_pred[i] != y_true[i]:
            FP += 1
        if y_true[i] == 1 and y_pred[i] == 1:
            TP += 1
    return TP / (FP + TP)


def recall(y_true, y_pred):

    FN = 0
    TP = 0
    for i in range(y_true):
        if y_true[i] == 1 and y_pred[i] == 0:
            FN += 1
        if y_true[i] == 1 and y_pred[i] == 1:
            TP += 1

    return TP / (TP + FN)


def roc_auc(y_true, y_pred):

    TPR = recall(y_true, y_pred)
    FP = 0
    TN = 0
    for i in range(y_true):
        if y_true[i] == 0 and y_pred[i] == 1:
            FP += 1
        if y_true[i] == 0 and y_pred[i] == 0:
            TN += 1
    FPR = FP / (FP + TN)

    return (1 + TPR - FPR) / 2
