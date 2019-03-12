#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.__follows = {}
        self.__userPosts = {}
        self.__postReadUsers = {}


    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        try:
            self.__userPosts[user_id].append(post_id)
        except KeyError:
            self.__userPosts[user_id] = [post_id]
        self.__postReadUsers[post_id] = []
        return None

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        try:
            self.__postReadUsers[post_id].index(user_id)
        except ValueError:
            self.__postReadUsers[post_id].append(user_id)
        except KeyError:
            self.__postReadUsers[post_id] = [user_id]
        return None

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        try:
            self.__follows[follower_user_id].append(followee_user_id)
        except KeyError:
            self.__follows[follower_user_id] = [followee_user_id]
        return None

    def get_recent_posts(self, user_id: int, k: int)-> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        postsForUser = []
        try:
            for user in self.__follows[user_id]:
                try:
                    postsForUser = postsForUser + self.__userPosts[user]
                except KeyError:
                    pass
        except KeyError:
            return []
        postsForUser = sorted(postsForUser)
        recentPosts = []
        for i in range(k):
            try:
                recentPosts.append(postsForUser.pop())
            except IndexError:
                return recentPosts
        return recentPosts

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        maxLen = 0
        inverted_dict = {}
        posts = []
        topPosts = []
        for key in self.__postReadUsers:
            try:
                inverted_dict[len(self.__postReadUsers[key])].append(key)
            except KeyError:
                inverted_dict[len(self.__postReadUsers[key])] = [key]
            if len(self.__postReadUsers[key]) > maxLen:
                maxLen = len(self.__postReadUsers[key])
        for key in range(maxLen + 1):
            try:
                posts = posts + sorted(inverted_dict[key])
            except KeyError:
                pass
        for i in range(k):
            topPosts.append(posts.pop())
        return topPosts