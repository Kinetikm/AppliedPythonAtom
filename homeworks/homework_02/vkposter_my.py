#!/usr/bin/env python
# coding: utf-8


# from .heap import MaxHeap
# from .fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.user_to_post_add = {}
        self.post_to_user_read = {}
        self.user_to_user = {}

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''

        if self.user_to_post_add.get(user_id) is None:
            self.user_to_post_add[user_id] = {post_id}
        else:
            self.user_to_post_add[user_id].add(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''

        if self.post_to_user_read.get(post_id) is None:
            self.post_to_user_read[post_id] = {user_id}
        else:
            if self.post_to_user_read.get(post_id).count(user_id) == 0:
                self.post_to_user_read[post_id].add(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''

        if self.user_to_user.get(followee_user_id) is None:
            self.user_to_user[followee_user_id] = {follower_user_id}
        else:
            self.user_to_user[followee_user_id].add(follower_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''

        get_followers = []
        recent_posts = []

        for i in self.user_to_user[user_id]:
            get_followers.append(i)

        for i in get_followers:
            recent_posts += self.user_to_post_add[i]

        return sorted(recent_posts)[-k:]

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''

        popularity_counter = {}

        for i in self.post_to_user_read:
            counter = len(self.post_to_user_read[i])
            popularity_counter[i] = counter

        print("popularity_counter", popularity_counter)

        popular_posts = []

        for i in sorted(popularity_counter.items(), key=lambda item: item[1]):
            popular_posts.append(i[0])

        return popular_posts[-k:]
