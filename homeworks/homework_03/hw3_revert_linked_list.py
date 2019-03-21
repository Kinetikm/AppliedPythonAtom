#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    tail = None
    while head:
        tmp = tail
        tail = head
        head = head.next_node
        tail.next_node = tmp
    return tail
