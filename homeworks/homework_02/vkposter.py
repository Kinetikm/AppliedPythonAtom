#!/usr/bin/env python
# coding: utf-8


class VKPoster:

    def __init__(self):
        self.readed_post = {}
        self.posted_post = {}
        self.user_followers = {}
        self.readlist = {}

    def user_posted_post(self, user_id: int, post_id: int):

        if user_id in self.posted_post:
            self.posted_post[user_id].append(post_id)
        else:
            self.posted_post.update({user_id: [post_id]})

    def user_read_post(self, user_id: int, post_id: int):

        if user_id in self.readed_post:
            if post_id not in self.readed_post[user_id]:
                self.readed_post[user_id].append(post_id)
                if post_id in self.readlist:
                    self.readlist[post_id] = self.readlist[post_id] + 1
                else:
                    self.readlist.update({post_id: 1})
        else:
            self.readed_post.update({user_id: [post_id]})
            if post_id in self.readlist:
                self.readlist[post_id] = self.readlist[post_id] + 1
            else:
                self.readlist.update({post_id: 1})

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if follower_user_id in self.followers:
            self.user_followers[follower_user_id].append(followee_user_id)
        else:
            self.user_followers.update({follower_user_id: [follower_user_id]})

    def get_recent_posts(self, user_id: int, k: int) -> list:
        tmp_list = []
        tmp_list2 = []
        if user_id in self.followers:
            for user in self.followers[user_id]:
                if user in self.posted_post:
                    for post in self.posted_post[user]:
                        if post not in tmp_list:
                            tmp_list.append(post)
            length_list = min(k, len(tmp_list))
            out_list = sorted(tmp_list, reverse=True)
            for i in range(length_list):
                tmp_list2.append(out_list[i])
            return tmp_list2
        return tmp_list

    def get_most_popular_posts(self, k: int) -> list:
        tmp_list = []
        length_list = min(k, len(self.readlist))
        inverse = sorted(self.readlist.items(),
                         key=lambda m: (m[1], m[0]), reverse=True)
        for i in range(length_list):
            tmp_list.append(inverse[i][0])
        return tmp_list
