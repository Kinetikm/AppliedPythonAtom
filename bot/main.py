import itertools
import numpy as np
import pandas as pd
from annoy import AnnoyIndex
from gensim.models.word2vec import Word2Vec
import pickle as pkl

Product_dict = pkl.load(open('Product_dict.pkl', 'rb'))
data = pd.read_csv('data_2.csv')
data = data.applymap(str)
data.drop(data.columns[data.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
model = Word2Vec.load('./hackaton.w2v_gensim3')
model.similar_by_vector(model['1260627'])
data_storage = {i[1]['product_id']: i[1]['id'] for i in data.iterrows()}
index_img_emb = AnnoyIndex(100)
index_img_emb.load('./hackaton_annoy_30')
map_id_hashimg = pkl.load(open('hackaton_map_id_to_hash_products.dict5', 'rb'))
index_img_emb1 = AnnoyIndex(100)
index_img_emb1.load('./hackaton_annoy_100')
map_id_hashimg1 = pkl.load(open('hackaton_map_id_to_hash_products.dict100', 'rb'))
prod1 = pd.read_csv('prod111.csv')
prod1.fillna(value='', inplace=True)
prod1 = prod1.applymap(str)
prod1.drop(prod1.columns[prod1.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)


# i) Рекомендуем похожие товары по id-шнику .возвращает имена  в ответ на id
def request_id(a=134832):
    pr = data.loc[data['product_id'] == str(a)]
    pr.reset_index(inplace=True, drop=False)
    vector = str(pr['id'])
    vec = np.zeros(100)
    for word in vector.split(' '):
        if word in model:
            vec += model[word]

    data_storage_norm1 = vec
    annoy_res = list(index_img_emb.get_nns_by_vector(data_storage_norm1, 13, include_distances=True, search_k=10000))
    print('\n\nСоседи:')
    a = list()
    for annoy_id, annoy_sim in itertools.islice(zip(*annoy_res), 13):
        image_id = map_id_hashimg[annoy_id]
        # print(image_id)
        # print(data_storage[image_id], 1 - annoy_sim ** 2 / 2)
        a.append(list(prod1.loc[prod1['index'] == str(image_id)]['0']))

    return a


# iii) Обрабатываем текстовый запрос вместе id-шника. возвращает имена  в ответ на на запрос в виде строки str
def poisk_id(zapros='Колдрекс'):
    zapros = str(zapros)
    lst = []
    lst_id = []
    lst_final = []
    for k, v in Product_dict.items():
        lst.append((k, v))
    for lek in lst:
        if zapros.lower() in lek[1].lower():
            lst_id.append(lek[0])
    for el in lst_id:
        lst_final.append(list((data['id'][data.product_id == el])))
    vector = lst_final[0][0]
    vec = np.zeros(100)
    for word in vector.split(' '):
        if word in model:
            vec += model[word]

    data_storage_norm1 = vec
    annoy_res = list(index_img_emb.get_nns_by_vector(data_storage_norm1, 13, include_distances=True, search_k=10000))
    # print('\n\nСоседи:')
    a = list()
    for annoy_id, annoy_sim in itertools.islice(zip(*annoy_res), 13):
        image_id = map_id_hashimg[annoy_id]
        # print(image_id)
        # print(data_storage[image_id], 1 - annoy_sim ** 2 / 2)
        a.append(list(prod1.loc[prod1['index'] == str(image_id)]['0']))

    return a
    # Товары, предлагаемые как заменители гарантированно из той же подкатегории


def find_similar_subgroup(a=134832):
    pr = data.loc[data['product_id'] == str(a)]
    pr.reset_index(inplace=True, drop=False)
    vector = pr['id'][0]
    group = pr['product_sub_category_id'][0]
    # print(group)
    vec = np.zeros(100)
    for word in vector.split(' '):
        if word in model:
            vec += model[word]

    data_storage_norm1 = vec
    annoy_res = list(index_img_emb.get_nns_by_vector(data_storage_norm1, 500, include_distances=True, search_k=10000))
    a = list()
    d = (data.loc[data['product_sub_category_id'] == str(group)])
    for annoy_id, annoy_sim in itertools.islice(zip(*annoy_res), 500):
        image_id = map_id_hashimg[annoy_id]
        # print(image_id)
        # print(data_storage[image_id], 1 - annoy_sim ** 2 / 2)
        if (any(d['product_id'] == image_id)):
            a.append(list(prod1.loc[prod1['index'] == str(image_id)]['0']))
    return a


# Рекомендуем комплиментарные товары по id-шнику - 1 балл
def request_id_1(a=134832):
    pr = data.loc[data['product_id'] == str(a)]
    pr.reset_index(inplace=True, drop=False)
    vector = str(pr['id'])

    vec = np.zeros(100)
    for word in vector.split(' '):
        if word in model:
            vec += model[word]

    data_storage_norm1 = vec
    annoy_res = list(index_img_emb1.get_nns_by_vector(data_storage_norm1, 13, include_distances=True, search_k=10000))
    # print('\n\nСоседи:')
    a = list()
    for annoy_id, annoy_sim in itertools.islice(zip(*annoy_res), 13):
        image_id = map_id_hashimg1[annoy_id]
        # print(image_id)
        # print(data_storage[image_id], 1 - annoy_sim ** 2 / 2)
        a.append(list(prod1.loc[prod1['index'] == str(image_id)]['0']))

    return a
