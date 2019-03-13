#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.posts = {}
        self.subs = {}

    def user_posted_post(self, user_id: int, post_id: int):
        if post_id not in self.posts:
            self.posts[post_id] = [user_id, []]

    def user_read_post(self, user_id: int, post_id: int):
        if post_id in self.posts.keys():
            if user_id not in self.posts[post_id][1]:
                self.posts[post_id][1].append(user_id)
        else:
            self.posts[post_id] = [[], [user_id]]

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if follower_user_id not in self.subs.keys():
            self.subs[follower_user_id] = [followee_user_id]
        else:
            if followee_user_id not in self.subs.get(follower_user_id):
                self.subs[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        res_list = []
        if user_id in self.subs.keys():
            for post in sorted(list(self.posts.keys()), reverse=True):
                if self.posts[post][0] in self.subs[user_id]:
                    if user_id not in self.posts[post][1]:
                        res_list.append(post)
                    if len(res_list) == k:
                        return res_list
        return res_list

    def get_most_popular_posts(self, k: int) -> list:
        if k <= 0:
            return []
        popular = [(k, len(self.posts[k][1])) for k in
                   sorted(self.posts, key=lambda i:
                   len(self.posts.get(i)[1]), reverse=True)]
        res_list = []
        group_ind = popular[0][1]
        while len(res_list) != k:
            found = []
            for elem in popular:
                if elem[1] == group_ind:
                    found.append(elem[0])
            if len(found) == 0:
                group_ind -= 1
                continue
            found = sorted(found, reverse=True)
            for elem in found:
                res_list.append(elem)
                if len(res_list) == k:
                    break
            group_ind -= 1
            if len(res_list) == len(popular):
                break
        return res_list


