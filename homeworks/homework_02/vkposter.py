#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.user_posted_post=dict()
        self.user_read_post=dict()
        self.user_follow_for=dict()
        
    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        ''' 
        if self.user_posted_post.get(user_id):
            self.user_posted_post[user_id].append(post_id)
        else: self.user_posted_post[user_id]=[post_id]

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if self.user_read_post.get(user_id):
            self.user_read_post[user_id].append(post_id)
        else: self.user_read_post[user_id]=[post_id]

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if self.user_follow_post.get(follower_user_id):
            self.user_follow_post[follower_user_id].append(followee_user_id)
        else: self.user_follow_post[follower_user_id]=[followee_user_id]

    def get_recent_posts(self, user_id: int, k: int)-> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        l=[]
        for followee_user_id in self.user_follow_for[user_id]:    
            for i in range(k):
                if self.user_posted_post.get(followee)!= defaut:
                    l.append(sorted(self.user_posted_post[followee]))
        return l

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        d={}
        a={}
        for user_id in user_read_post:
            for post_id in user_read_post[user_id]:
                if user_read_post.items() not in d:
                    d.append(user_read_post.items())
        for post_id in d[user_id]:
            for user_id in user_read_post:
                if post_id not in a:
                    a[post_id]=1
                else: a[post_id]+=1
        for post_id in a[post_id]:
                b.append(sorted(a.values())
        return b