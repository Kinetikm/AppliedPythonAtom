#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    try:
        prev = head.next_node
    except AttributeError:
        return head
    new_head = head
    new_head.next_node = None
    while prev:
        new_head, prev.next_node, prev =\
            prev, new_head, prev.next_node
    return new_head
