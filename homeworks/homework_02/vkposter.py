#!/usr/bin/env python
# coding: utf-8


#from homeworks.homework_02.heap import MaxHeap
#from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.users = dict()
        self.posts = dict()

    def user_posted_post(self, user_id: int, post_id: int):
        if post_id not in self.posts.keys():
            self.posts[post_id] = [user_id, []]

    def user_read_post(self, user_id: int, post_id: int):
        if post_id in self.posts.keys():
            if user_id not in self.posts[post_id][1]:
                self.posts[post_id][1].append(user_id)
        if post_id not in self.posts.keys():
            self.posts[post_id] = ["", [user_id]]

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if follower_user_id not in self.users.keys():
            self.users[follower_user_id] = [followee_user_id]
        else:
            self.users[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        list_of_recent_posts = []
        for key, value in self.posts.items():
            if value[0] in self.users[user_id]:
                list_of_recent_posts.append(key)
        list_of_recent_posts.sort(reverse=True)
        return list_of_recent_posts[:k:]

    def get_most_popular_posts(self, k: int) -> list:
        def sort_by_popularity(input):
            return (len(self.posts.get(input)[1]), input)
        list_of_posts = list(self.posts.keys())
        list_of_posts.sort(key=sort_by_popularity, reverse=True)
        return list_of_posts[:k:]
