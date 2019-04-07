#!/usr/bin/env python
# coding: utf-8

import numpy as np
np.seterr(divide='ignore')  # допускаем деление на 0, т.к получаем inf


def simplex_method(a, b, c):
    """
    Почитать про симплекс метод простым языком:
    * https://ru.wikibooks.org/wiki/Симплекс-метод._Простое_объяснение
    Реализацию алгоритма взять тут:
    * https://youtu.be/gRgsT9BB5-8 (это ссылка на 1-ое из 5 видео).

    Используем numpy и, в целом, векторные операции.

    a * x.T <= b
    c * x.T -> max
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(n, 1)
    :param c: np.array, shape=(1, m)
    :return x: np.array, shape=(1, m)
    """
    basis = np.full(len(b), -1)  # базис позиции

    # Формирование симплекс таблицы
    # строк = всего ограничений + P
    # столбцов = основных переменных + доп переменных + P + ограничение
    lines = len(b) + 1
    cols = len(a[0]) + len(b) + 1 + 1
    full_table = np.zeros((lines, cols))
    table_eye = np.eye(lines)

    for i in range(len(a)):
        full_table[i, :] = np.hstack([a[i], table_eye[i], b[i]])
    full_table[-1, :] = np.hstack([-1 * c, table_eye[-1], 0])

    # Расчёт симплекс методом
    while True:
        # Выбор столбца с наименьшим значением
        p_column = np.argmin(full_table[-1])
        if full_table[-1, p_column] >= 0:
            break

        # Выбор строки с наименьшим значением (вес / значение в выбранном столбце)
        p_line = np.argmin(full_table[:, -1][:-1] / full_table[:, p_column][:-1])

        # Приведение выбранного pivot к 1
        pivot = full_table[p_line, p_column]
        if pivot != 1:
            full_table[p_line, :] /= pivot

        # Обнуляем все значения в pivot_column
        for i in range(len(full_table)):
            if i != p_line:
                full_table[i, :] += full_table[i, p_column] * -1 * full_table[p_line, :]

        # Обновление позиций
        basis[p_line] = p_column

    # Формирование результата
    x = np.zeros(len(c))  # результаты
    for i in range(len(full_table) - 1):
        if basis[i] >= 0:
            x[int(basis[i])] = full_table[i, -1]

    return x
