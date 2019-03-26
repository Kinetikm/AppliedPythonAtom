#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    first = head
    try:
        next = first.next_node
    except AttributeError:
        return first
    head_of_new_list = first
    head_of_new_list.next_node = None
    while True:
        if next is None:
            break
        next.next_node, head_of_new_list, next = \
            head_of_new_list, next, next.next_node
    return head_of_new_list
