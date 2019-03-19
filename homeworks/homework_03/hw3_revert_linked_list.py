#!/usr/bin/env python
# coding: utf-8

def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    #raise NotImplementedError
    new_head=None
    while head != None:
        print(head.value)
        tmp=head
        head=tmp.next_node
        tmp.next_node=new_head
        new_head=tmp
    return new_head

# class Node:
#     def __init__(self, value,next_node):
#         self.value=value
#         self.next_node=None


# def createlist(reglist):
#     retlist=Node(reglist[0])
#     itr=retlist
#     for i in reglist[1:]:
#         while itr.nextnode is not None:
#             itr=itr.nextnode
#         temp=Node(i)
#         itr.nextnode=temp
#     return retlist

# def print_list(innode):
#     while innode != None:
#         print(innode.data)
#         innode=innode.nextnode
