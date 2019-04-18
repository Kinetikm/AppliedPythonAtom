from bs4 import BeautifulSoup
import requests
import asyncio
import aiohttp


def asparse(page):
    anstext = []
    undersoup = BeautifulSoup(page, 'html.parser')
    answers = undersoup.find_all('div', attrs={'class': 'post-text'})
    for answer in answers:
        if answer.find('p') is not None:
            anstext.append(answer.find('p').text)
    return anstext


async def asnc(link, title):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://stackoverflow.com' + link) as resp:
            fin = asparse(await resp.text())
            return title, fin


def parsing(link):
    reqdata = {}
    page = requests.get(link)
    if page.ok is True:
        soup = BeautifulSoup(page.content, 'html.parser')
        themes = soup.find_all('a', attrs={'class': 'question-hyperlink'})
        tasks = []
        loop = asyncio.new_event_loop()
        for theme in themes:
            tasks.append(loop.create_task(asnc(theme['href'], theme.text)))
        fin = loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
        for i in fin[0]:
            if i._result is not None:
                reqdata[i._result[0]] = i._result[1]
    return reqdata


def print_answers(req_title, database):
    print(req_title)
    themes = database.get(req_title)
    for theme in themes:
        print('\t' + theme)
        answers = themes.get(theme)
        for answer in answers:
            print('\t\t' + answer)


def make_response(answers):
    if not isinstance(answers, dict):
        return answers
    resp = ''
    for ans in answers:
        resp += '+' * 10 + ans + '+' * 10 + '\n'
        a = answers.get(ans)
        for i in a:
            resp += i + '\n'
    return resp
