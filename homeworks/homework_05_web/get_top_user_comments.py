import sys
import csv
import asyncio
from collections import defaultdict
import aiohttp
from aiohttp.client_exceptions import ClientResponseError, ClientConnectorError
from bs4 import BeautifulSoup


def parse_page(html_txt):
    """
    Parse page for commentators
    :param html_txt:
    :return: Top chart of commentators and total count of comments
    """
    soup = BeautifulSoup(html_txt, 'html.parser')
    counter = defaultdict(int)
    comments_count = 0

    for comment in soup.find_all('div', attrs={"class": ['comment__head']}):
        user = comment.find('a')['data-user-login']
        comments_count += 1
        counter[user] += 1

    return sorted(counter.items(), key=lambda c: c[1], reverse=True), comments_count


async def fetch(session, url):
    """
    Fetch a URL using aiohttp.
    As suggested by the aiohttp docs we reuse the session.
    :param session: session of aiohttp.ClientSession
    :param url:
    :return: text with html
    """
    async with session.get(url) as resp:
        return await resp.text()


async def process_page(session, url):
    """
    Counts the top chart of commentators for url.
    :param session:
    :param url:
    :return: tuple of url, chart of commentators and total count comments of url
    """
    txt_html = await fetch(session, url)
    top_commentators, comments_count = parse_page(txt_html)
    return url, [(nick, count) for nick, count in top_commentators], comments_count


async def gather_tasks(session, urls):
    tasks = [process_page(session, url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return [result for result in results if not isinstance(result, (ClientResponseError, ClientConnectorError))]


def save_result(filename, top_list):
    """
    Save result to csv.
    :param filename:
    :param top_list:
    :return:
    """
    print(filename)
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['link', 'username', 'count_comment'])
        # for row in top_list:
        writer.writerows(top_list)


async def top_commentators(loop, urls, filename):
    """
    Строит рейтинг комментаторов по каждой из статьи, результаты записать в файл в формате csv
    (link,username,count_comment). Где link - это ссылка на статью, username - ник пользователя, count_comment -
    количество комментариев пользователя в статье.
    Данные сливаются в один файл, сортировка по link, count_comment с группировкой link,username.
    :param loop:
    :param urls:
    :param filename:
    """
    async with aiohttp.ClientSession(loop=loop, raise_for_status=True) as session:
        results = await gather_tasks(session, urls)
    results.sort(key=lambda item: item[2], reverse=True)
    top_list = [(res[0], nick, count) for res in results for nick, count in res[1]]
    save_result(filename, top_list)


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(top_commentators(loop, links, filename))
    loop.close()
