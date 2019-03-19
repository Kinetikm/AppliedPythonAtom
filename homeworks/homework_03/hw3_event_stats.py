#!/usr/bin/env python
# coding: utf-8
import collections


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.activity = collections.deque()

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод

        self.activity.appendleft((time, user_id))

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
        activity_count = 0
        time_dict = {}
        for tmp in self.activity:
            if time - self.FIVE_MIN < tmp[0] <= time:
                if tmp[1] in time_dict:
                    time_dict[tmp[1]] = time_dict.get(tmp[1]) + 1
                else:
                    time_dict[tmp[1]] = 1
        for user, counts in time_dict.items():
            if counts == count:
                activity_count += 1
        return activity_count
