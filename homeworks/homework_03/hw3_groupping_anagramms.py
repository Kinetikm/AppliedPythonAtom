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
    # TODO: реализовать функцию
    def isanag(a, b):
        l1 = list(a.lower())
        l2 = list(b.lower())
        if len(l1) != len(l2):
            return False
        l1 = l1.sort()
        l2 = l2.sort()
        if l1 == l2:
            return True
        return False

    lists = list()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if isanag(words[i], words[j]):
                l = list()
                l.append(words[i])
                l.append(words[j])
    return lists
