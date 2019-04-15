#!/usr/bin/env python
# coding: utf-8


import numpy as np


class LinearRegression:

    # инициализация
    def __init__(self, e=10**-5, lambda_coef=0.001, regularization=None,
                 alpha=0.5):
        self.e = e
        self.lambda_coef = lambda_coef
        self.regularization = regularization
        self.alpha = alpha
        self.training = False
        self.mean_x, self.sigma_x = [], []
        self.mean_y, self.sigma_y = 0, 0

    # обучение
    def fit(self, x_train, y_train):
        self.training = True  # в скором времени модель будет обучена
        # приводим x_train в удобный вид
        if type(x_train[0]) is not np.ndarray:
            help_array = np.zeros([len(x_train), 1])
            for i in np.arange(len(x_train)):
                help_array[i][0] = x_train[i]
            x_train = help_array
        # нормализуем входные данные и запоминаем прежние их параметры
        for i in np.arange(len(x_train[0])):
            self.sigma_x.append(np.std(x_train[:, i]))
            self.mean_x.append(np.mean(x_train[:, i]))
            x_train[:, i] = (x_train[:, i]-self.mean_x[i])/self.sigma_x[i]
        self.sigma_y = np.std(y_train)
        self.mean_y = np.mean(y_train)
        y_train = (y_train-self.mean_y)/self.sigma_y
        # задаем начальные веса
        self.weights = np.random.rand(len(x_train[0])+1)
        # совершаем один шаг градиентного спуска
        grad = self.loss_grad(x_train, y_train)
        help_weights = self.weights-self.lambda_coef*grad
        # реалиуем градиентный спуск
        while grad @ grad > self.e:
            self.weights = help_weights
            grad = self.loss_grad(x_train, y_train)
            help_weights = self.weights-self.lambda_coef*grad
        self.weights = help_weights
        # корректируем веса с учетом начальной нормировки
        for i in np.arange(len(x_train[0])):
            self.weights[i] *= self.sigma_y/self.sigma_x[i]
        self.weights[-1] *= self.sigma_y
        self.weights[-1] += self.mean_y-np.sum(self.weights[:-1]*self.mean_x)

    # градиент функции потерь в точке нынешних весов
    def loss_grad(self, x, y):
        result = np.zeros(len(self.weights))
        for i in np.arange(len(y)):
            # вычисляем очередное значение, предлагаемое моделью
            y_model = x[i] @ self.weights[:-1] + self.weights[-1]
            # обавляем очередное слагаемое к каждой из координат grad
            for j in np.arange(len(result)-1):
                result[j] += -2*(y[i]-y_model)*x[i][j]/len(y)
            result[-1] += -2*(y[i]-y_model)/len(y)
        # в зависимости от типа регуляризации вносим поправку
        for j in np.arange(len(result)-1):
            if self.regularization == 'L1':
                result[j] += self.alpha*np.sign(self.weights[j])
            elif self.regularization == 'L2':
                    result[j] += self.alpha*2*self.weights[j]
        return result

    # функиця потерь в точке weights (для возможности изменить условие
    # выхода из цикла)
    def loss(self, x, y, weights):
        # вычисляем очередное значение, предлагаемое моделью
        y_model = x @ weights[:-1] + weights[-1]
        if self.regulatization is None:
            return (y - y_model) @ (y - y_model) / len(y)
        elif self.regularization == 'L1':
            return ((y - y_model) @ (y - y_model) / len(y) +
                    self.alpha * np.sum(np.abs(weights[:-1])))
        elif self.regularization == 'L2':
            return ((y - y_model) @ (y - y_model) / len(y) +
                    self.alpha * 2 * weights[:-1] @ weights[:-1])

    def predict(self, x_test):
        if self.training:
            return x_test @ self.weights[:-1] + self.weights[-1]
        else:
            print('Модель не обучена')
            return Warning

    def get_weights(self):
        if self.training:
            return self.weights
        else:
            print('Модель не обучена')
            raise Warning
