#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.users = dict()

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        if not (user_id in self.users):
            self.users[user_id] = list()
        self.users[user_id].append(time)

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
        n = 0
        for user in self.users:
            i = 0
            for times in self.users[user]:
                if (time - 300) < times and times <= time:
                    i += 1
            if i == count and self.users[user][0] <= time:
                n += 1
            print("sds " + str(i))
        return n
