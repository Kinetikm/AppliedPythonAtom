#!/usr/bin/env python
# coding: utf-8


class Heap():

    def __init__(self, array):
        self.length=len(array)         #size of heap
        self.heap=[None]*(self.length+1) #intialize an empty list
        self.last=0            #index where the last item was inserted
        self.array = array
        self.build_heap()

    def add(self, elem_with_priority):
        self.last+=1
        if self.last<=self.length:
            self.heap[self.last]=elem_with_priority[:]
        else:
            self.length+=1            #if the heap is already full
            self.heap+=[None]
            self.heap[self.last]=elem_with_priority[:]
        self.bubble_up()

    def build_heap(self):
        for x in self.array:
            self.add(x)

    def bubble_up(self):
        parent=self.last//2
        current=self.last
        while parent>0 and comparator_d(self.heap[current],self.heap[parent]):  #for min-heap
            self.heap[parent],self.heap[current]=self.heap[current],self.heap[parent]
            current=parent
            parent=parent//2

    def bubble_down(self):
        current=1
        child1=current*2
        child2=(current*2)+1
        while True:
            if child1<=self.length and child2<=self.length and ( current <=(self.length//2) and
                                                                     (comparator_d(self.heap[child1],self.heap[current]) or comparator_d(self.heap[child2],self.heap[current]))):
                ind=max((child1,child2),key=lambda x:self.heap[x][-1])
                self.heap[current],self.heap[ind]=self.heap[ind],self.heap[current]
                current=ind
                child1=current*2
                child2=(current*2)+1
            elif child1==self.length  and (current <=(self.length//2) and (self.heap[current] > self.heap[child1])):
                self.heap[current],self.heap[ind]=self.heap[ind],self.heap[current]
                break
            else:
                break

class MaxHeap(Heap):

    def __init__(self, array):
        super().__init__(array)


    def extract_maximum(self):
        if self.length>=1:
            maxx=self.heap[1].pop(-1)
            if len(self.heap[1])==0:
                self.length-=1
                self.heap[1],self.heap[self.last]=self.heap[self.last],self.heap[1]  #swap root with last element
                self.last-=1               #decrement length
                self.heap.pop(-1)          #pop the root that was moved to the last element
            if self.length>1:          #coz first item is None
                if self.length<=2:
                    self.heap[1:]=sorted(self.heap[1:], reverse=True,key=lambda x: x[-1]) #use reverse=True for max-heap
                else:
                    self.bubble_down()
            return maxx


def comparator_d(x, y):
    if x[-1] == y[-1]:
        return x[-2] >= y[-2]
    elif x[-1] > y[-1]:
        return True
    else:
        return False
