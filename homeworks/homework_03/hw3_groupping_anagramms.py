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
    list_of_lists_of_words = list()
    while words:
        last_word = words.pop()
        if not words:
            list_of_lists_of_words.append(last_word)
            return list_of_lists_of_words
        add_anagrams = list()
        for i in range(len(words)):
            if is_anagrams(last_word, words[i]):
                add_anagrams.append(words[i])
                words[i] = None
        words = [x for x in words if x is not None]
        add_anagrams.append(last_word)
        list_of_lists_of_words.append(add_anagrams)
    return list_of_lists_of_words


def is_anagrams(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.lower()
    dict_for_chars = dict()
    for char in first_word:
        if dict_for_chars.get(char):
            dict_for_chars[char] += 1
        else:
            dict_for_chars[char] = 1
    for char in second_word:
        if dict_for_chars.get(char):
            dict_for_chars[char] -= 1
        else:
            return False
    for char in dict_for_chars:
        if dict_for_chars[char] != 0:
            return False
    return True
