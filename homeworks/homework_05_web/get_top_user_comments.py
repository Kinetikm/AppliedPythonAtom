import sys
from bs4 import BeautifulSoup
import re
import collections
import asyncio
import aiohttp

# Ваши импорты

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}


async def get_html_page(link):
    async with aiohttp.ClientSession() as session:
        async with session.get(link, headers=headers) as res:
            page = await res.text()
            return page


async def main(links):
    result = await asyncio.gather(*(get_html_page(link) for link in links))
    return result


def write_to_file(filename, links):
    data_to_record = list(asyncio.run(main(links)))
    result_dict = dict()
    try:
        with open(filename, 'w') as file:
            file.write("link, username, count_comments \n")
            for index in range(len(data_to_record)):
                buf = parser(data_to_record[index])
                for tmp in sorted(buf, key=buf.get, reverse=True):
                    result_dict[tmp] = buf[tmp]
                for user in result_dict:
                    file.write(links[index] + "," + user + "," + str(result_dict[user]) + "\n")
    except IOError:
        print("An IOError has occurred")


def parser(page):
    page_to_work_with = BeautifulSoup(page, "html.parser")
    result = [re.sub('<.+?>', '', str(user))
              for user in page_to_work_with.findAll('span', attrs={'class': 'user-info__nickname_comment'})]
    users = collections.Counter()
    for word in result:
        users[word] += 1
    users_result = collections.OrderedDict(users.most_common())
    return users_result


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]
    links.sort()
    write_to_file(filename, links)

    # Ваш код
