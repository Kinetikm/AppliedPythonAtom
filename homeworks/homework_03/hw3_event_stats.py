#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.events = defaultdict(list)

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        self.events[user_id].append(time)

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        result = 0
        for ts in self.events.values():
            res_sum = sum(time - 300 < t < time for t in ts)
            result += 1 if res_sum == count != 0 else 0
        return result
