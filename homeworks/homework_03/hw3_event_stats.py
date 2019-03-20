#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.events = {}
        raise NotImplementedError

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        if user_id in self.events.keys():
            self.events[user_id].append(time)
        else:
            self.events[user_id] = time
        raise NotImplementedError

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
        count_users = 0
        for user_id in self.events.keys():
            count_event = 0
            for times in self.events[user_id]:
                if time - FIVE_MIN < times <= time:
                    count_event += 1
            if count_event == count:
                count_users += 1
        return count_users
        raise NotImplementedError
