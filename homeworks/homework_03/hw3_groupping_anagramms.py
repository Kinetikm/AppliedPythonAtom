#!/usr/bin/env python
# coding: utf-8


def groupping_anagramms(words):
    if not words:
        return []
    i = 0
    result = []
    while i < len(words):
        words[i] = [words[i], False]
        i += 1
    i = 0
    while i < len(words):
        if not words[i][1]: 
            h1 = False
            j = 0
            help_string1 = words[i][0].lower()
            while j < len(words):
                help_string2 = words[j][0].lower()
                if (not words[j][1] and j != i and 
                    len(help_string1) == len(help_string2)):
                    k = 0
                    h2 = False
                    while k < len(help_string2):
                        if help_string1.find(help_string2[k]) == -1:
                            h2 = True
                            break
                        k += 1
                    if not h2:
                        if not h1:
                            result.append([words[j][0]])
                        else:
                            result[-1].append(words[j][0])
                        h1 = True
                        words[j][1] = True
                j += 1
            if not h1:
                result.append([words[i][0]])
            else:
                result[-1].append(words[i][0])
            words[i][1] = True
        i += 1
    return result
