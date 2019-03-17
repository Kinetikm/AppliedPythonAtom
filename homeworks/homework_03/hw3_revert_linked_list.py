#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    last = None
    now = None
    next = head
    while next is not None:
        last = now
        now = next
        next = now.next_node
        now.next_node = last
    return now
