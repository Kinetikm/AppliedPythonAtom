#!/usr/bin/env python
# coding: utf-8


class VKPoster:

    def __init__(self):
        self.readed_post = {}  # прочитанные посты
        self.reposted_post = {}  # репостнутые посты
        self.followers = {}  # кто на кого подписан
        self.number_read = {}  # количество просмотров

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id in self.reposted_post:
            self.reposted_post[user_id].append(post_id)
        else:
            self.reposted_post.update({user_id: [post_id]})

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id in self.read_post:
            if post_id not in self.readed_post[user_id]:
                self.readed_post[user_id].append(post_id)
                if post_id not in self.number_readt:
                    self.number_read.update({post_id: 1})
                else:
                    self.number_read[post_id] = self.number_read[post_id] + 1
        else:
            self.readed_post.update({user_id: [post_id]})
            if post_id not in self.readlist:
                self.number_read.update({post_id: 1})
            else:
                self.number_read[post_id] = self.readlist[post_id] + 1

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id in self.followers:
            self.followers[follower_user_id].append(followee_user_id)
        else:
            self.followers.update({follower_user_id: [followee_user_id]})

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        out = []
        if user_id in self.followers:
            for user in self.followers[user_id]:
                if user in self.reposted_post:
                    for post in self.reposted_post[user]:
                        if post not in out:
                            out.append(post)
            out = sorted(out, reverse=True)
            out = out[:min(k, len(self.number_read))]
            return out
        return []

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        out = []
        tmp = sorted(self.number_read.items(),
                     key=lambda m: (m[1], m[0]), reverse=True)
        for i in range(min(k, len(self.number_read))):
            out.append(tmp[i][0])
        return out
