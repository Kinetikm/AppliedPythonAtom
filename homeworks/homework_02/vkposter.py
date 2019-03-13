#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.author = {}
        self.follower = {}
        self.post = {}
        raise NotImplementedError

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id in self.author.keys():
            self.author[user_id].append(post_id)
        else:
            self.author[user_id] = [post_id]
        pass

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id in self.post.keys():
            self.post[user_id].add(post_id)
        else:
            self.post[user_id] = set([post_id])
        pass

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id in self.follower.keys():
            self.follower[follower_user_id].append(followee_user_id)
        else:
            self.follower[follower_user_id] = [followee_user_id]
        pass

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        follower_post_id = []
        while follower_user_id in self.follower[user_id]:
            while post_id in self.author[follower_post_id]:
                follower_post_id = follower_post_id + self.author[post_id]
        follower_post_id.reverse()
        return follower_post_id[:k:]
        pass

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        count_read = []
        post = []
        while post_id in self.post.keys():
            count_read.append((len(self.post[post_id]), post_id))
            count_read.reverse()
            for i in range(k):
                post.append(count_read[i][1])
            post.sort()
            return post[:k:]
        pass
