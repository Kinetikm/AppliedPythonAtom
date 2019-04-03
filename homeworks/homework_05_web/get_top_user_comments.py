import sys
import csv
from bs4 import BeautifulSoup
import re
from collections import Counter, OrderedDict
import asyncio
import aiohttp


# Ваши импорты

async def create_html_queue(link: str, async_queue: asyncio.Queue):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            if response is not None:
                await async_queue.put((link, await response.text()))


async def work_with_html_queue(async_queue: asyncio.Queue):
    link, text = await async_queue.get()
    html = BeautifulSoup(text, 'html.parser')
    users_list = [re.sub(f'<.+?>', '', str(user))
                  for user in html.findAll
                  ('span', attrs={'class': 'user-info__nickname_comment'})]
    comments_dict = OrderedDict(Counter(users_list).most_common())
    async_queue.task_done()
    return link, comments_dict


def write_to_file(filename: str, result: list):
    with open(filename, 'w') as file:
        field_names = ['link', 'username', 'count_comment']
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for article in result:
            for user in article[1]:
                writer.writerow({'link': article[0], 'username': user, 'count_comment': article[1][user]})


async def main(filename: str, links: list):
    async_queue = asyncio.Queue()
    get_html = [asyncio.create_task(create_html_queue(link, async_queue)) for link in links]
    process_html = [asyncio.create_task(work_with_html_queue(async_queue)) for _ in range(len(links))]
    result = sorted(await asyncio.gather(*process_html),
                    key=lambda links_dict: sum(links_dict[1].values()),
                    reverse=True)
    write_to_file(filename, result)


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]
    # Ваш код
    asyncio.run(main(filename, links))
