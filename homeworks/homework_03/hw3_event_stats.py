#!/usr/bin/env python
# coding: utf-8
from collections import deque, Counter


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.memory_time = TEventStats.FIVE_MIN
        self.act_memory = deque()
#        raise NotImplementedError

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        self.act_memory.appendleft((user_id, time))
#        raise NotImplementedError

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]),
        совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        # TODO: реализовать метод
        acted_users = []
        for x in self.act_memory:
            if (x[1] > time - self.memory_time) and (x[1] <= time):
                acted_users.append(x[0])
        counter = Counter(acted_users)
        i = 0
        if count in counter.values():
            for x in counter.values():
                if x == count:
                    i += 1
            activity_count = i
            return activity_count
        else:
            return 0
