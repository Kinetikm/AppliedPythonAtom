#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger
import collections


class VKPoster:

    def __init__(self):
        self.published_posts = dict()
        self.read_posts = dict()
        self.followers = dict()

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id not in self.published_posts:
            self.published_posts.setdefault(user_id, [])
            self.published_posts[user_id].append(post_id)
        else:
            self.published_posts.setdefault(user_id, [])
            self.published_posts[user_id].append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id not in self.read_posts:
            self.read_posts.setdefault(user_id, [])
            self.read_posts[user_id].append(post_id)
        else:
            buf = list(self.read_posts.pop(user_id))
            if post_id in buf:
                self.read_posts[user_id] = buf
            else:
                buf.append(post_id)
                self.read_posts[user_id] = buf

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id not in self.followers:
            self.followers.setdefault(follower_user_id, [])
            self.followers[follower_user_id].append(followee_user_id)
        else:
            self.followers.setdefault(follower_user_id, [])
            self.followers[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        recent_posts = list()
        follow = list(self.followers.get(user_id))
        for user in follow:
            if user in self.published_posts:
                recent_posts.extend(self.published_posts.get(user))
        # buf = recent_posts
        # recent_posts.clear()
        # for i in range(k + 1):
        #     recent_posts.append(buf[i])
        recent_posts.sort()
        recent_posts = recent_posts[-k:]
        recent_posts = recent_posts[::-1]
        return recent_posts

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
            buf_list = []
            most_read_list = list()
            most_read = dict()
            for user in self.read_posts:
                most_read_list.extend(self.read_posts.get(user))

            most_read_list.sort()

            most_read = dict.fromkeys(most_read_list, 0)
            for p_id in most_read_list:
                if p_id in most_read:
                    counter = most_read.get(p_id) + 1
                    most_read[p_id] = counter
            buf_list = list(most_read.items())
            buf_list = sorted(buf_list, reverse=True,
                              key=lambda var: (var[1], var[0]))
            buf_list = [var[0] for var in buf_list]
            most_read_list.clear()
            most_read_list = buf_list[:k]
            return most_read_list
