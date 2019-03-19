#!/usr/bin/env python
# coding: utf-8



kodirovki = ['utf8', 'utf16', 'cp1251']


def get_kod(filename):
    for kod in kodirovki:
        try:
            with open(filename, 'r', encoding=kod) as file:
                file.readlines()
                return kod
        except UnicodeError:
            continue
    print("Формат не валиден")
