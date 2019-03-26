#!/usr/bin/env python
# coding: utf-8
from collections import OrderedDict


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
    lettersets = OrderedDict()
    result = []
    for word in words:
        print(word)
        lowerword = word.lower()
        letters = list(lowerword)
        jumbled_letters = ''.join(sorted(letters))
        if jumbled_letters not in lettersets.keys():
            lettersets[jumbled_letters] = []
        lettersets[jumbled_letters].append(word)
    for v in lettersets.values():
        result.append(v)
    return result
