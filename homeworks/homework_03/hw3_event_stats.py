#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.events = {}

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        if user_id in self.events.keys():
            self.events[user_id].append(time)
        else:
            self.events[user_id] = [time]

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        activity_count = 0
        for i in self.events.values():
            quantity = 0
            for j in i:
                if time - self.FIVE_MIN < j and j <= time:
                    quantity = quantity + 1
            if quantity == count and quantity != 0:
                activity_count = activity_count + 1
        return activity_count
