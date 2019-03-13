#!/usr/bin/env python
# coding: utf-8


class VKPoster:

    def __init__(self):
        # user_id:{'posts':[(id созд. постов)], 'follow':[(id user'ов)]}
        self.users_dict = {}
        # содержат id user'ов в виде: post_id:set of user ids
        self.readed_posts = {}

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if self.users_dict.get(user_id, False):
            self.users_dict.get(user_id)['posts'].append(post_id)
        else:
            self.users_dict[user_id] = {'posts': [post_id], 'follow': []}

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if self.readed_posts.get(post_id, False):
            self.readed_posts.get(post_id).add(user_id)
        else:
            self.readed_posts[post_id] = set([user_id])

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if self.users_dict.get(follower_user_id, False):
            self.users_dict.get(follower_user_id)['follow'].append(
                followee_user_id)
        else:
            self.users_dict[follower_user_id] =\
                {'posts': [], 'follow': [followee_user_id]}

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        if k >= 0:
            posts_newest = []
            for followee in self.users_dict[user_id]['follow']:
                try:  # если такого id нет
                    posts_newest.extend(
                        self.users_dict.get(followee, [])['posts'])
                except:
                    continue

            return sorted(posts_newest, reverse=True)[:k]
        else:
            return []

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        if k >= 0:
            # сортируем от наиболее до наименее популярного
            buf = sorted(self.readed_posts, reverse=True)
            buf = sorted(buf, key=lambda rp: len(self.readed_posts[rp]),
                         reverse=True)
            return buf[:k]
        else:
            return []
