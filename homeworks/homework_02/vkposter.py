#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_02.heap_delete import MaxHeap1
from homeworks.homework_02.fastmerger import FastSortedListMerger
from collections import defaultdict
from collections import OrderedDict


class User:

    def __init__(self, user_id: int):
        self.read_posts = []
        self.posts = []
        self.tracked_users = []
        self.user_id = user_id

    def follow_user(self, user_id: int):
        self.tracked_users.append(user_id)

    def posted_post(self, post_id: int):
        self.posts.append(post_id)

    def read_post(self, post_id: int) -> bool:
        if post_id in self.read_posts:
            return False
        else:
            self.read_posts.append(post_id)
            return True


class VKPoster:

    def __init__(self):
        self.users = defaultdict(User)
        self.posts = {}

    def __user_check(self, user_id: int):
        if user_id not in self.users:
            self.users[user_id] = User(user_id)

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''

        self.__user_check(user_id)
        user = self.users.get(user_id)
        user.posted_post(post_id)
        if post_id not in self.posts:
            self.posts[post_id] = 0

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''

        if post_id not in self.posts:
            self.posts[post_id] = 0
        self.__user_check(user_id)
        user = self.users.get(user_id)
        if user.read_post(post_id):
            self.posts[post_id] += 1

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''

        self.__user_check(followee_user_id)
        self.__user_check(follower_user_id)
        user = self.users.get(follower_user_id)
        user.follow_user(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        self.__user_check(user_id)
        user = self.users.get(user_id)
        posts = []
        for followee_user in user.tracked_users:
            posts.extend([x for x in self.users[followee_user].posts if
                          x not in user.read_posts][-k:])
        posts.sort()
        answer = posts[-k:]
        answer.reverse()
        return answer

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        heap = MaxHeap1([(v, k) for k, v in self.posts.items()])
        __posts_for_print = []
        for i in range(k):
            __posts_for_print.append(MaxHeap1.extract_maximum(heap)[1])
        return __posts_for_print
