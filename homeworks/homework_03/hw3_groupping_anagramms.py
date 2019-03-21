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
    words_itog = list()
    while words:
        last_word = words.pop()
        if not words:
            words_itog.append(last_word)
            return words_itog
        anagr_list = list()
        for i in range(len(words)):
            if inside(last_word, words[i]):
                anagr_list.append(words[i])
                words[i] = None
        words = [x for x in words if x is not None]
        anagr_list.append(last_word)
        words_itog.append(anagr_list)
    return words_itog


def inside(first, second):
    first = first.lower()
    second = second.lower()
    ch_d = dict()
    for char in first:
        if ch_d.get(char):
            ch_d[char] += 1
        else:
            ch_d[char] = 1
    for char in second:
        if ch_d.get(char):
            ch_d[char] -= 1
        else:
            return False
    for char in ch_d:
        if ch_d[char] != 0:
            return False
    return True
