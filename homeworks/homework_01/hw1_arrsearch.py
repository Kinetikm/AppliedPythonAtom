#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    i=0
    j=len(input_list)-1
    if (n==0 or j<1):
        return(None)
    a=list(input_list)
    a.sort()
    while i!=j:
        if (a[i]+a[j]==n):
            return(input_list.ind(a[i]),input_list.ind(a[j]))
        elif (a[i]+a[j]>n):
            i+=1
        else:
            j-=1
    return(None)
