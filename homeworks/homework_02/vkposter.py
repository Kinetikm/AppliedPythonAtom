#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self._posts = {}  # ключ user id, параметры - его посты
        self._read_posts = {}  # ключ-пост, параметры - люди, которые прочитали
        self._followers = {}  # ключ - подписчик, параметры - его подписки

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id in self._posts:
            self._posts[user_id].append(post_id)
        else:
            self._posts[user_id] = list()
            self._posts[user_id].append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id in self._read_posts:
            if self._read_posts[post_id].count(user_id) < 1:
                self._read_posts[post_id].append(user_id)
        else:
            self._read_posts[post_id] = list()
            self._read_posts[post_id].append(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id in self._followers:
            self._followers[follower_user_id].append(followee_user_id)
        else:
            self._followers[follower_user_id] = list()
            self._followers[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        followed = self._followers[user_id]
        posts = list()
        for followed_id in followed:
            if followed_id in self._posts:
                posts = posts + self._posts[followed_id]
        posts.sort(reverse=True)
        return posts[:k]

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        sorted_posts = sorted(self._read_posts.items(),
                              key=lambda x: (len(x[1]), x[0]), reverse=True)
        ret = list()
        if k <= len(sorted_posts):
            pass
        else:
            k = len(sorted_posts)
        for i in range(k):
            ret.append(sorted_posts[i][0])
        return ret
