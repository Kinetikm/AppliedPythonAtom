#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    prev = None

    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev
