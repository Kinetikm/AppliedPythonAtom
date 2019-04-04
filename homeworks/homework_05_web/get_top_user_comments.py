import sys

# Ваши импорты
import csv
from bs4 import BeautifulSoup
import requests
import collections
import aiohttp
import asyncio


async def func(link, file):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            if (resp is not None):
                text = resp.text()
                await text
    soup = BeautifulSoup(text, 'html.parser')
    user_list = []
    d = {}
    users = soup.findAll('span', attrs={'class': 'user-info__nickname_comment'})
    for i in range(len(users)):
        user_list.append(users[i].contents[0])
        d[users[i]] = None
    for user in d:
        d[user] = users_list.count(user)
    sort_d = sorted(d.items(), lambda item: item[1], reverse=True)
    out = (link, collections.OrderedDict(sort_d))
    out = sorted(out, lambda item: sum(item[1].values()), reverse=True)
    print_csv(file, out)


def print_csv(file, out):
    with open(file, 'w') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['link', 'username', 'count_comment'])
        dict_writer.writeheader()
        for link_user in out:
            for user in link_user[1]:
                dict_writer.writerow({'link': link_user[0], 'username': user, 'count_comment': link_user[1][user]})


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]
    # Ваш код

    lop = asyncio.get_event_loop()
    task = [asyncio.ensure_future(func(q, filename)) for q in range(len(links))]
    result = asyncio.wait(task)
    lop.run_until_complete(result)
    lop.close()
