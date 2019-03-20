#!/usr/bin/env python
# coding: utf-8


def anagrams_check(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    symbol_dict = {}
    for symbol in word1:
        if symbol_dict.get(symbol):
            symbol_dict[symbol] += 1
        else:
            symbol_dict[symbol] = 1
    for symbol in word2:
        if symbol_dict.get(symbol):
            symbol_dict[symbol] -= 1
        else:
            return False
    for symbol in symbol_dict:
        if symbol_dict[symbol] != 0:
            return False
    return True


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
                    ['Аз', 'За'], ['Ариост', 'сирота'],
                    ['Риме', 'мире'], ['Я', 'Я', 'я', 'я'],
                    ['в', 'в'], ['вижу', 'живу'],
                    ['есмь', 'семь'], ['мерой', 'морей'],
                    ['остр', 'рост'], ['ростка', 'строка']
                ]
    :param words: list of words (words in str format)
    :return: list of lists of words
    """
    # TODO: реализовать функцию

    list_of_lists = []
    while words:
        last_word = words.pop()
        if not words:
            list_of_lists.append(last_word)
            return list_of_lists
        add_anagrams = []
        for i in range(len(words)):
            if anagrams_check(last_word, words[i]):
                add_anagrams.append(words[i])
                words[i] = None
        words = [x for x in words if x is not None]
        add_anagrams.append(last_word)
        list_of_lists.append(add_anagrams)
    return list_of_lists
