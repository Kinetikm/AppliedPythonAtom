#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self._user_posts = {}
        self._followed_for = {}
        self._posted_posts = {}

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id not in self._posted_posts.keys():
            self._posted_posts[post_id] = [user_id, []]
        if user_id not in self._user_posts.keys():
            self._user_posts[user_id] = [post_id]
        else:
            if post_id not in self._user_posts.get(user_id):
                self._user_posts.get(user_id).append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id in self._posted_posts:
            if user_id not in self._posted_posts[post_id][1]:
                self._posted_posts[post_id][1].append(user_id)
        if post_id not in self._posted_posts:
            self._posted_posts[post_id] = ["", [user_id]]

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id not in self._followed_for.keys():
            self._followed_for[follower_user_id] = [followee_user_id]
        else:
            self._followed_for.get(follower_user_id).append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        heap_sort = True
        if heap_sort:
            return FastSortedListMerger.merge_first_k(
                [self._user_posts.get(i)for i in
                 self._followed_for.get(user_id) if i in
                 self._user_posts.keys()], k)
        else:
            recent_posts = []
            for key, value in self._posted_posts.items():
                if value[0] in self._followed_for[user_id]:
                    recent_posts.append(key)
            recent_posts.sort()
            recent_posts.reverse()
            return recent_posts[:k]

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        heap_sort = True
        if heap_sort:
            lists = [(len(self._posted_posts.get(i)[1]), i)
                     for i in list(self._posted_posts.keys())]
            heap = MaxHeap(lists)
            return [heap.extract_maximum()[1] for i in range(k)]
        else:
            sort_posts = list(self._posted_posts.keys())
            sort_posts.sort(key=lambda i: (
                len(self._posted_posts.get(i)[1]), i), reverse=True)
            return sort_posts[:k]
