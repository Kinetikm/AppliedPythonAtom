#!/usr/bin/env python
# coding: utf-8
from collections import deque, Counter


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):

        self.deq = deque()

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """

        event = {"user_id": user_id, "time": time}
        self.deq.append(event)

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """

        count_all = Counter()

        if self.deq:
            for event in self.deq:
                if time >= event["time"] > time - self.FIVE_MIN:
                    count_all[event["user_id"]] += 1

        result = 0
        for _, ct in dict(count_all).items():
            if ct == count:
                result += 1

        return result
