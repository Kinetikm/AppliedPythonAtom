#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.posts=dict()
        self.follows=dict()
        self.views=dict()

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id in self.posts:
            self.posts[user_id].append(post_id)
        else:
            self.posts[user_id]=list()
            self.posts[user_id].append(post_id)
        self.views[post_id]=set()
        

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id in self.views:
            self.views[post_id].add(user_id)
        else:
            self.views[post_id]=set()
            self.views[post_id].add(user_id)
        

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id in self.follows:
            self.follows[follower_user_id].add(followee_user_id)
        else:
            self.follows[follower_user_id]=set()
            self.follows[follower_user_id].add(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        lists = list()
        for people in self.follows[user_id]:
            if people in self.posts:
                lists+=self.posts[people]
        lists.sort(reverse=True)
        out = lists[:k]
        return out

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        lists = list()
        for posts in self.views:
            lists.append(posts)
        lists.sort(reverse=True)
        #lists.sort()
        lists.sort(key=lambda x: len(self.views[x]),reverse=True)
        return lists[:k]
