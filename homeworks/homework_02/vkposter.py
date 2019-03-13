#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.all_posts = {}
        self.posts_of_each_user = {}
        self.subscriptions = {}
        self.read_by_user = {}
    #    raise NotImplementedError

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id not in self.all_posts:
            self.all_posts[post_id] = []
        if user_id not in self.posts_of_each_user:
            self.posts_of_each_user[user_id] = []
        if post_id not in self.posts_of_each_user[user_id]:
            self.posts_of_each_user[user_id].append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id not in self.all_posts:
            self.all_posts[post_id] = []
        if user_id not in self.all_posts[post_id]:
            (self.all_posts[post_id]).append(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if followee_user_id not in self.subscriptions:
            self.subscriptions[followee_user_id] = []
        if follower_user_id not in self.read_by_user:
            self.read_by_user[follower_user_id] = []
        if follower_user_id not in self.subscriptions[followee_user_id]:
            (self.subscriptions[followee_user_id]).append(follower_user_id)
        if followee_user_id not in self.read_by_user[follower_user_id]:
            (self.read_by_user[follower_user_id]).append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        list_of_lists = []
        output_list = []
        if user_id not in self.read_by_user.keys():
            return output_list
        for followee in self.read_by_user[user_id]:
            if followee not in self.posts_of_each_user:
                continue
            list_of_lists.append(self.posts_of_each_user[followee])
        output_list = FastSortedListMerger.merge_first_k(list_of_lists, k)
        return output_list

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        post_tuple_list = []
        output = []
        for post in self.all_posts.keys():
            post_tuple_list.append((len(self.all_posts[post]), post))
        post_heap = MaxHeap(post_tuple_list)
        for i in range(0, k):
            try:
                max_el = post_heap.extract_maximum()
            except IndexError:
                break
            output.append(max_el[1])
        return output
