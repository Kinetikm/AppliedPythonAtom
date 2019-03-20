#!/usr/bin/env python
# coding: utf-8

from collections import deque, Counter
import time


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        # raise NotImplementedError
        self.activity = deque()

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        self.activity.append((user_id, time))

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """

        c = Counter()
        for i in self.activity:
            if i[1] in range(time - self.FIVE_MIN, time):
                c[i[0]] += 1

        activity_count = 0
        for i in c.keys():
            if c[i] == count:
                activity_count += 1

        return activity_count
