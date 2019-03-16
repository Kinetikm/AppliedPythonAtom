#!/usr/bin/env python
# coding: utf-8

import copy


def revert_linked_list(head):
    if head is None:
        return None
    # проверяем, присуствует ли хотя бы два элемента в списке
    if head.next_node is not None:
        # далее работаем с копиями объектов
        h1 = copy.copy(head)
        h2 = copy.copy(head.next_node)
        h1.next_node = None
        while h2.next_node is not None:
            h = copy.copy(h2.next_node)
            h2.next_node = copy.copy(h1)
            h1 = copy.copy(h2)
            h2 = copy.copy(h)
        h2.next_node = copy.copy(h1)
        return h2
    else:
        return head
