#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.inf = {}

    def register_event(self, user_id, time):
        if self.inf.get(user_id) is None:
            self.inf[user_id] = []
        self.inf[user_id].append(time)

    def query(self, count, time):
        result = 0
        for i in self.inf.keys():
            j_left, j_right = -1, -1
            j = len(self.inf[i]) - 1
            while j >= 0:
                if self.inf[i][j] <= time:
                    j_right = j
                    break
                j -= 1
            j = 0
            while j < len(self.inf[i]):
                if self.inf[i][j] > time - TEventStats.FIVE_MIN:
                    j_left = j
                    break
                j += 1
            if j_left != -1 and j_right != -1:
                if len(self.inf[i][j_left:j_right+1]) == count:
                    result += 1
        return result
