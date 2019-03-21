#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    This = head
    early = None
    while This:
        next = This.next_node
        This.next_node = early
        early = This
        This = next
    return early