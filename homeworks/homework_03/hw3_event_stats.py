#!/usr/bin/env python
# coding: utf-8
import time

class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        #raise NotImplementedError
        self.log={}

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        #raise NotImplementedError
        print('register: '+str(user_id)+' '+str(time))
        if self.log.get(user_id) is None:
            self.log[user_id]=[time]
        else:
            self.log[user_id].append(time)
            self.log[user_id]=sorted(self.log[user_id])


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
        print('query: '+str(count)+' '+str(time))
        print(time- self.FIVE_MIN)
        keys=self.log.keys()
        log=self.log
        if count != 0:
            for usr in keys:
                while len(log[usr])>0 and log[usr][0] < time - self.FIVE_MIN:
                    log[usr].pop(0)
                # for i in range(len(self.log[usr])):
                #     if i>len(self.log[usr]):
                #             break
                #     if self.log[usr][i] < time - self.FIVE_MIN:
                #         self.log[usr].pop(i)         
        cnt = 0
        for usr in keys:
            if len(log[usr])==count:
                cnt+=1
        return cnt


a=TEventStats()
a.register_event(122, 1552565081)
a.register_event(123, 1552565082)
a.register_event(124, 1552565092)
a.register_event(124, 1552565093)
a.register_event(123, 1552565100)
a.register_event(125, 1552565482)
print(a.query(2, 1552565101))
print(a.query(1, 1552565493))
print(a.query(1, 1552565181))
print(a.query(0, 1552565181))