#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict

from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.users = defaultdict(set)
        self.subscriptions = defaultdict(set)
        self.posts = defaultdict(lambda: dict(owner=None, users_viewed=set()))

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id in self.posts:
            return
        self.posts[post_id]['owner'] = user_id
        self.users[user_id].add(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id not in self.posts:
            self.user_posted_post(-1, post_id)
        self.posts[post_id]['users_viewed'].add(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        self.subscriptions[follower_user_id].add(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        return FastSortedListMerger.merge_first_k(
            [sorted(self.users[follower]) for follower
             in self.subscriptions[user_id]], k)

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        h = MaxHeap([(len(spec["users_viewed"]), post_id) for post_id, spec
                     in self.posts.items()])
        res = []
        for _ in range(k):
            try:
                res.append(h.extract_maximum()[1])
            except IndexError:
                break
        return res
