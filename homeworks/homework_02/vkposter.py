#!/usr/bin/env python
# coding: utf-8


class VKPoster:

    def __init__(self):
        self.posts = {}
        self.follows = {}

    def user_posted_post(self, user_id: int, post_id: int):
        if post_id not in self.posts:
            self.posts[post_id] = [user_id, []]

    def user_read_post(self, user_id: int, post_id: int):
        if post_id in self.posts.keys():
            if user_id not in self.posts[post_id][1]:
                self.posts[post_id][1].append(user_id)
        else:
            self.posts[post_id] = [0, [user_id]]

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if follower_user_id in self.follows.keys():
            if followee_user_id not in self.follows[follower_user_id]:
                self.follows[follower_user_id].append(followee_user_id)
        else:
            self.follows[follower_user_id] = [followee_user_id]

    def get_recent_posts(self, user_id: int, k: int)-> list:
        last_k = []
        if user_id in self.follows.keys():
            temp = sorted(self.posts.keys(), reverse=True)
            for post in temp:
                if self.posts[post][0] in self.follows[user_id]:
                    if (user_id not in self.posts[post][1]):
                        if (len(last_k) == k):
                            return last_k
                        last_k.append(post)
        return last_k

    def get_most_popular_posts(self, k: int) -> list:
        temp = sorted(self.posts.items(),
                      key=lambda x: len(x[1][1]), reverse=True)
        for i in range(len(temp)):
            for j in range(len(temp)-1):
                if ((temp[j][0] < temp[j+1][0]) and
                        (len(temp[j][1][1]) == len(temp[j+1][1][1]))):
                    temp[j], temp[j+1] = temp[j+1], temp[j]
        res = []
        for post in temp:
            if (k == len(res)):
                return res
            else:
                res.append(post[0])
        return res
