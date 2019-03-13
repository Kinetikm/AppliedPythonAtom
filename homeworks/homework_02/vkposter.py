#!/usr/bin/env python
# coding: utf-8


# from homeworks.homework_02.heap import MaxHeap
# from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.user_to_post = {}
        self.post_to_user = {}
        self.user__to_user = {}

    def user_posted_post(self, user_id: int, post_id: int):

        if self.user_to_post.get(user_id) is None:
            self.user_to_post[user_id] = {post_id}
        else:
            self.user_to_post[user_id].add(post_id)

    def user_read_post(self, user_id: int, post_id: int):

        if self.post_to_user.get(post_id) is None:
            self.post_to_user[post_id] = {user_id}
        else:
            self.post_to_user[post_id].add(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):

        if self.user__to_user.get(follower_user_id) is None:
            self.user__to_user[follower_user_id] = {followee_user_id}
        else:
            self.user__to_user[follower_user_id].add(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        users = self.user__to_user[user_id]
        posts = set()
        for i in users:
            if self.user_to_post.get(i) is not None:
                posts.update(self.user_to_post[i])
        posts = sorted(posts)
        return list(posts)[::-1][:k]

    def get_most_popular_posts(self, k: int) -> list:

        temp = {}
        for i in self.post_to_user:
            if temp.get(len(self.post_to_user[i])) is None:
                temp[len(self.post_to_user[i])] = [i]
            else:
                temp[len(self.post_to_user[i])].append(i)
        viewlist = sorted(temp)[::-1]
        finlist = []
        for i in viewlist:
            finlist.extend(sorted(temp[i])[::-1])
        return finlist[:k]
