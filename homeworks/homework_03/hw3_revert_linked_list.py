#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    
    """
    if head is None:
        return head
    prev, next = None, None
    curr = head
    while curr is not None:
        next = curr.next_node
        curr.next_node = prev
        prev = curr
        curr = next
    return prev
