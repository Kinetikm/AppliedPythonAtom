#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger
import collections


class VKPoster:

    def __init__(self):
        self.read_post = dict()
        self.follow = dict()
        self.pub_post = dict()

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id not in self.pub_post:
            self.pub_post.setdefault(user_id, [])
            self.pub_post[user_id].append(post_id)
        else:
            self.pub_post.setdefault(user_id, [])
            self.pub_post[user_id].append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id not in self.read_post:
            self.read_post.setdefault(user_id, [])
            self.read_post[user_id].append(post_id)
        else:
            buf = list(self.read_post.pop(user_id))
            if post_id in buf:
                self.read_post[user_id] = buf
            else:
                buf.append(post_id)
                self.read_post[user_id] = buf

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id not in self.follow:
            self.follow.setdefault(follower_user_id, [])
            self.follow[follower_user_id].append(followee_user_id)
        else:
            self.follow.setdefault(follower_user_id, [])
            self.follow[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        recent = list()
        follow = list(self.follow.get(user_id))
        for user in follow:
            if user in self.pub_post:
                recent.extend(self.pub_post.get(user))
        recent.sort()
        recent = recent[-k:]
        recent = recent[::-1]
        return recent

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''

        if k <= 0:
            return None
        else:
            bufer = []
            most_read_l = list()
            most_read = dict()
            for user in self.read_post:
                most_read_l.extend(self.read_post.get(user))

            most_read_l.sort()

            most_read = dict.fromkeys(most_read_l, 0)
            for p_id in most_read_l:
                if p_id in most_read:
                    i = most_read.get(p_id) + 1
                    most_read[p_id] = i
            bufer = list(most_read.items())
            bufer = sorted(bufer,
                           reverse=True,
                           key=lambda var: (var[1], var[0]))
            bufer = [var[0] for var in bufer]
            most_read_l.clear()
            most_read_l = bufer[:k]
            return most_read_l
