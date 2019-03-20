#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict
from collections import deque


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.__events = deque()

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        self.__events.append({'user_id': user_id, 'time': time})

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        # TODO: реализовать метод
        __users_eventCounter = defaultdict(int)

        for event in self.__events:
            if 0 <= time - event['time'] < self.FIVE_MIN:
                __users_eventCounter[event['user_id']] += 1

        activity_count = 0
        for user_id in __users_eventCounter:
            if __users_eventCounter[user_id] == count:
                activity_count += 1

        return activity_count
