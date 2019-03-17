#!/usr/bin/env python
# coding: utf-8


def groupping_anagramms(words):
    """
    Функция, которая группирует анаграммы.
    Возвращаем массив, где элементом является массив с анаграмами.
    Пример:  '''Аз есмь строка живу я мерой остр
                За семь морей ростка я вижу рост
                Я в мире сирота
                Я в Риме Ариост'''.split()
                ->
                [
                 ['Аз'], ['есмь', 'семь'],
                 ['строка', 'ростка'], ['живу', 'вижу'],
                 ['я', 'я'], ['мерой', 'морей'],
                 ['остр)'], ['За'], ['рост'], ['Я', 'Я'],
                 ['в', 'в'], ['мире'], ['сирота'],
                 ['Риме'], ['Ариост']
                ]
    :param words: list of words (words in str format)
    :return: list of lists of words
    """
    sort_buf = []
    res_buf = []
    counter = []
    for i in words:
        sort_buf.append(sorted(i.lower()))
    i = 0
    while i < len(sort_buf):
        j = i + 1
        buf = []
        if i not in counter:
            buf.append(words[i])
            while j < len(sort_buf):
                if sort_buf[i] == sort_buf[j]:
                    buf.append(words[j])
                    counter.append(j)
                j = j + 1
        if buf:
            res_buf.append(buf)
        i = i + 1
    return res_buf
