#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        # словарь, ключами которого являются id пользователей, а значенями -
        # списки с id пользователей, на которых они подписаны
        self.users = {}
        # словарь, ключами которого являются id постов, а значениями -
        # списки с id пользователей, которые его прочитали, причем
        # на первом месте стоит создатель поста
        self.posts = {}
        raise NotImplementedError

    def create_new_user(self, user_id):
        self.users.update({user_id: []})

    def user_posted_post(self, user_id: int, post_id: int):
        # проверка на существование данного пользователя в базе
        if self.users.get(user_id) is None:
            self.create_new_user(user_id)

        self.posts.update({post_id: []})

    def user_read_post(self, user_id: int, post_id: int):
        # проверка на существование данного поста в базе
        if self.posts.get(post_id) is None:
            self.posts.update({post_id: ['somebody']})

        self.posts[post_id].append(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        # проверка на существование данных пользователей в базе
        if self.users.get(follower_user_id) is None:
            self.create_new_user(follower_user_id)
        if self.users.get(follower_user_id) is None:
            self.create_new_user(followee_user_id)

        self.users[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        help_list = []
        result_list = []
        # перебираем все существующие посты
        for i in self.posts.keys():
            # пробуем найти id создателя очередного поста в списке подписок
            # пользователя, сделавшего запрос
            try:
                self.users[user_id].index(self.posts[i][0])
            except ValueError:  # id не найден
                pass
            else:  # id найден, т.е. пользователь подписан на создателя поста
                # пробуем найти id пользователя в списке прочитавших пост
                try:
                    self.posts[i].index(user_id)
                except ValueError:  # пользователь не читал пост
                    # добавляем кортеж, 0-ым элементом которого является
                    # число прочитавших пост, а 1-ым - id поста
                    help_list.append((len(self.posts[i])-1, i))
        # преобразуем полученный список в кучу
        h = MaxHeap(help_list)
        i = 0
        while i < k:
            result_list.append(h.extract_maximum()[1])
            i += 1
        return result_list

    def get_most_popular_posts(self, k: int) -> list:
        help_list = []
        result_list = []
        # перебираем все существующие посты
        for i in self.posts.keys():
            # добавляем кортеж, 0-ым элементом которого является
            # число прочитавших пост, а 1-ым - id поста
            help_list.append((len(self.posts[i])-1, i))
        # преобразуем полученный список в кучу
        h = MaxHeap(help_list)
        while i < k:
            result_list.append(h.extract_maximum()[1])
            i += 1
        return result_list
