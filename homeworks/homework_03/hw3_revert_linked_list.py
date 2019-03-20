#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    prev_node = None
    while True:
        if head is None:
            return prev_node
        else:
            node = head.next_node
            head.next_node = prev_node
            prev_node = head
            head = node
