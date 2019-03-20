#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.users_dict = dict()

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        if self.users_dict.get(user_id):
            self.users_dict[user_id] = time
        else:
            self.users_dict[user_id] = [time]

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
        for user in self.users_dict:
            count_actions_t = 0
            for action_time in self.users_dict.get(user):
                if (time >= action_time) and (action_time > time - self.FIVE_MIN):
                    count_actions_t += 1
            if count_actions_t == count:
                if count != 0:
                    activity_count += 1
                else:
                    for action_time in self.users_dict.get(user):
                        if action_time < time:
                            activity_count += 1
                            break
        return activity_count
