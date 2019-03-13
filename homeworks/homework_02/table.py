#!/usr/bin/env python
# coding: utf-8
import sys

# Ваши импорты
import json

# if __name__ == '__main__':
#    filename = sys.argv[1]


def dict_func (newdict):
    listofkeys=[]
    listofvalues=[]
    for key,value in newdict.items():
        listofkeys.append(key)
        listofvalues.append(value)
    return listofkeys, listofvalues


keyslist=[]
valueslist=[]
biglist=[]

def max_leng(kl, vl):
    maxleng=0
    tmp1=0
    for i in range(len(kl)):
        tmp1+=len(str(vl[i]))
        if(tmp1>maxleng):
            maxleng=tmp1
    return maxleng
newmax=0






with open('files/posts-cp1251.json', 'r') as f:
    data = json.load(f)
    len1=len(data)
    for i in range(len1):
        tmpdict=data.pop()
        keyslist, valueslist=dict_func(tmpdict)
        maximallength=max_leng(keyslist,valueslist)
        if maximallength>newmax:
            newmax=maximallength
        biglist.append(keyslist)
        biglist.append(valueslist)
asd=0
for i in range(len(biglist)):
    if i%2==0:
        if i>0:
            biglist.pop(i-asd)
            asd += 1
for i in range(len(biglist)):
    print (biglist[i])
