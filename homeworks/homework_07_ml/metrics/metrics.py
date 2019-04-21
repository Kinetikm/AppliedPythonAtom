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
    if y.size != p.size:
        print("Size Error")
        return 0
    loss = (-1.0 / y.size) * np.sum(y * np.log(p) + (1 - y) * np.log(1 - p)).mean
    return loss


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    if y_true.size != y_pred.size:
        print("Size Error")
        return 0
    true = 0
    for index in range(len(y_true)):
        if y_true[index] == y_pred[index]:
            true += 1
    loss = true / len(y_true)
    return loss


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """

    def presicion(y_true, y_pred):
        if y_true.size != y_pred.size:
            print("Size Error")
            return 0
        tp = 0
        fp = 0
        for index in range(len(y_true)):
            if y_true[index] == y_pred[index] and y_true[index] == 1:
                tp += 1
            if y_true[index] == 0 and y_pred[index] == 1:
                fp += 1
        print(tp, fp)
        loss = tp / (tp + fp)
        return loss


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: loss
    """
    if y_true.size != y_pred.size:
        print("Size Error")
        return 0
    tp = 0
    fn = 0
    for index in range(len(y_true)):
        if y_true[index] == y_pred[index] and y_true[index] == 1:
            tp += 1
        if y_true[index] == 1 and y_pred[index] == 0:
            fn += 1
    loss = tp / (tp + fn)
    return loss


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_pred: vector of estimated probabilities
    :return: loss
    """
    if y_true.size != y_pred.size:
        print("Size Error")
        return 0
    tp = 0
    fn = 0
    fp = 0
    tn = 0
    for index in range(len(y_pred)):
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
    loss = (1 + tpr - fpr) / 2
    return loss
