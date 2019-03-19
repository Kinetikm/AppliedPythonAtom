#!/usr/bin/env python
# coding: utf-8
import collections


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.users_activity = dict()

    def register_event(self, user_id, time):
        if user_id in self.users_activity.keys():
            self.users_activity[user_id].append(time)
        else:
            self.users_activity[user_id] = [time]

    def query(self, count, time):
        overall_activity = dict()
        for id in self.users_activity.keys():
            overall_activity[id] = 0
            if self.users_activity[id][0] > time:
                overall_activity[id] -= 1
                continue
            for act in self.users_activity[id]:
                if (act > time - self.FIVE_MIN) and (act <= time):
                    overall_activity[id] += 1
        result = [number for number in overall_activity.values()]
        return collections.deque(result).count(count)
