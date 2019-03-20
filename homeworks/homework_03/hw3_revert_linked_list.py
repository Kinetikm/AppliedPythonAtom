#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    if not head:
        return None
    else:
        new_head = None
        while head:
            add_head = head.next_node
            head.next_node = new_head
            new_head = head
            head = add_head
        return new_head
    raise NotImplementedError
