#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    prev = None
    curr = head
    next = curr.getNextNode()

    while curr:
        curr.setNextNode(prev)
        prev = curr
        curr = next
        if next:
            next = next.getNextNode()
        head = next
    return prev
