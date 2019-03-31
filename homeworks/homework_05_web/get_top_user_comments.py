import sys
import asyncio
import aiohttp
import csv
from bs4 import BeautifulSoup


async def getdata(link):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            data = await resp.text()
            return data


async def main(links):
    res = await asyncio.gather(*(getdata(link) for link in links))
    return res


def parser(data):
    soup = BeautifulSoup(data, "html.parser")
    d = soup.findAll(
        "a", attrs={"class": ["user-info user-info_inline"], "data-user-login": [True]}
    )
    out = dict()
    for i in range(len(d)):
        user = d[i]["data-user-login"]
        if user in out:
            out[user] += 1
        else:
            out[user] = 1
    return out


if __name__ == "__main__":
    filename = "top_user_comments.csv"
    links = sys.argv[1:4]
    links.sort()
    listofdata = list(asyncio.run(main(links)))
    end = dict()
    with open(filename, mode="w") as csv_file:
        fieldnames = ["link", "username", "count_comment"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(listofdata)):
            out = parser(listofdata[i])
            for w in sorted(out, key=out.get, reverse=True):
                end[w] = out[w]
            for key in end:
                writer.writerow(
                    {"link": links[i], "username": key, "count_comment": end[key]}
                )
