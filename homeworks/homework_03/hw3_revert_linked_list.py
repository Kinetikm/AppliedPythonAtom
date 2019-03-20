#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    previous_node = None
    while head:
        next_node = head.next_node
        head.next_node = previous_node
        previous_node = head
        head = next_node
    return previous_node
