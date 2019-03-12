#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        """
        users (user_id):
            f_ids: []   - подписан на
            p_ids: []   - посты (созданные)

        posts (post_id):
                   {}  - уникальные просмотревшие
        """
        self.users = {}
        self.posts = {}

    def user_posted_post(self, user_id: int, post_id: int):
        """
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        """
        self.users.setdefault(user_id, {'p_ids': [], 'f_ids': []})['p_ids']\
            .append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        """
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        """
        self.posts.setdefault(post_id, set()).add(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        """
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        """
        self.users.setdefault(follower_user_id,
                              {'p_ids': [], 'f_ids': []}
                              )['f_ids'].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int,
                         fast_sorted: bool = True) -> list:
        """
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :param fast_sorted: Использовать ли FastSortedListMerger
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        """
        # Реализация через FastSortedListMerger
        if fast_sorted:
            posts = [self.users[folowee]['p_ids']
                     for folowee in self.users[user_id]['f_ids']]
            return FastSortedListMerger.merge_first_k(posts, k)

        # если пользователя не существует будет выброшена ошибка KeyError
        # по подпискам собираем список уникальных идентификаторов постов
        # уникальность за счёт того что автор поста всегда один
        posts = [post
                 for folowee in self.users[user_id]['f_ids']
                 for post in self.users[folowee]['p_ids']]
        # сортируем по убыванию и отдаём первые k
        return sorted(posts, reverse=True)[:k]

    def get_most_popular_posts(self, k: int,
                               fast_sorted: bool = True) -> list:
        """
        Метод который возвращает список k самых популярных постов за все время,
        отсортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :param fast_sorted: Использовать ли FastSortedListMerger
        :return: Список из post_id размером К из популярных постов. list
        """
        # Реализация через FastSortedListMerger - O(N + k * log N)
        if fast_sorted:
            # формирование списка кортежей (популярность, post_id)
            full_list = [(len(val), key) for key, val in self.posts.items()]

            # отдавать не больше чем есть
            if k > len(full_list):
                k = len(full_list)

            h = MaxHeap(full_list)
            first_k = []
            for i in range(k):
                first_k.append(h.extract_maximum()[1])

            return first_k

        # сортируем посты по убыванию post_id - O(N * log N)
        fresh_posts = sorted(self.posts, reverse=True)
        # получаем k постов по их популярности (count) - O(N * log N)
        return sorted(fresh_posts, key=lambda post: len(self.posts[post]),
                      reverse=True)[:k]
