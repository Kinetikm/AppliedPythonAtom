import sys
from collections import Counter

import requests
from bs4 import BeautifulSoup
import json
import re
# Ваши импорты


def write_data(href, login, count_):
    return href + ';' + login + ';' + str(count_) + ';\n'


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    # links = sys.argv[1:4]
    links = sys.argv[1]

    r = requests.get(links)

    # soup = BeautifulSoup(, "html.parser")
    #
    # comments_list = soup.find_all('ul', attrs={"id": "comments-list"})
    soup = BeautifulSoup(r.text, "html.parser")

    comment = soup.find_all("div", attrs={"class": "comment"})
    cnt = Counter()
    login_name = {}
    for i in comment:
        commentator_name = i.find('a').find('span').text
        commentator_href = i.find('a')['href']
        if not cnt[commentator_name]:
            cnt[commentator_name] = 0
            login_name[commentator_name] = commentator_href
        cnt[commentator_name] += 1

    # print(cnt)
    # print(login_name)
    with open("top_user_comments.csv", 'w') as csv_file:
        for count_elem in cnt.most_common():
            login = count_elem[0]
            count_ = count_elem[1]
            href = login_name[login]

            csv_file.write(write_data(href, login, count_))
