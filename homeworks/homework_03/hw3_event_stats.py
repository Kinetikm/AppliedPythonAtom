#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.dict = {}

    def register_event(self, user_id, time):

        if user_id in self.dict.keys():
            self.dict[user_id].append(time)
        else:
            self.dict[user_id] = [time]

    def query(self, count, time):

        res = []
        for i, j in self.dict.items():
            suming = sum(time - 300 < x < time for x in j)
            if suming == 0 and count == 0:
                continue
            if suming == count:
                res.append(i)
        return len(res)