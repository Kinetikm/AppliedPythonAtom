#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.PostedPosts = {}
        self.ReadPosts = {}
        self.FolUsers = {}
        raise NotImplementedError

    def value_check(self, dic: dict, key: int):
        try:
            if isinstance(dic[key], int):
                return 1
            elif isinstance(dic[key], list):
                return 2
        except KeyError:
            return 3

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if value_check(self.PostedPosts, user_id) == 1:
            self.PostedPosts.setdefault(user_id, post_id)
        elif value_check(self.PostedPosts, user_id) == 2:
            self.PostedPosts[user_id].append(post_id)
        else:
            self.PostedPosts[user_id] = [self.PostedPosts[user_id], post_id]

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if value_check(self.ReadPosts, post_id) == 1:
            self.ReadPosts.setdefault(post_id, user_id)
        elif value_check(self.ReadPosts, post_id) == 2:
            self.ReadPosts[post_id].append(user_id)
        else:
            self.ReadPosts[post_id] = [self.ReadPosts[post_id], user_id]

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if value_check(self.FolUsers, follower_user_id) == 1:
            self.FolUsers.setdefault(follower_user_id, followee_user_id)
        elif value_check(self.FolUsers, follower_user_id) == 2:
            self.FolUsers[follower_user_id].append(followee_user_id)
        else:
            self.FolUsers[follower_user_id] = \
                [self.FolUsers[follower_user_id], followee_user_id]

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        Output = []
        try:
            for followee in self.FolUsers[user_id]:
                if value_check(self.PostedPosts, followee) == 1:
                    self.Output.append(self.PostedPosts[followee])
                elif value_check(self.PostedPosts, followee) == 2:
                    Output += self.PostedPosts[followee]
            return sorted(Output, reverse=True)[:k]
        except KeyError:
            print('Incorrect user id')

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        lst = []
        for post in self.ReadPosts.keys():
            lst.append([post, len(set(self.ReadPosts[post]))])
        N = []
        bank = set()
        for i in range(len(lst)):
            index = 0
            ll = []
            for j in range(len(lst) - 1, i - 1, -1):
                if lst[i][1] == lst[j][1] and i != j:
                    ll.append(lst[j][0])
                    bank.add(lst[j][1])
                    index += 1
                elif i == j and index > 0:
                    ll.append(lst[j][0])
                    N.append([ll, lst[i][1]])
                elif i == j and index == 0 and lst[j][1] not in bank:
                    N.append([lst[i][0], lst[i][1]])
        P = {}
        for i in range(len(N)):
            P.setdefault(N[i][1], sorted(N[i][0], reverse=True))
        Output = []
        for key in sorted(P.keys()):
            try:
                if k - len(P[key]) >= 0:
                    Output += P[key]
                    k -= len(P[key])
                else:
                    Output += P[key][:k]
                    break
            except TypeError:
                if k > 0:
                    Output.append(P[key])
                    k -= 1
                else:
                    break

        return Output
