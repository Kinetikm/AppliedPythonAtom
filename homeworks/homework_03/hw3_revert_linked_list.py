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
    f_node = head.s_node
    new_head = head
    new_head.s_node = None
    while f_node is not None:
        f_node.s_node, new_head, f_node = \
           new_head, f_node,  f_node.s_node
    return new_head
