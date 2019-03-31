import sys


# Ваши импорты
from com.parse import link_parser
from com.output import out_writer
from com.handler import dict_handler
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import requests
import os

if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]

    # Ваш код
    data = dict()
    for link in links:
        count_to_username = dict_handler.reverse_dict_to_ordered(link_parser.parseLink(link))
        data.update({link: count_to_username})
    out_writer.outputData(data)
