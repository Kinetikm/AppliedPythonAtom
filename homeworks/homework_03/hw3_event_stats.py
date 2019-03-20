#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.users_d = {}

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        if self.users_d.get(user_id):
            self.users_d[user_id].append(time)
        else:
            self.users_d[user_id] = [time]

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        count_act = 0
        for user in self.users_d:
            number_act_t = 0
            for action_time in self.users_d.get(user):
                if (time >= action_time) and \
                        (action_time > time - self.FIVE_MIN):
                    number_act_t = number_act_t + 1
            if number_act_t == count:
                if count > 0:
                    count_act = count_act + 1
                else:
                    for action_time in self.users_d.get(user):
                        if action_time < time:
                            count_act = count_act + 1
                            break
        return count_act
