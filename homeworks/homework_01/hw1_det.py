#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    length=len(list_of_lists)
    for i in list_of_lists:
        if len(i)!=length:
            return(None)
    return recurs(list_of_lists,[i for i in range(length)],[j for j in range(length)])

def recurs(Ll,a,b):
    res=0
    if (len(a) == 1):
        return Ll[a[0]][b[0]]
    b1=b[1:]
    for i in range (len(a)):
        a1=a[::]
        a1.remove(a[i])
        res=res+(-1)**(i%2)*Ll[a[i]][b[0]]*recurs(Ll,a1,b1)
    return (res)

