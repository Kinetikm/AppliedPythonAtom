from hackathon.vk_api import vk_bot_api
from hackathon.machine.Answerer import Answerer
import requests


def get_answer(body, name, f, check):
    answerer = Answerer()
    answerer.predict(body)

    if check == 1:
        message = 'Привет ' + name + ', я новый бот!' + ' your_token ' + str(f)
    elif check == 2:
        message = 'Привет ' + name + ', я новый бот!' + ' ты на стороне зла '
    elif check == 3:
        message = 'Привет ' + name + ', я новый бот! ' + str(f)
    elif check == 4:
        message = 'Привет ' + name + ', я новый бот! ' + ' your mass : ' + body
    return message


def create_answer(data, token):
    user_id = data['user_id']
    resp = requests.post('https://api.vk.com/method/users.get?user_id=' + str(
        user_id) + '&access_token=4645c5e2f5d643d17ccf64f33ea8368ac407e4153091'
                   '9e5eaeb75c17f65c6e7fa6ab13544cf0788f7757e&v=5.52')
    name = resp.json()['response'][0]['first_name']
    uy = requests.post(
        'https://api.vk.com/method/storage.get' +
        '&access_token=4645c5e2f5d643d17ccf64f33ea8368ac407e41530919e5eaeb75c'
        '17f65c6e7fa6ab13544cf0788f7757e&v=5.52')
    USER = uy.json()['request_params'][0]['value']
    if USER == '0':
        check = aut(data, name, user_id)
        f = check[1]
        check1 = check[0]
        vk_bot_api.api.storage.set(key='user', value=check[2])
    else:
        check = 4
        f = None
    message = get_answer(data['body'].lower(), name, f, check1)
    vk_bot_api.send_message(user_id, token, message)


def aut(data, name, user_id):
    from hackathon import database1
    user = '0'
    s = str(data['body'].lower())
    check = 0
    if s[0:12] == 'start token:':
        tokk = s[12:]
        f = database1.get_account(user_id, name)
        if tokk == str(f[0]):
            check = 2
            f = None
            user = '1'
    else:
        f = database1.get_account(user_id, name)
        if f[1]:
            f = 'введи свой токен, ты уже зарегистрирован! вводить токен' \
                ' так: token:token'
            check = 3
        else:
            check = 1
            user = '1'
    return check, f, user
