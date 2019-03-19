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
    words_dict = dict()
    result_list = []
    for word in words:
        tmp = ''.join(sorted(word.lower()))

        if tmp not in words_dict:
            words_dict[tmp] = [word]

        else:
            words_dict.setdefault(tmp, [])
            words_dict[tmp].append(word)

    for key, value in words_dict.items():

        if len(value) > 1:
            result_list.append(value)
    return result_list
