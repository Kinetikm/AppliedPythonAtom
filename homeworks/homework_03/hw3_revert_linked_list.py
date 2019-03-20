#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    new_head = None
    while head is not None:
        buffer = head.next_node
        head.next_node = new_head
        new_head = head
        head = buffer

    return new_head
