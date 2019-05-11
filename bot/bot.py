#!/usr/bin/env python
# -*- coding: utf-8 -*-
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
from response import response
#import MySQLdb
import datetime
import requests
from login import isLogin, isAdmin, login
from secret import tokenVK #вынес пароль в отдельный файл
from admin import adminresponce
import bs4

#from tokens import generateUsers, getTokens

keyb="""{
  "one_time": false,
  "buttons": [
    [{
      "action": {
        "type": "text",
        "label": "Nice answer!"
      },
      "color": "positive"
    },
      {
        "action": {
          "type": "text",
          "label": "Normal answer."
        },
        "color": "positive"
      }],
    [{
      "action": {
        "type": "text",
        "label": "Bad answer!"
      },
      "color": "default"
    }]
  ]
}"""

def _get_user_name_from_vk_id(user_id):
    request = requests.get("https://vk.com/id"+str(user_id))
    bs = bs4.BeautifulSoup(request.text, "html.parser")

    user_name = str(bs.findAll("title")[0])
    user_name = user_name.replace("<title>","")
    return user_name.split()[0]


def main():
    badansw=0
    normalansw=0
    niceansw=0

    tok = tokenVK()
    vk_session = vk_api.VkApi(token=tok)

    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

            if isAdmin(str(event.user_id)):
                try:
                    text = (event.text).encode('utf-8')
                    time = str(datetime.datetime.now())
                    time = time[:19]
                    print(str(event.user_id)+"  "+text)

                    res = _get_user_name_from_vk_id(event.user_id)+", "+adminresponce(text)
                    vk.messages.send(user_id = event.user_id, message = res, random_id = randint(0, 9999),keyboard=keyb)

                except Exception as e:
                    requests.post("http://danr0.pythonanywhere.com/api/err/", data = str(event.user_id)+"$"+str(e)+"$"+time)
                    print(str(e.message))
            elif isLogin(str(event.user_id)):
                try:
                    text = (event.text).encode('utf-8')
                    time = str(datetime.datetime.now())
                    time = time[:19]

                    print(str(event.user_id)+"  "+text)
                    if text == "Nice answer!":
                        niceansw+=1
                        res="Уже "+str(niceansw)+" nice answers"
                    elif text == "Bad answer!":
                        badansw+=1
                        res="Уже "+str(badansw)+" bad answers"
                    elif text == "Normal answer.":
                        normalansw+=1
                        res="Уже "+str(normalansw)+" normal answers"
                    else:
                        text = str(text.encode('base64'))
                        text = text.replace("\n",'')
                        res = _get_user_name_from_vk_id(event.user_id)+", "+response(text)#заглушка со стандартнами ответами, потом сюда прикрутим нормальные ответы
                    vk.messages.send(user_id = event.user_id, message = res, random_id = randint(0, 9999),keyboard=keyb)
                    #requests.post("http://danr0.pythonanywhere.com/api/req/", data = str(event.user_id)+"$"+str(text)+"$"+time)
                except Exception as e:
                #логирование ошибок
                    requests.post("http://danr0.pythonanywhere.com/api/err/", data = str(event.user_id)+"$"+str(e)+"$"+time)
                    print(str(e.message))
            else:
                try:
                    text = (event.text).encode('utf-8')
                    time = str(datetime.datetime.now())
                    time = time[:19]
                    res = login(str(event.user_id), text)
                    vk.messages.send(user_id = event.user_id, message = res, random_id = randint(0, 9999),keyboard=keyb)
                    print(str(event.user_id)+"  "+text)
                    #text = str(text.encode('base64'))
                    #text = text.replace("\n",'')
                    #requests.post("http://danr0.pythonanywhere.com/api/req/", data = str(event.user_id)+"$"+str(text)+"$"+time)
                except Exception as e:
                    #логирование ошибок
                    requests.post("http://danr0.pythonanywhere.com/api/err/", data = str(event.user_id)+"$"+str(e)+"$"+time)
                    print(str(e.message))


if __name__ == '__main__':
    main()