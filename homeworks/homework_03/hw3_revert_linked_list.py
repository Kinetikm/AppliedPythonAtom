#!/usr/bin/env python
# coding: utf-8

from .hw3_testing import LLNode


def revert_linked_list(head: LLNode):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """

    prev = None
    curr = head
    while curr:
        nex = curr.next_node
        curr.next_node = prev
        prev = curr
        curr = nex
    return prev
