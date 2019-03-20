#!/usr/bin/env python
# coding: utf-8


# from homeworks.homework_02.heap import MaxHeap
# from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.posted_post = {}
        self.read_post = {}
        self.user_follow = {}

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if self.posted_post.get(user_id) is None:
            self.posted_post[user_id] = {post_id}
        else:
            self.posted_post[user_id].add(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if self.read_post.get(post_id) is None:
            self.read_post[post_id] = {user_id}
        else:
            self.read_post[post_id].add(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if self.user_follow.get(follower_user_id) is None:
            self.user_follow[follower_user_id] = {followee_user_id}
        else:
            self.user_follow[follower_user_id].add(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        if self.user_follow.get(user_id) is None:
            return None
        else:
            users = self.user_follow[user_id]
            posts = set()
            for i in users:
                if self.posted_post.get(i) is not None:
                    posts.update(self.posted_post[i])
            posts = sorted(posts)
            return (list(posts)[::-1][:k])

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        tempmap = {}
        for i in self.read_post:
            if tempmap.get(len(self.read_post[i])) is None:
                tempmap[len(self.read_post[i])] = [i]
            else:
                tempmap[len(self.read_post[i])].append(i)
        viewlist = sorted(tempmap)[::-1]
        finlist = []
        for i in viewlist:
            finlist.extend(sorted(tempmap[i])[::-1])
        return finlist[:k]
