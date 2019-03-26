#!/usr/bin/env python
# coding: utf-8
from collections import deque


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.event_deque = deque()

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        event = (user_id, time)
        self.event_deque.append(event)

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
        user_actions = dict.fromkeys(
            set(map(lambda x: x[0],
                    filter(lambda t:
                           t[1] <= time and t[1] > time - self.FIVE_MIN,
                           self.event_deque))),
            0)
        for ev in reversed(self.event_deque):
            if ev[0] in user_actions:
                user_actions[ev[0]] += 1
        num_of_users = list(user_actions.values()).count(count)
        return num_of_users
