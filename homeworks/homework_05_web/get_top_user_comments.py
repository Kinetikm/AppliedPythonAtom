import sys
from bs4 import BeautifulSoup
import re
import collections
import requests

# Ваши импорты

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}


def parce_and_write(link):
    response = BeautifulSoup(requests.get(link, headers=headers).text, 'html.parser')
    result = [re.sub('<.+?>', '', str(user))
              for user in response.findAll('span', attrs={'class': 'user-info__nickname_comment'})]
    users = collections.Counter()
    for word in result:
        users[word] += 1
    users = users.most_common()
    print(users)
    try:
        with open(filename, 'a') as file:
            file.write('link, username, count_of_comments \n')
            for user in users:
                file.write(link + ',' + user[0] + ',' + str(user[1]) + '\n')
    except IOError:
        print("An IOError has occurred")


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]
    links.sort()
    for link in links:
        parce_and_write(link)

    # Ваш код
