#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
  MyDict = {}
  for j in range(len(input_list)):
      k = input_list[j]
      if k not in MyDict:
          MyDict.update({k: j})
      if MyDict.get(n-input_list[j]):
          return [MyDict.get(n-input_list[j]), j]
  return None

a = [2, 1, 4, 5, 7, 5, 1, 5, 8, 354, 23, 4356, 3421, 6, 321, 4]
print(find_indices(a, 4362))