import sys
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import requests
import operator
import csv


def make_all(link):
    users = []
    page = link
    soup = BeautifulSoup(page, 'html.parser')
    comments = soup.find_all('span', attrs={'class': [
                             'user-info__nickname user-info__nickname_small user-info__nickname_comment']})
    for comm in comments:
        users.append(comm.text)
    user_dict = {}
    for us in users:
        user_dict[us] = users.count(us)
    user_dict = sorted(user_dict.items(), key=operator.itemgetter(1))[::-1]
    return user_dict


def csv_writer(fin, csv_file, link, csvwriter):
    for user, rate in fin:
        csvwriter.writerow([link, user, rate])


async def asnc(link, csv_file, csvwriter):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            fin = make_all(await resp.text())
            csv_writer(fin, csv_file, link, csvwriter)

if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]
    with open(filename, mode='w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(['link', 'username', 'count_comment'])
        tasks = []
        loop = asyncio.get_event_loop()
        for link in links:
            tasks.append(loop.create_task(asnc(link, csv_file, csvwriter)))
        loop.run_until_complete(asyncio.wait(tasks))
        csv_file.close()
        loop.close()
