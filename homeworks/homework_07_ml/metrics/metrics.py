#!/usr/bin/env python
# coding: utf-8


import numpy as np


def logloss(y_true, y_hat, eps=1e-8):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated probabilities
    :param eps: for evading log(1) and log(0)
    :return: loss
    """
    y_hat = np.clip(y_hat, eps, 1 - eps)
    return ((y_true * np.log2(y_hat) + (1 - y_true) * np.log2(
        1 - y_hat)).sum()) / (len(y_true))


def accuracy(y_true, y_hat):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    true_positive, false_positive, true_negative, false_negative = \
        __confusion_matrix__(y_true, y_hat)
    return (true_positive + true_negative) / (
            true_positive + true_negative + false_negative + false_positive)


def precision(y_true, y_hat):
    """
    precision
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    true_positive, false_positive, true_negative, false_negative = \
        __confusion_matrix__(y_true, y_hat)
    return true_positive / (true_positive + false_positive)


def recall(y_true, y_hat):
    """
    recall
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    true_positive, false_positive, true_negative, false_negative = \
        __confusion_matrix__(y_true, y_hat)
    return true_positive / (true_positive + false_negative)


def roc_auc(y_true, y_hat):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    1 + TPR - FPR
    -------------  = S  ????
         2
    """
    true_positive, false_positive, true_negative, false_negative = \
        __confusion_matrix__(y_true, y_hat)
    t_p_r = true_positive / (true_positive + false_negative)
    f_p_r = false_positive / (false_positive + true_negative)
    return (1 + t_p_r - f_p_r) / 2


def __confusion_matrix__(y_true, y_hat):
    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0

    for i in range(len(y_hat)):
        if y_true[i] == y_hat[i] == 1:
            true_positive += 1
        if y_hat[i] == 1 and y_true[i] != y_hat[i]:
            false_positive += 1
        if y_true[i] == y_hat[i] == 0:
            true_negative += 1
        if y_hat[i] == 0 and y_true[i] != y_hat[i]:
            false_negative += 1

    return true_positive, false_positive, true_negative, false_negative
