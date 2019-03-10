#!/usr/bin/env python
# coding: utf-8


# from homeworks.homework_02.heap import MaxHeap
# from homeworks.homework_02.fastmerger import FastSortedListMerger
import collections


class VKPoster:

    def __init__(self):
        self.user_post = {}
        self.user_read = {}
        self.user_follow = {}
        self.post_readings = collections.Counter()

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id in self.user_post:
            self.user_post[user_id] += [post_id]
        else:
            self.user_post[user_id] = [post_id]

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''

        print(user_id, post_id)

        bl = True
        if user_id in self.user_read:
            if post_id not in self.user_read[user_id]:
                self.user_read[user_id] += [post_id]
            else:
                bl = False
        else:
            self.user_read[user_id] = [post_id]

        if bl:
            if post_id in self.post_readings:
                self.post_readings[post_id] += 1
            else:
                self.post_readings[post_id] = 1

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id in self.user_follow:
            self.user_follow[follower_user_id] += [followee_user_id]
        else:
            self.user_follow[follower_user_id] = [followee_user_id]

    def get_recent_posts(self, user_id: int, k: int)-> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        posts = []
        for followee in self.user_follow[user_id]:
            if followee in self.user_post:
                posts += self.user_post[followee]

        posts = list(dict.fromkeys(posts))
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

        pop_list = []
        pop_dict = dict(self.post_readings.most_common(k))

        for k in sorted(pop_dict.items(), key=lambda x: (-x[1], -x[0])):
            pop_list += [k[0]]
        return pop_list
