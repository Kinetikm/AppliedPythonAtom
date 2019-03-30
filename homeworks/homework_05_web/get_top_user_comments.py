import sys
import aiohttp
import asyncio
from collections import defaultdict
from bs4 import BeautifulSoup


async def load_and_parse_page(url: str, data: dict) -> None:
    """Метод для загрузки и парсинга данных со страницы"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # Получение тела
            data[url] = {}
            tmp = data[url]
            tmp['users'] = defaultdict(lambda: {'rating': 0, 'comments': 0})
            tmp['total_comments'] = 0

            # Проверка статуса ответа
            if 200 <= resp.status < 300:
                soup = BeautifulSoup(await resp.text(), 'html.parser')
                # парсинг комментариев, сбор из них комментаторов
                # наша логика -> больше постов = выше рейтинг
                for comment in soup.find_all('div', attrs={"class": ['comment__head']}):
                    user = comment.find('a')['data-user-login']
                    tmp['users'][user]['comments'] += 1
                    tmp['total_comments'] += 1
                    # Получение суммарного рейтинга по комментариям
                    rating = comment.find('div', attrs={"class": ['voting-wjt']})\
                        .find('span', attrs={"class": ['voting-wjt__counter']}).text
                    if '–' in rating:
                        rating = '-' + rating[1:]
                    tmp['users'][user]['rating'] += int(rating)


async def prepare_tasks(urls: list) -> dict:
    """Метод для подготовки и пост обработки задач"""
    data = {}  # dict()

    tasks = [load_and_parse_page(url, data) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if result is not None:
            try:
                raise result
            except aiohttp.InvalidURL:
                # Кривой url -> удаление его из обработки
                url = str(sys.exc_info()[1])
                urls.remove(url)

    return data


def main_method(file: str, urls: list) -> list:
    """
    Распарсить 3 любые статьи с https://habr.com с числом комментариев > 100.
    Построить рейтинг комментаторов по каждой из статьи,
    результаты записать в файл top_user_comments.csv в формате csv
    (link,username,count_comment).
    Где link - это ссылка на статью,
    username - ник пользователя,
    count_comment - количество комментариев пользователя в статье.

    Данные сливать в один файл, сортировка должна быть по link,
    count_comment с группировкой link, username.

    Получается один username может встретится 3 раза,
    потому что комментировал 3 статьи. Скрипт запускать с помощью команды:
    python3 get_top_user_comments.py link1 link2 link3

    :param file: имя файла в который сохранять данные
    :param urls: список ссылок с которых парсить данные (links)
    """
    # Получение нужных данных
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(prepare_tasks(urls))
    loop.close()

    # сортировка urls по убыванию количества комментариев
    urls.sort(key=lambda k: data[k]['total_comments'], reverse=True)

    # открытие файла (на перезапись)
    with open(file, mode='w') as f:
        # запись заголовка
        f.write('link,username,count_comment\n')
        # запись данных
        for url in urls:
            users = sorted(
                data[url]['users'].keys(),
                key=lambda k: data[url]['users'][k]['comments'],
                reverse=True)
            for user in users:
                comments = str(data[url]['users'][user]['comments'])
                f.write(url + ',' + user + ',' + comments + '\n')

    # Список обработанных ссылок
    return urls


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]
    res = main_method(filename, links[:])
    if res != links:
        print(f'Некоторые ссылки не были корректно обработаны: {set(links) - set(res)}')
