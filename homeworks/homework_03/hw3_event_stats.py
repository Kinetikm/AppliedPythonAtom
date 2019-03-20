#!/usr/bin/env python
# coding: utf-8
import time
import copy
from collections import deque, Counter


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        # raise NotImplementedError
        self.log = {}

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        # raise NotImplementedError
        if self.log.get(user_id) is None:
            self.log[user_id] = [time]
        else:
            self.log[user_id].append(time)
            self.log[user_id] = sorted(self.log[user_id])

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
        # raise NotImplementedError
        keys = self.log.keys()
        log = copy.deepcopy(self.log)
        if count != 0:
            for usr in keys:
                while len(
                        log[usr]) > 0 and log[usr][0] not in range(
                        time - self.FIVE_MIN,
                        time):
                    log[usr].pop(0)
        cnt = 0
        for usr in keys:
            if len(log[usr]) == count:
                cnt += 1
        return cnt
