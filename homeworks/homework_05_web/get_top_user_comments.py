import concurrent
import csv
import sys
from collections import Counter
from concurrent.futures import as_completed

import requests
from bs4 import BeautifulSoup


# def write_data(href, login, count_):
#     return href + ';' + login + ';' + str(count_) + ';\n'

def parse_habr(link):
    r = requests.get(link)

    soup = BeautifulSoup(r.text, "html.parser")
    comment = soup.find_all("div", attrs={"class": "comment"})
    cnt = Counter()
    for comm in comment:
        commentator_name = comm.find('a').find('span').text
        if not cnt[commentator_name]:
            cnt[commentator_name] = 0
        cnt[commentator_name] += 1

    # with lock:
    #     with open("top_user_comments.csv", 'w+') as csv_file:
    #         for count_elem in cnt.most_common():
    #             login = count_elem[0]
    #             count_ = count_elem[1]
    #             href = link
    #
    #             csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #             # print(write_data(href, login, count_))
    #             # csv_file.write(write_data(href, login, count_))
    #             csv_writer.writerow([href, login, count_])

    return (cnt, link)


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

        # results = executor.map(parse_habr, link, lock)

        with open(filename, 'w+') as csv_file:
            iter = 0
            for tup in result:
                cnt = tup[0]
                href = tup[1]
                for count_elem in cnt.most_common():
                    login = count_elem[0]
                    count_ = count_elem[1]

                    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow([href, login, count_])
                iter += 1
