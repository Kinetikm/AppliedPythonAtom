import pickle as pkl
from annoy import AnnoyIndex
import string
from gensim.models import KeyedVectors
import numpy as np
import pymorphy2 as morphy
from functools import lru_cache


class Answerer:

    def __init__(self, index_img_emb='./annoy_20',
                 map_id_hashimg='map_id_to_hash_products.dict4'):
        self.X = AnnoyIndex(100)
        self.X.load('X_annoy')
        self.Y = pkl.load(open('map_id_to_hash_products.dict', 'rb'))
        self.morpher = morphy.MorphAnalyzer()

    w2v_fpath = "all.norm-sz100-w10-cb0-it1-min100.w2v"
    w2v = KeyedVectors.load_word2vec_format(w2v_fpath, binary=True,
                                            unicode_errors='ignore')

    @lru_cache(maxsize=100000)
    def get_normal_form(self, word):
        return self.morpher.normal_forms(word)[0]

    def _normalize_text(self, text):
        text = text.translate(str.maketrans(string.punctuation, ' ' * len(
            string.punctuation))).lower()
        words = text.split()
        normalized_text = ''
        for word in words:
            normalized_text += self.get_normal_form(word) + ' '

        return normalized_text.rstrip()

    def _text_vectorize(self, text):
        text = self._normalize_text(text)
        words = text.split()

        vector = np.zeros(shape=100)
        for word in words:
            try:
                vector += self.w2v[word]
            except:
                continue
        return vector / len(words)

    def predict(self, x):
        x_vec = self._text_vectorize(x)
        idx = self.X.get_nns_by_vector(x_vec, 1)

        return self.Y[idx[0]][0]
