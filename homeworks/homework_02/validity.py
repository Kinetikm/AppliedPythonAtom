# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:17:30 2019

@author: User
"""

def get_encoding_correct_file(filename):
    encoding = ('utf-16', 'utf8', 'cp1251')
    for e in encoding:
        try:
            with open(filename, 'r', encoding = e) as f:
                f.readlines()
                return e
        except UnicodeDecodeError:
            continue
        except UnicodeError:
            continue
        except FileNotFoundError:
            return 0
    return 1       


        

