import sys


# Ваши импорты
from com.parse import link_parser
from com.output import out_writer
from com.handler import dict_handler
from collections import OrderedDict
import operator
import asyncio


async def main(filename, links):
    data = dict()
    tasks = []
    for link in links:
        tasks.append(link_parser.parseLink(link))
    results = await asyncio.gather(*tasks)
    for items in results:
        count_to_username = dict_handler.reverse_dict_to_ordered(items[1])
        data.update({items[0]: count_to_username})
    sorted_data = OrderedDict(sorted(data.items(), key=operator.itemgetter(0)))
    out_writer.outputData(sorted_data, filename)


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]

    # Ваш код
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(filename, links))
