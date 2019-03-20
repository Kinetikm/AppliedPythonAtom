#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.activs_dict = {}

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        if self.activs_dict.get(user_id, False):
            self.activs_dict[user_id].append(time)
        else:
            self.activs_dict[user_id] = []
            self.activs_dict[user_id].append(time)

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """

        res = 0
        for user, times in self.activs_dict.items():
            if times[0] <= time:
                cow = len(list(filter(lambda x: time - self.FIVE_MIN < x <= time, times)))
                if cow == count:
                    # print("\n\n",list(filter(lambda x: 0 < time - x < self.FIVE_MIN, self.activs_dict[user])))
                    res += 1
        return res
