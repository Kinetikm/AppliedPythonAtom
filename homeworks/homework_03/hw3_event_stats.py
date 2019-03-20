#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.user_act = {}
        raise NotImplementedError

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        if not self.user_act.get(user_id):
            self.user_act[user_id] = [time]
        else:
            self.user_act[user_id].append(time)
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
        activity_count = 0
        for user, timestamp in self.act.items():
            index = 0
            for t in timestamp:
                if 0 <= time - t < self.FIVE_MIN:
                    index += 1
            if index == count:
                activity_count += 1
            if index != 0 and count != 0:
                continue

        return activity_count
        raise NotImplementedError
