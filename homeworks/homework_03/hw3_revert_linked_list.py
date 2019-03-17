#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    if head is not None:
        list_buffer = None
        while head is not None:
            buffer = head.next_node
            head.next_node = list_buffer
            list_buffer = head
            head = buffer
        return list_buffer
    else:
        return None
