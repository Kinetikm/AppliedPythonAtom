#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    fivemin = 300

    def __init__(self):
        self.users = {}

    def register_event(self, user_id, time):

        if user_id in self.users.keys():
            self.users.get(user_id).append(time)
        else:
            self.users[user_id] = [time]

    def query(self, count, time):

        result = []
        for key, value in self.users.items():
            k = 0
            for time_user in value:
                if time - self.fivemin < time_user <= time:
                    k += 1
            if count == 0 and k == 0:
                continue
            if k == count:
                result.append(key)
            else:
                continue
        return len(result)
