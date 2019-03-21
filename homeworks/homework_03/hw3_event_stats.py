#!/usr/bin/env python
# coding: utf-8

from collections import deque


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.events = deque()

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        self.events.append((user_id, time))

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
        if not self.events:
            return 0
        while self.events and time - self.events[0][1] > TEventStats.FIVE_MIN:
            self.events.popleft()
        users_to_count = dict()
        for event in self.events:
            if event[0] not in users_to_count:
                users_to_count.update({event[0]: 0})
            users_to_count[event[0]] += 1
        full_count = 0
        for count_for_user in users_to_count.values():
            if count_for_user == count:
                full_count += 1
        return full_count
