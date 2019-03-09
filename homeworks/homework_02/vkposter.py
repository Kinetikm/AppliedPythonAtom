#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.read_post = {}
        self.repost_post = {}
        self.followers = {}
        self.readlist = {}

    def user_posted_post(self, user_id: int, post_id: int):

        if user_id in self.repost_post:
            self.repost_post[user_id].append(post_id)
        else:
            self.repost_post.update({user_id: [post_id]})

    def user_read_post(self, user_id: int, post_id: int):

        if user_id in self.read_post:
            if post_id not in self.read_post[user_id]:
                self.read_post[user_id].append(post_id)
                if post_id in self.readlist:
                    self.readlist[post_id] = self.readlist[post_id] + 1
                else:
                    self.readlist.update({post_id: 1})
        else:
            self.read_post.update({user_id: [post_id]})
            if post_id in self.readlist:
                self.readlist[post_id] = self.readlist[post_id] + 1
            else:
                self.readlist.update({post_id: 1})

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):

        if follower_user_id in self.followers:
            self.followers[follower_user_id].append(followee_user_id)
        else:
            self.followers.update({follower_user_id: [followee_user_id]})

    def get_recent_posts(self, user_id: int, k: int)-> list:

        out_list = []
        out_list1 = []
        if user_id in self.followers:
            for user in self.followers[user_id]:
                if user in self.repost_post:
                    for post in self.repost_post[user]:
                        if post not in out_list:
                            out_list.append(post)
            length_list = min(k, len(out_list))
            out_list = sorted(out_list, reverse=True)
            for i in range(length_list):
                out_list1.append(out_list[i])
            return out_list1
        return out_list

    def get_most_popular_posts(self, k: int) -> list:

        out_list = []
        length_list = min(k, len(self.readlist))
        inverse = sorted(self.readlist.items(),
                         key=lambda m: (m[1], m[0]), reverse=True)
        for i in range(length_list):
            out_list.append(inverse[i][0])
        return out_list
