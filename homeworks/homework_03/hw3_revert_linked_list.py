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

    new_head = None

    while head:
        head.next_node, head, new_head = new_head, head.next_node, head

    return new_head
