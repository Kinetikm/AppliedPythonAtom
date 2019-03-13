class VKPoster:

    def __init__(self):
        self.subs = {}
        self.post = {}
        self.autor = {}

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id not in self.post.keys():
            self.post[post_id] = []
            if user_id not in self.autor.keys():
                self.autor[user_id] = [post_id]
            else:
                self.autor[user_id].append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id not in self.post.keys():
            self.user_posted_post(-1, post_id)
        if user_id not in self.post.get(post_id):
            self.post.get(post_id).append(user_id)

    def user_follow_for(self, follower_user_id: int,
                        followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id not in self.subs.keys():
            self.subs[follower_user_id] = [followee_user_id]
        else:
            if followee_user_id not in self.subs[follower_user_id]:
                self.subs[follower_user_id].append(
                    followee_user_id)

    def get_recent_posts(self, user_id: int, k: int) -> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Числоо.
        :param k: Сколько самых свежих постов необходимоо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        new_list = []
        if user_id in self.subs.keys():
            for i in self.subs[user_id]:
                if i in self.autor.keys():
                    new_list += self.autor[i]
        if len(new_list) != 0:
            new_list = sorted(new_list, reverse=True)
        return new_list[:-(len(new_list) - k)]

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Числоо.
        :return: Список из post_id размером К из популярных постов. list
        '''
        pop_list = []
        pop_list = sorted(self.post.keys(),
                          key=lambda ForPost: (len(self.post.get(ForPost)),
                                               ForPost), reverse=True)
        if len(pop_list) > k:
            return pop_list[:-(len(pop_list) - k)]
        elif k <= 0:
            return []
        else:
            return pop_list
