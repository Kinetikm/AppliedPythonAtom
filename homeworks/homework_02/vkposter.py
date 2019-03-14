#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.user_post = {}
        self.user_follow = {}
        self.posted_posts = {}

    def user_posted_post(self, user_id: int, post_id: int):
        if user_id in self.user_post.keys():
            self.user_post[user_id].append(post_id)
        else:
            self.user_post[user_id] = [post_id]

    def user_read_post(self, user_id: int, post_id: int):
        if post_id in self.posted_posts.keys():
            self.posted_posts[post_id].add(user_id)
        else:
            self.posted_posts[post_id] = set([user_id])


    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if follower_user_id in self.user_follow.keys():
            self.user_follow.get(follower_user_id).append(followee_user_id)
        else:
            self.user_follow[follower_user_id] = [followee_user_id]

    def get_recent_posts(self, user_id: int, k: int) -> list:
        pass
