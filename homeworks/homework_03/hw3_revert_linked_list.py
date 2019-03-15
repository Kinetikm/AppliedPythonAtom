#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    if head is None or head.next_node is None:
        return head

    prev = None
    cur = head
    while cur is not None:
        next = cur.next_node
        cur.next_node = prev
        prev = cur
        cur = next
    head = prev
    return head
