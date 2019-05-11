import re
import sys
import json
import gzip
import logging
import itertools
import pymorphy2
import numpy as np
import pandas as pd
from annoy import AnnoyIndex
from gensim.models.word2vec import Word2Vec
import pickle as pkl

Product_dict = pkl.load(open('Product_dict.pkl', 'rb'))
data=pd.read_csv('data.csv',nrows=100000)
data=data.applymap(str)
data['id']=data['contact_id']+' '+data['shop_id']+' ' +data['product_category_id']
data=data.drop(columns=['contact_id','shop_id','product_category_id'])
model = Word2Vec.load('./hackaton.w2v_gensim3')
model.similar_by_vector(model['1260627'] )
data_storage = {i[1]['product_id']:i[1]['id'] for i in data.iterrows()}
index_img_emb = AnnoyIndex(100)
index_img_emb.load('./hackaton_annoy_30')
map_id_hashimg = pkl.load(open('hackaton_map_id_to_hash_products.dict5', 'rb'))
prod1 = pd.read_csv('prod111.csv')
prod1.fillna(value='', inplace=True)
prod1=prod1.applymap(str)
prod1.drop(prod1.columns[prod1.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)


def request_id(a=134832):
    pr = data.loc[data['product_id'] == str(a)]
    pr.reset_index(inplace=True, drop=False)
    vector = pr['id'][0]

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

