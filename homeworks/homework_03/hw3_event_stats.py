#!/usr/bin/env python
# coding: utf-8

from collections import deque, Counter


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.events = deque()

    def register_event(self, user_id, time):
        self.events.appendleft((user_id, time))

    def query(self, count, time):
        cnt_dict = Counter()
        res_cnt = 0
        for event in self.events:
            if 0 <= time - event[1] < self.FIVE_MIN:
                cnt_dict[event[0]] += 1
        for item in cnt_dict.values():
            if item == count:
                res_cnt += 1
        return res_cnt
