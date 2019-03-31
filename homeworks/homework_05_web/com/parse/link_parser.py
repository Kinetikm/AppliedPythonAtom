#!/usr/bin/env python
# coding: utf-8

import aiohttp
from bs4 import BeautifulSoup
from user_agent import generate_user_agent


async def parseLink(link):
    username_to_count = dict()
    async with aiohttp.ClientSession() as session:
        async with session.get(link,
                               headers={'Content-type': 'text/html',
                                        'User-Agent': generate_user_agent(),
                                        'Content-Encoding': 'utf-8'},
                               ) as resp:
            if resp.status != 200:
                return link, username_to_count
            parsed = BeautifulSoup(await resp.text(), 'html.parser')
            for tag in parsed.findAll("a", attrs={"class": ["user-info user-info_inline"]}):
                username = tag["data-user-login"]
                if username not in username_to_count:
                    username_to_count[username] = 0
                username_to_count[username] += 1
    return link, username_to_count
