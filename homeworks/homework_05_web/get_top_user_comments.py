import concurrent
import csv
import sys
from collections import Counter
from concurrent.futures import as_completed

import requests
from bs4 import BeautifulSoup


def parse_habr(link):
    r = requests.get(link)

    soup = BeautifulSoup(r.text, "html.parser")
    comment = soup.find_all("div", attrs={"class": "comment"})
    count = Counter()
    for comm in comment:
        commentator_name = comm.find('a').find('span').text
        if not count[commentator_name]:
            count[commentator_name] = 0
        count[commentator_name] += 1

    return count, link


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]

    result = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:

        futures = [executor.submit(parse_habr, link) for link in links]

        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            try:
                data = future.result()
                result.append(data)
            except Exception as exc:
                print(exc, i, future)
            finally:
                pass

        with open(filename, 'w+') as csv_file:
            for tup in result:
                cnt, href = tup
                for count_elem in cnt.most_common():
                    login, count_ = count_elem

                    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow([href, login, count_])
