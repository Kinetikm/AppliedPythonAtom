from gensim.models import Word2Vec
import pickle
from os import path
from annoy import AnnoyIndex
import numpy as np

W2V_PATH = path.join("data/word2vec.model")
PKL_PATH = path.join("data/Product_dict.pkl")
PRODUCT_W2V_PATH = path.join("data/product.model")
ANNOY_PATH = path.join("data/product.ann")


class Model:

    def __init__(self):
        self.product_w2v = Word2Vec.load(PRODUCT_W2V_PATH)
        self.w2v = Word2Vec.load(W2V_PATH)
        self.product_annoy = AnnoyIndex(100)
        self.product_annoy.load(ANNOY_PATH)
        with open(PKL_PATH, 'rb') as f:
            pkl = pickle.load(f)
        self.products = dict()
        for i in pkl:
            try:
                self.products[int(i)] = pkl[i].split(") ")[1]
            except IndexError:
                pass

    def most_similar_id(self, id: int):
        try:
            out = self.w2v.wv.most_similar([str(id)], topn=1)
        except KeyError:
            print("{} id is wrong".format(id))
            return None
        try:
            print(out)
            return self.products[int(out[0][0])]
        except KeyError:
            print("WTF")
            return None

    def predict_output_id(self, id: int):
        try:
            out = self.w2v.predict_output_word([str(id)], topn=1)
        except KeyError:
            print("{} id is wrong".format(id))
            return None
        try:
            print(out)
            return self.products[int(out[0][0])]
        except KeyError:
            print("WTF")
            return None

    def predict_output_name(self, text: str):
        text = text.lower().split()
        vecs = list()
        for i in text:
            try:
                vec = self.product_w2v.wv[i]
                vecs.append(vec)
            except KeyError:
                pass
        if len(vecs) > 0:
            res = np.array(vecs[0])
            for i in range(1, len(vecs)):
                res += vecs[i]
            id = self.product_annoy.get_nns_by_vector(res, 1)
            return self.predict_output_id(int(id[0]))
        else:
            return None

    def most_popular_name(self, text: str):
        text = text.lower().split()
        vecs = list()
        for i in text:
            try:
                vec = self.product_w2v.wv[i]
                vecs.append(vec)
            except KeyError:
                pass
        if len(vecs) > 0:
            res = np.array(vecs[0])
            for i in range(1, len(vecs)):
                res += vecs[i]
            id = self.product_annoy.get_nns_by_vector(res, 1)
            return self.most_similar_id(int(id[0]))
        else:
            return None
