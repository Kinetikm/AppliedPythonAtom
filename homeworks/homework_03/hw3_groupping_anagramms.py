#!/usr/bin/env python
# coding: utf-8
from copy import deepcopy


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
    an_list = []
    n = 0
    words_copy = deepcopy(words)
    for i, word1 in enumerate(words):
        print("n =", n)
        print("words_copy", words_copy)
        try:
            words_copy.pop(0)
        except IndexError:
            break
        for word2 in words_copy:
            comp_word1 = deepcopy(word1)
            comp_word2 = deepcopy(word2)
            comp_word1 = comp_word1.lower()
            comp_word2 = comp_word2.lower()
            m = 0
            flag = True
            print("compare", word1, "with", word2)
            if len(comp_word1) != len(comp_word2):
                flag = False
            elif comp_word1 == comp_word2:
                if len(comp_word1) == 1:
                    flag = False
            else:
                w1 = list(comp_word1)
                w2 = list(comp_word2)
                for i in w1:
                    if i in w2:
                        m += 1
                if m == len(word1) and flag:
                    an_list.append([word1])
                    an_list[n].append(word2)
                    n += 1
    # TODO: реализовать функцию
    chars = delete_chars(words)
    print(an_list + chars)
    return an_list + chars
#    raise NotImplementedError


def delete_chars(list_of_words):
    ind_list = []
    char_list = []
    for i, val in enumerate(list_of_words):
        if len(val) == 1:
            char_list.append(val)
    n = 0
    for i, w1 in enumerate(char_list):
        ind_list.append([w1])
        for w2 in char_list:
            if w1.lower() == w2.lower():
                ind_list[n].append(w2)
                char_list.remove(w2)
        n += 1
    return(ind_list)
