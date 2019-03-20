#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.dict_of_users = {}

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        if self.dict_of_users.get(user_id):
            self.dict_of_users[user_id].append(time)
        else:
            self.dict_of_users[user_id] = [time]

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
        for user in self.dict_of_users:
            number_of_timely_actions = 0
            for action_time in self.dict_of_users.get(user):
                if time >= action_time > time - self.FIVE_MIN:
                    number_of_timely_actions += 1
            if number_of_timely_actions == count:
                if count != 0:
                    activity_count += 1
                else:
                    for action_time in self.dict_of_users.get(user):
                        if action_time < time:
                            activity_count += 1
                            break
        return activity_count
