import sys
import requests
from bs4 import BeautifulSoup
import collections
import operator
import csv
import concurrent.futures


def parse_page(link, file_name):

    with requests.get(link) as r:

        soup = BeautifulSoup(r.text, "html.parser")
        temp = soup.find_all('span', attrs={
            "class": ["user-info__nickname user-info__nickname_small user-info__nickname_comment"]})

        names = []
        for i in temp:
            names.append(i.text)

        name_dict = collections.Counter()
        for word in names:
            name_dict[word] += 1

        sort_name_dict = sorted(name_dict.items(), key=operator.itemgetter(1))
        sort_name_dict.reverse()

        top_user_comments = dict()
        for i in sort_name_dict:
            top_user_comments[i[0]] = i[1]

        with open(file_name, 'a') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in top_user_comments.items():
                writer.writerow([link, key, value])


if __name__ == '__main__':
    file_name = 'top_user_comments.csv'

    with open(file_name, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['link', 'username', 'count_comment'])

    links = sorted(sys.argv[1:])

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(links)) as executor:
        future_to_link = {executor.submit(parse_page, link, file_name): link for link in links}
        for future in concurrent.futures.as_completed(future_to_link):
            link = future_to_link[future]
            try:
                future.result()
            except Exception as exc:
                print(exc, future)
