import sys
import csv
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from collections import Counter, OrderedDict


async def get_page(link):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as r:
            html = await r.text()
            return html


def parser(html):
    soup = BeautifulSoup(html, "lxml")
    tags_a = soup.findAll(
        "a", attrs={"class": ["user-info user-info_inline"], "data-user-login": [True]}
    )
    users_list = [tags_a[i]["data-user-login"] for i in range(len(tags_a))]
    comment_d = OrderedDict(Counter(users_list).most_common())
    return comment_d


async def collect_links(links):
    result = await asyncio.gather(*(get_page(link) for link in links))
    return result


def write_csv(filename, links):
    links.sort()
    data_list = list(asyncio.run(collect_links(links)))
    end = dict()
    with open(filename, mode="w") as csv_file:
        fieldnames = ["link", "username", "count_comment"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(data_list)):
            out = parser(data_list[i])
            for res in sorted(out, key=out.get, reverse=True):
                end[res] = out[res]
            for key in end:
                writer.writerow(
                    {"link": links[i], "username": key, "count_comment": end[key]}
                )


if __name__ == "__main__":
    filename = "top_user_comments.csv"
    links = sys.argv[1:4]
    write_csv(filename, links)
