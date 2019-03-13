#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.posts = {}
        self.posts_readed = {}
        self.sort_posts = {}
        self.subscriptions = {}

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id in self.posts.keys():
            self.posts[user_id].append(post_id)
        else:
            self.posts[user_id] = [post_id]
        if post_id not in self.posts_readed.keys():
            self.posts_readed[post_id] = []
        if post_id not in self.sort_posts.keys():
            self.sort_posts[post_id] = 0

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id in self.posts_readed.keys():
            if user_id not in self.posts_readed[post_id]:
                self.posts_readed[post_id].append(user_id)
                self.sort_posts[post_id] += 1
        else:
            self.posts_readed[post_id] = [user_id]
            self.sort_posts[post_id] = 1

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id in self.subscriptions.keys():
            self.subscriptions[follower_user_id].append(followee_user_id)
        else:
            self.subscriptions[follower_user_id] = [followee_user_id]

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        fresh_list = []
        try:
            for subscriptions in self.subscriptions[user_id]:
                if subscriptions in self.posts.keys():
                    fresh_list.extend(self.posts[subscriptions])
        except KeyError:
            pass
        finally:
            return FastSortedListMerger.merge_first_k(fresh_list, k)

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        result_list = []
        list_for_heap = []
        if k < len(self.sort_posts) and k != 0:
            length = k
        else:
            length = len(self.sort_posts)
        for posts, reads in self.sort_posts.items():
            list_for_heap.append((reads, posts))
        h = MaxHeap(list_for_heap)
        while len(result_list) != length:
            reads, post = h.extract_maximum()
            result_list.append(post)
        return result_list
