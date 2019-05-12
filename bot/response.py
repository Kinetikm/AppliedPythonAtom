#!/usr/bin/env python
# -*- coding: utf-8 -*-
from main import request_id, poisk_id,find_similar_subgroup, request_id_1

def response(text):
    #text = text.decode('utf-8','ignore')
    text = str(text)
    text = text.lower()
    print(text)
    #text = str(text)
    if len(text) > 50 :
        return u"Слишком длинный запрос"
    if u"привет" in text:
        return "Привет!"
    if u"пока" in text or u"bye" in text:
        return u"Пока"
    if u"?" in text:
        return u"Это вопрос!"
    if u"кто ты" in text or u"помощь" in text or u"help" in text:
        return "я бот"
    #s = poisk_id(zapros=str(text))
    if text.isdigit():
        s = "\nпохожие товары: "+str(request_id(a=int(text)))
        s = s+"\n\nзаменители: "+str(find_similar_subgroup(a=int(text)))
        s = s+"\n\nкомплиментарные товары: "+str(request_id_1(a=int(text)))
        return str(s)
    return str(poisk_id(zapros=text))
    #return u"Я пока такое не умею"

#print(response("0L/RgNC40LLQtdGC"))