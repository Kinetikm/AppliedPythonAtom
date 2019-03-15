#!/usr/bin/env python
# coding: utf-8


from collections import deque, Counter


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.actions = deque()

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        self.actions.appendleft({'user_id': user_id, 'time': time})

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        actions_count = Counter()
        for item in self.actions:
            if 0 <= time - item['time'] < self.FIVE_MIN:
                actions_count[item['user_id']] += 1
            elif actions_count:
                break

        rez = 0
        for key, value in dict(actions_count).items():
            if value == count:
                rez += 1
        return rez
