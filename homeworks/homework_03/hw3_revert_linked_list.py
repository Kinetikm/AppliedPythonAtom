#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head4: LLNode
    :return: new_head: LLNode
    """
    if head is None:
        return None
    prev = None
    after = None
    while head:
        after = head.next_node
        head.next_node = prev
        prev = head
        head = after
    return prev
