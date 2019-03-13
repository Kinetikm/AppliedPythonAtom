#!/usr/bin/env python
# coding: utf-8


class VKPoster:
    # Key: post_id, Value: user_id
    read_post = {}
    # Key: user_id, Value: post_id
    posted_post = {}
    # Key: follower_user_id, Value: followee_user_id
    follow_for = {}

    def __init__(self):
        self.read_post.clear()
        self.posted_post.clear()
        self.read_post.clear()

    def user_posted_post(self, user_id: int, post_id: int):
        fill_dict(self.posted_post, user_id, post_id)
        return

    def user_read_post(self, user_id: int, post_id: int):
        print('user_id', user_id)
        print('post_id', post_id)
        if self.read_post.get(post_id):
            if self.read_post.get(post_id).count(user_id) == 0:
                fill_dict(self.read_post, post_id, user_id)
        else:
            fill_dict(self.read_post, post_id, user_id)

        return

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        fill_dict(self.follow_for, follower_user_id, followee_user_id)
        return

    def get_recent_posts(self, user_id: int, k: int)-> list:
        i = 0
        res = []
        ff = self.follow_for.get(user_id)
        if self.posted_post.get(ff[i]) is not None:
            while i < len(ff):
                res.extend(self.posted_post.get(ff[i]))
                i += 1
        res = sorted(res, reverse=True)[0:k]
        return res

    def get_most_popular_posts(self, k: int) -> list:
        print('k', k)
        print('rr', self.read_post)
        res0 = sorted(self.read_post.items(),
                      key=lambda kv: (len(kv[1]), kv[0]), reverse=True)
        res = ([x for x, y in res0])[0:k]
        print('res', res)
        return res


def fill_dict(dictionary: dict, key: int, value: int):
    cur = dictionary.pop(key, None)
    if cur:
        if isinstance(cur, list):
            dictionary[key] = cur + [value]
        else:
            dictionary[key] = [cur, value]
    else:
        dictionary[key] = [value]
    return
