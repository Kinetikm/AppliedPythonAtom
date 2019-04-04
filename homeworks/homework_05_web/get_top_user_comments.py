import sys
import requests
from bs4 import BeautifulSoup
from collections import Counter
import asyncio
import csv


async def parser(url):
    user_comm = list()
    user_com_itog = list()

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    soup_find = soup.find_all('div', attrs={"class": ["comment__head"]})

    for i in enumerate(soup_find):
        user_comm.append((soup_find[list(i)[0]].find('a')['data-user-login']))

    user_comm_c = Counter()
    for word in user_comm:
        user_comm_c[word] += 1

    for key, value in user_comm_c.items():
        user_com_itog.append({"link": url, "username": key, "count_comment": value})

    sort_user_com = sorted(user_com_itog, key=lambda x: (-x["count_comment"], x['username']))
    return sort_user_com


def form_file(user_comment, file_name):
    sort_link = [j for i in user_comment for j in i.result()]
    sorted_link = sorted(sort_link, key=lambda x: x['link'])

    with open(file_name, "w", newline="") as file:
        write_csv = csv.DictWriter(file, fieldnames=["link", "username", "count_comment"])
        write_csv.writeheader()
        write_csv.writerows(sorted_link)


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]

    user_comments = list()
    io_loop = asyncio.get_event_loop()
    for link in links:
        user_comments.append(io_loop.create_task(parser(link)))
    io_loop.run_until_complete(asyncio.wait(user_comments))
    io_loop.close()

    form_file(user_comments, filename)
